"""Percorso ricovero end-to-end: Prenotazione -> Prericovero -> Ricovero.

Verifica che i tre sottotipi di ContattoPz coesistano, che i link opzionali del
percorso reggano e che il polimorfismo (joined-table inheritance) restituisca il
`tipo_contatto` corretto per ciascun sottotipo.
"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models.contatto_pz import ContattoPz
from app.models.prenotazione import Prenotazione


def _crea_paziente(client: TestClient, codice_fiscale: str = "RSSGNN70A01H501Z") -> int:
    payload = {
        "nome": "Giovanni",
        "cognome": "Russo",
        "data_nascita": "1970-01-01",
        "codice_fiscale": codice_fiscale,
    }
    return client.post("/pazienti", json=payload).json()["id"]


def test_percorso_completo_prenotazione_prericovero_ricovero(client: TestClient) -> None:
    paziente_id = _crea_paziente(client)

    prenotazione = client.post(
        f"/pazienti/{paziente_id}/prenotazioni",
        json={"data": "2026-07-01", "regime_ricovero": "Ordinario"},
    ).json()

    prericovero = client.post(
        f"/pazienti/{paziente_id}/prericoveri",
        json={"data_inizio": "2026-07-05", "prenotazione_id": prenotazione["id"]},
    ).json()
    assert prericovero["prenotazione_id"] == prenotazione["id"]
    assert prericovero["tipo_contatto"] == "prericovero"

    ricovero = client.post(
        f"/pazienti/{paziente_id}/ricoveri",
        json={
            "reparto": "Cardiochirurgia",
            "data_ricovero": "2026-07-10",
            "prenotazione_id": prenotazione["id"],
            "prericovero_id": prericovero["id"],
        },
    ).json()
    assert ricovero["prenotazione_id"] == prenotazione["id"]
    assert ricovero["prericovero_id"] == prericovero["id"]
    assert ricovero["tipo_contatto"] == "ricovero"

    # i tre contatti sono distinti ma appartengono allo stesso paziente
    assert len({prenotazione["id"], prericovero["id"], ricovero["id"]}) == 3


def test_ricovero_urgente_senza_prericovero(client: TestClient) -> None:
    """Un ricovero può nascere direttamente da una prenotazione (caso urgente)."""
    paziente_id = _crea_paziente(client, "RSSGNN70A01H501Y")
    prenotazione = client.post(
        f"/pazienti/{paziente_id}/prenotazioni", json={"data": "2026-07-01"}
    ).json()

    ricovero = client.post(
        f"/pazienti/{paziente_id}/ricoveri",
        json={
            "reparto": "Cardiochirurgia",
            "data_ricovero": "2026-07-02",
            "prenotazione_id": prenotazione["id"],
        },
    ).json()
    assert ricovero["prenotazione_id"] == prenotazione["id"]
    assert ricovero["prericovero_id"] is None


def test_polimorfismo_contatti_pz(client: TestClient, db_session: Session) -> None:
    """Interrogando la base ContattoPz si ottengono le istanze dei sottotipi giusti."""
    paziente_id = _crea_paziente(client, "RSSGNN70A01H501X")
    client.post(f"/pazienti/{paziente_id}/prenotazioni", json={"data": "2026-07-01"})
    client.post(f"/pazienti/{paziente_id}/prericoveri", json={"data_inizio": "2026-07-05"})
    client.post(
        f"/pazienti/{paziente_id}/ricoveri",
        json={"reparto": "Cardiochirurgia", "data_ricovero": "2026-07-10"},
    )

    contatti = db_session.query(ContattoPz).filter(ContattoPz.paziente_id == paziente_id).all()
    assert {c.tipo_contatto for c in contatti} == {"prenotazione", "prericovero", "ricovero"}


def test_backref_prenotazione_verso_ricovero_e_prericovero(
    client: TestClient, db_session: Session
) -> None:
    """I reverse ([NonPersistent] nel legacy) sono relationship navigabili."""
    paziente_id = _crea_paziente(client, "RSSGNN70A01H501W")
    prenotazione = client.post(
        f"/pazienti/{paziente_id}/prenotazioni", json={"data": "2026-07-01"}
    ).json()
    prericovero = client.post(
        f"/pazienti/{paziente_id}/prericoveri",
        json={"data_inizio": "2026-07-05", "prenotazione_id": prenotazione["id"]},
    ).json()
    client.post(
        f"/pazienti/{paziente_id}/ricoveri",
        json={
            "reparto": "Cardiochirurgia",
            "data_ricovero": "2026-07-10",
            "prenotazione_id": prenotazione["id"],
            "prericovero_id": prericovero["id"],
        },
    )

    p = db_session.get(Prenotazione, prenotazione["id"])
    db_session.refresh(p)
    assert p.prericovero is not None
    assert p.prericovero.id == prericovero["id"]
    assert p.ricovero is not None
    assert p.ricovero.prericovero.id == prericovero["id"]

from fastapi.testclient import TestClient


def _crea_paziente(client: TestClient, codice_fiscale: str = "BNCLCU90A41F205K") -> int:
    payload = {
        "nome": "Luca",
        "cognome": "Bianchi",
        "data_nascita": "1990-01-01",
        "codice_fiscale": codice_fiscale,
    }
    return client.post("/pazienti", json=payload).json()["id"]


def test_crea_prenotazione(client: TestClient) -> None:
    paziente_id = _crea_paziente(client)
    payload = {
        "data": "2026-07-01",
        "regime_ricovero": "Ordinario",
        "classe_priorita": "B",
        "stato": "DaEvadere",
    }
    response = client.post(f"/pazienti/{paziente_id}/prenotazioni", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["paziente_id"] == paziente_id
    assert body["tipo_contatto"] == "prenotazione"
    assert body["regime_ricovero"] == "Ordinario"
    assert body["classe_priorita"] == "B"
    # data_apertura del ContattoPz deriva dalla data prenotazione
    assert body["data_apertura"] == "2026-07-01"


def test_crea_prenotazione_data_default_oggi(client: TestClient) -> None:
    paziente_id = _crea_paziente(client, "BNCLCU90A41F205L")
    response = client.post(f"/pazienti/{paziente_id}/prenotazioni", json={})
    assert response.status_code == 201
    body = response.json()
    assert body["data"] is not None
    assert body["data"] == body["data_apertura"]


def test_crea_prenotazione_paziente_inesistente(client: TestClient) -> None:
    response = client.post("/pazienti/999999/prenotazioni", json={"data": "2026-07-01"})
    assert response.status_code == 404


def test_regime_ricovero_non_valido(client: TestClient) -> None:
    paziente_id = _crea_paziente(client, "BNCLCU90A41F205M")
    response = client.post(
        f"/pazienti/{paziente_id}/prenotazioni", json={"regime_ricovero": "Inesistente"}
    )
    assert response.status_code == 422


def test_lista_e_lettura_prenotazione(client: TestClient) -> None:
    paziente_id = _crea_paziente(client, "BNCLCU90A41F205N")
    created = client.post(
        f"/pazienti/{paziente_id}/prenotazioni", json={"data": "2026-07-01"}
    ).json()

    lista = client.get(f"/pazienti/{paziente_id}/prenotazioni")
    assert lista.status_code == 200
    assert len(lista.json()) == 1

    letta = client.get(f"/prenotazioni/{created['id']}")
    assert letta.status_code == 200
    assert letta.json()["id"] == created["id"]


def test_leggi_prenotazione_non_esistente(client: TestClient) -> None:
    assert client.get("/prenotazioni/999999").status_code == 404

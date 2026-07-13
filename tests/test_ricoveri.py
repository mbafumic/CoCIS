from fastapi.testclient import TestClient


def _crea_paziente(client: TestClient, codice_fiscale: str = "VRDGPP75B02F205X") -> int:
    payload = {
        "nome": "Giuseppe",
        "cognome": "Verdi",
        "data_nascita": "1975-02-02",
        "codice_fiscale": codice_fiscale,
    }
    return client.post("/pazienti", json=payload).json()["id"]


def _ricovero_payload() -> dict:
    return {
        "reparto": "Cardiochirurgia",
        "data_ricovero": "2026-07-01",
    }


def test_crea_ricovero(client: TestClient) -> None:
    paziente_id = _crea_paziente(client)
    response = client.post(f"/pazienti/{paziente_id}/ricoveri", json=_ricovero_payload())
    assert response.status_code == 201
    body = response.json()
    assert body["paziente_id"] == paziente_id
    assert body["tipo_contatto"] == "ricovero"
    assert body["stato"] == "aperto"
    assert body["data_apertura"] == "2026-07-01"


def test_crea_ricovero_paziente_inesistente(client: TestClient) -> None:
    response = client.post("/pazienti/999999/ricoveri", json=_ricovero_payload())
    assert response.status_code == 404


def test_lista_ricoveri(client: TestClient) -> None:
    paziente_id = _crea_paziente(client)
    client.post(f"/pazienti/{paziente_id}/ricoveri", json=_ricovero_payload())
    client.post(f"/pazienti/{paziente_id}/ricoveri", json=_ricovero_payload())

    response = client.get(f"/pazienti/{paziente_id}/ricoveri")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_leggi_ricovero(client: TestClient) -> None:
    paziente_id = _crea_paziente(client)
    created = client.post(f"/pazienti/{paziente_id}/ricoveri", json=_ricovero_payload()).json()

    response = client.get(f"/ricoveri/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_leggi_ricovero_non_esistente(client: TestClient) -> None:
    response = client.get("/ricoveri/999999")
    assert response.status_code == 404

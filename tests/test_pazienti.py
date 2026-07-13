from fastapi.testclient import TestClient


def _payload(codice_fiscale: str = "RSSMRA80A01H501U") -> dict:
    return {
        "nome": "Mario",
        "cognome": "Rossi",
        "data_nascita": "1980-01-01",
        "codice_fiscale": codice_fiscale,
    }


def test_crea_paziente(client: TestClient) -> None:
    response = client.post("/pazienti", json=_payload())
    assert response.status_code == 201
    body = response.json()
    assert body["nome"] == "Mario"
    assert body["codice_fiscale"] == "RSSMRA80A01H501U"
    assert "id" in body


def test_crea_paziente_codice_fiscale_duplicato(client: TestClient) -> None:
    client.post("/pazienti", json=_payload())
    response = client.post("/pazienti", json=_payload())
    assert response.status_code == 409


def test_leggi_paziente_non_esistente(client: TestClient) -> None:
    response = client.get("/pazienti/999999")
    assert response.status_code == 404


def test_leggi_paziente(client: TestClient) -> None:
    created = client.post("/pazienti", json=_payload()).json()
    response = client.get(f"/pazienti/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]

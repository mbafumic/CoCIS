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
    # campi opzionali non passati: valori di default
    assert body["sesso"] is None
    assert body["consenso_tratt_pers"] is False
    assert body["consenso_dossier"] is False


def test_crea_paziente_campi_opzionali(client: TestClient) -> None:
    payload = _payload("VRDLGU85C41F205Z") | {
        "sesso": "F",
        "eta": "45",
        "deceduto": False,
        "testimone_di_geova": False,
        "telefoni_paziente": "3331234567",
        "consenso_tratt_pers": True,
        "consenso_dossier": True,
        "codice_esterno": 42,
    }
    response = client.post("/pazienti", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["sesso"] == "F"
    assert body["eta"] == "45"
    assert body["telefoni_paziente"] == "3331234567"
    assert body["consenso_tratt_pers"] is True
    assert body["codice_esterno"] == 42


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

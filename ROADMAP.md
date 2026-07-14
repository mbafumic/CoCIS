# Roadmap

Tabella di marcia condivisa del progetto: **unica fonte di verità**. Ogni dev, da ogni
branch, legge e aggiorna questo file. La skill `/coscience` lo usa per dirti cosa fare e per
registrare gli avanzamenti.

Convenzioni:
- Una riga = una slice verticale (piccola, rilasciabile).
- Annota il branch accanto agli item *In corso*.
- Quando chiudi una slice spostala in *Fatto* con data e, se c'è, PR#.
- Non restare bloccato: se la tua PR è in review, prendi un item sbloccabile dal *Backlog*.

## In corso
- [ ] Anagrafica Paziente + ContattoPz (base, campi completi) + Ricovero (sottotipo) —
      prima slice MVP — branch: `feat/paziente-contatto-ricovero`. Paziente e ContattoPz
      ora includono tutti i campi scalari persistenti del legacy (con relative tabelle
      lookup: Comune, Regione, GruppoSanguigno, StatoCivile, Professione,
      PosizioneProfessionale, TipoDocumento, LivelloIstruzione, CategoriaPaziente, Stato,
      Asp, MedicoEsterno, PresidioOsp, Dipendente — questi ultimi due in versione minima,
      l'anagrafica organizzativa completa è nel Backlog) e i campi calcolati (Nominativo,
      Iniziali, IMC, Superficie Corporea, Comune_Provincia, ecc., come property Python /
      `computed_field` Pydantic, mai colonne DB). Le relazioni uno-a-molti verso altri
      domini (Telefoni, Parenti, Anamnesi, Fatture, Imaging, Microbiologia) sono state
      **rimandate a slice dedicate per dominio**, vedi Backlog. Codice, migration e test
      scritti; manca la verifica end-to-end (nessun PostgreSQL raggiungibile in questa
      sessione — da lanciare `uv run alembic upgrade head` + `uv run pytest` contro
      un'istanza reale prima di chiudere la slice).

## Backlog
- [ ] Modello Scheda Clinica polimorfica (Schederic→Schede, discriminatore + JSONB)
- [ ] Prenotazione + Prericovero (percorso ricovero: entrambi opzionali, con link
      incrociati a Prenotazione/Prericovero/Ricovero — vedi diagramma in CLAUDE.md)
- [ ] Prenotazione Ambulatorio + Prestazione Ambulatoriale (percorso ambulatoriale, link
      bidirezionale tra i due)
- [ ] Rilevazioni (parametri vitali, esami di laboratorio) collegate al Ricovero
- [ ] Procedure previste / effettuate collegate al Ricovero
- [ ] SDO / SDO10 (scheda dimissione ospedaliera)
- [ ] Contatti telefonici (Telefoni/TelefoniPz — uno-a-molti da ContattoPz)
- [ ] Parenti del paziente (uno-a-molti da Paziente)
- [ ] Anamnesi clinica (FattoriRischio, Patologie, AllergieIntolleranze,
      InterventiPregressi, EsamiDiagEsterni da ContattoPz; PresidiPaziente da Paziente —
      dominio coeso, una slice)
- [ ] Fatturazione contatti (Fatture — uno-a-molti da ContattoPz, lega a GlobalFattModule)
- [ ] Diagnostica per immagini / DICOM (EsamiDICOM da ContattoPz; EsamiDICOMEsterni e
      RefertiAmbMdw da Paziente)
- [ ] Microbiologia (EsamiMicrobiologici e Tamponi — uno-a-molti da Paziente)
- [ ] Anagrafica organizzativa completa (Dipendenti, PresidiOsp — oggi versioni minime,
      da espandere quando serve la gestione staff/reparti/presidi, vedi mappa moduli in
      CLAUDE.md)

## Fatto
- [x] Definire lo stack del progetto (FastAPI + PostgreSQL) e documentarlo in `CLAUDE.md` — 2026-07-10
- [x] Analisi del db legacy (`cocisdb_vuoto.sql`) con `/graphify` per informare il modello dati — 2026-07-10
- [x] Ricostruzione del grafo da codice sorgente legacy (`oldsystem/`, business object XPO) e mappa delle dipendenze tra moduli — 2026-07-13
<!-- - [x] Titolo slice — 2026-06-01, PR #1 -->

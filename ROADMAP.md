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
<!-- - [ ] Titolo slice — branch: `feat/...` -->

## Debito aperto (da chiudere appena c'è un Postgres raggiungibile)
- [ ] **Verifica su PostgreSQL reale mai eseguita.** Nessun PostgreSQL è stato raggiungibile
      nelle sessioni di sviluppo: `alembic upgrade head` non ha **mai** girato contro un DB
      reale. Mitigazioni in essere (non sostitutive): la coerenza migration↔modelli è
      verificata applicando la migration a uno SQLite usa-e-getta e diffandola con i
      metadati SQLAlchemy; la suite `pytest` **gira ed è verde su SQLite**
      (`TEST_DATABASE_URL="sqlite:///./test_tmp.db" uv run pytest`, vedi README). Restano
      scoperte le differenze specifiche di PostgreSQL (tipi, vincoli, JSONB futuro) e il
      percorso Alembic. Da fare prima di considerare davvero chiuse le slice mergiate.

## Backlog
- [ ] Modello Scheda Clinica polimorfica (Schederic→Schede, discriminatore + JSONB)
- [ ] Prenotazione Ambulatorio + Prestazione Ambulatoriale (percorso ambulatoriale, link
      bidirezionale tra i due)
- [ ] Rilevazioni (parametri vitali, esami di laboratorio) collegate al Ricovero
- [ ] Procedure previste / effettuate collegate al Ricovero (incl. la collection
      `ProcedurePreviste` su Prenotazione)
- [ ] SDO / SDO10 (scheda dimissione ospedaliera)
- [ ] Rinvii + MotiviRinvio (uno-a-molti da Prenotazione)
- [ ] Codifiche cliniche ICD9/ICD10 (GlobalClinModule): oggi `Diagnosi.icd9_cm_id` è un
      FK-placeholder Integer
- [ ] Contatti telefonici (Telefoni/TelefoniPz — uno-a-molti da ContattoPz)
- [ ] Parenti del paziente (uno-a-molti da Paziente)
- [ ] Anamnesi clinica (FattoriRischio, Patologie, AllergieIntolleranze,
      InterventiPregressi, EsamiDiagEsterni da ContattoPz; PresidiPaziente da Paziente —
      dominio coeso, una slice)
- [ ] Fatturazione contatti (Fatture — uno-a-molti da ContattoPz, lega a GlobalFattModule)
- [ ] Diagnostica per immagini / DICOM (EsamiDICOM da ContattoPz; EsamiDICOMEsterni e
      RefertiAmbMdw da Paziente)
- [ ] Microbiologia (EsamiMicrobiologici e Tamponi — uno-a-molti da Paziente)
- [ ] Reparti + Medici (anagrafica organizzativa/staff): `Reparto` è una tabella grande
      (~30 campi, letti/magazzino/terapia), `Medici` è un sottotipo di `Dipendente`
      (chiave condivisa). Oggi sono referenziati come FK-placeholder Integer da
      `Dipendente.reparto_predefinito_id` e `PresidioOsp.direttore_sanitario_id`/
      `responsabile_dipartimento_id`: modellandoli, quei placeholder diventano FK vere e
      si aggiungono le relazioni inverse (Dipendente↔Reparti, ecc.). Vedi mappa moduli in
      CLAUDE.md.

## Fatto
- [x] Definire lo stack del progetto (FastAPI + PostgreSQL) e documentarlo in `CLAUDE.md` — 2026-07-10
- [x] Analisi del db legacy (`cocisdb_vuoto.sql`) con `/graphify` per informare il modello dati — 2026-07-10
- [x] Ricostruzione del grafo da codice sorgente legacy (`oldsystem/`, business object XPO) e mappa delle dipendenze tra moduli — 2026-07-13
- [x] Anagrafica Paziente + ContattoPz (base polimorfica) + Ricovero (sottotipo) — prima slice
      MVP: scaffolding FastAPI/SQLAlchemy/Alembic, joined-table inheritance, campi legacy
      completi e campi calcolati come property/`computed_field` — 2026-07-13, PR #1
- [x] Completamento campi legacy XPO sulle tabelle anagrafiche: `Dipendente` e `PresidioOsp`
      completi, nuove lookup `Titolo`/`TipoDipendente`/`RapportoDipendenza`, gap minori
      colmati. `Reparti`/`Medici` restano FK-placeholder (vedi Backlog) — 2026-07-16, PR #2
- [x] Prenotazione + Prericovero (percorso ricovero): due nuovi sottotipi di `ContattoPz`,
      link reali `Ricovero→{Prenotazione,Prericovero}` e `Prericovero→Prenotazione` (i
      reverse erano `[NonPersistent]` nel legacy → relationship), 6 lookup nuove
      (`GradoUrgenza`, `ModalitaAccesso`, `Provenienza`, `Disciplina`, `Diagnosi`,
      `DisdettaPrenotazione`), router + 20 test verdi (prima esecuzione reale della suite,
      su SQLite). Scoperta: i 5 "sottotipi" legacy di Prenotazioni (Ord/DH/DayService/
      PreRic/PreRicDH) **non hanno tabella** (`MapInheritance.ParentTable`) → sono il campo
      `regime_ricovero`, non entità — 2026-07-16, PR #3

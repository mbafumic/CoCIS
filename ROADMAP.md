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
- [ ] Completamento campi legacy XPO sulle tabelle anagrafiche — branch:
      `feat/campi-mancanti-anagrafica`. Tutte le lookup ora hanno i campi persistenti
      del rispettivo oggetto XPO: `Dipendente` e `PresidioOsp` completati (non più
      minimi), aggiunte `Titolo`/`TipoDipendente`/`RapportoDipendenza`, colmati piccoli
      gap (`transcodifica`, `codice_altro_sistema`, ecc.) e campi calcolati (Nominativo).
      Fonte autoritativa = oggetto XPO C# (colonne solo-SQL come `SiglaRegione`, o
      pseudo-proprietà come `Prov`, non portate). `Reparti` e `Medici`, referenziati da
      `Dipendente`/`PresidioOsp`, sono FK-placeholder (Integer nullable) — vedi Backlog.
      Codici Gestclid (`Codpaz`/`Cod_dpaz`/`Codric`) restano esclusi come da decisione.
      Migration allineata (verificata vs metadati), ruff pulito, test verdi in collezione;
      manca la verifica end-to-end contro un Postgres reale.
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
<!-- - [x] Titolo slice — 2026-06-01, PR #1 -->

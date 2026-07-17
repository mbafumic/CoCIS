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

## Debito aperto
<!-- - [ ] Titolo — descrizione -->

## Debito chiuso
- [x] **Verifica su PostgreSQL reale** — 2026-07-17. `alembic upgrade head` eseguito con
      successo contro un'istanza reale (le 32 tabelle attese, nessuna in più/mancante,
      confrontate con `Base.metadata`). Verificati anche a mano: i 63 vincoli FK (incl. le
      self-FK `reparti.reparto_mag_id`/`medici.tutor_spec_id` e la corretta **assenza** di FK
      su `presidi_osp.direttore_sanitario_id`/`responsabile_dipartimento_id` — il ciclo va
      rotto lì, come nel legacy); un giro end-to-end via HTTP del percorso
      Paziente→Prenotazione→Prericovero→Ricovero; il polimorfismo `Dipendente`→`Medico` e la
      M:M `reparti_dipendenti` via SQLAlchemy diretto. Dati di verifica ripuliti a fine sessione
      (schema intatto, tabelle vuote). Nota operativa: il DB `cocisdb` su questo server condiviso
      apparteneva a un altro ruolo (`s_coscience`) — schema `public` senza `CREATE` per `cocis`
      finché non se n'è cambiata la proprietà (comportamento di default da PostgreSQL 15+).
      Bloccava **tutte** le slice precedenti (PR #1-#4): ora è sciolto per tutte in un colpo.
- [x] **`pytest` contro PostgreSQL reale** — 2026-07-17. Creato `cocisdb_test` (database
      separato da `cocisdb`, proprietà di `cocis` fin dalla creazione — nessun problema di
      permessi sullo schema `public`). **28/28 test verdi** contro l'istanza reale; il
      `drop_all` di fine sessione ripulisce correttamente `cocisdb_test` senza toccare lo
      schema migrato in `cocisdb`. La Definition of Done ("test verdi") è ora soddisfatta su
      Postgres, non solo su SQLite, per tutte le slice mergiate (PR #1-#4).

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
- [ ] Parenti del paziente (uno-a-molti da Paziente); oggi `Prericovero.parente_id` è un
      FK-placeholder Integer
- [ ] Gestione posti letto (Letti/Camere — uno-a-molti da Reparto)
- [ ] Anamnesi clinica (FattoriRischio, Patologie, AllergieIntolleranze,
      InterventiPregressi, EsamiDiagEsterni da ContattoPz; PresidiPaziente da Paziente —
      dominio coeso, una slice)
- [ ] Fatturazione contatti (Fatture — uno-a-molti da ContattoPz, lega a GlobalFattModule)
- [ ] Diagnostica per immagini / DICOM (EsamiDICOM da ContattoPz; EsamiDICOMEsterni e
      RefertiAmbMdw da Paziente)
- [ ] Microbiologia (EsamiMicrobiologici e Tamponi — uno-a-molti da Paziente)
- [ ] Specializzazioni (M:M con Dipendente, legata a `TipoDipendente`)

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
- [x] Reparti + Medici (anagrafica organizzativa/staff): `Reparto` (~30 campi, M:M con
      Dipendente, self-ref magazzino) e `Medico` come **sottotipo di `Dipendente`**
      (seconda gerarchia polimorfica del progetto, discriminatore `tipo_personale`).
      **Sciolti 8 dei 10 FK-placeholder** accumulati nelle slice precedenti; i 2 su
      `PresidioOsp` restano senza FK a DB di proposito (ciclo `presidi_osp→medici→
      dipendenti→presidi_osp`, come nel legacy) ma sono navigabili via relationship.
      Scoperta: `repartireparti_medicimedici` è una tabella morta (nessun oggetto XPO la
      dichiara) → non modellata — 2026-07-16, branch `feat/reparti-medici`

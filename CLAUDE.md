# CLAUDE.md — Convenzioni di progetto Coscience

Questo progetto nasce dal **template Coscience**. Per lavorare, lancia `/coscience` dal tuo
branch: ti dice cosa c'è da fare, pianifica e porta avanti la roadmap.

## Stack
**Backend: FastAPI + PostgreSQL** (SQLAlchemy + Alembic per modelli/migrazioni, pytest per i
test). Scelta confermata: CoCIS è la reingegnerizzazione di un gestionale ospedaliero legacy
(vedi sezione Dominio sotto), coerente con la preferenza di default di Coscience.

## Dominio & modello dati

CoCIS sostituisce un vecchio gestionale ospedaliero (MySQL/MariaDB + DevExpress XAF/XPO,
~750 tabelle) di cui esiste un dump vuoto (`cocisdb_vuoto.sql`) analizzato con `/graphify`
(risultati in `graphify-out/`, non versionato — rigenerabile con `graphify cocisdb_vuoto.sql`).

Struttura di dominio emersa dall'analisi del grafo (confermata dal dev):

```
Paziente (anagrafica)
  └─ ContattoPz (contatto/interazione — radice polimorfica, chiave condivisa OID)
        ├─ Ricovero ─┬─ N SchedaClinica (radice polimorfica Schederic→Schede, ~66 sottotipi:
        │            │   cartella infermieristica, cartella CEC, referti, scale di
        │            │   valutazione, consulenze...)
        │            ├─ N Rilevazioni (parametri vitali, esami di laboratorio)
        │            ├─ N ProcedurePreviste / ProcedureEffettuate
        │            └─ 1 SDO + 1 SDO10 (scheda dimissione ospedaliera, doppia codifica)
        ├─ Prericovero        (stessa struttura di Ricovero)
        ├─ PrenotazioneAmbulatorio
        └─ PrestazioneAmbulatoriale ─ 1 documento clinico (da Schede)
```

Decisioni di design per la riscrittura:
- **`ContattoPz` e `Schederic` sono basi polimorfiche** nel legacy (class-table inheritance
  DevExpress, PK condivisa). Nel nuovo modello: **non portare 1:1** le decine di sottotipi.
  Preferire un'unica entità con discriminatore di tipo (`tipo_scheda`, `tipo_contatto`) e un
  campo `JSONB` per gli attributi specifici del sottotipo, salvo che servano validazioni forti
  per-tipo (in quel caso, joined-table inheritance via SQLAlchemy).
- Le tabelle di sistema DevExpress (audit, permessi, metadata XPO — riconoscibili dai prefissi
  `devexpress_*`, `persistent*`, `xpo*`, `security*`) sono infrastruttura ORM legacy: **non
  vanno migrate**. Permessi e audit si reimplementano nativamente sullo stack scelto.
- `Ricovero` nel legacy è una "god table" da 84 colonne: nel nuovo modello va scomposto per
  bounded context (clinico, amministrativo/DRG, posti letto) sfruttando le ~49 tabelle figlie
  già esistenti come guida ai confini.

## Convenzioni (codebase autodichiarativa)
- Nomi espliciti; un modulo = una responsabilità con confini netti.
- Ogni nuova funzionalità = una **slice verticale** piccola e rilasciabile, con i suoi test.
- Aggiorna la documentazione nello stesso commit della modifica.
- Chi arriva dopo (umano o agente) deve capire il progetto leggendolo, non chiedendo.

## Definition of Done (una slice è "fatta" quando)
1. Codice scritto e autodichiarativo.
2. Test verdi e controlli di qualità puliti (gli strumenti dipendono dallo stack scelto).
3. `ROADMAP.md` e documentazione toccata aggiornati.
4. PR aperta (per la review asincrona su GitHub).

## Flusso di lavoro
- Una slice per volta, dal Backlog di `ROADMAP.md`.
- Branch corti (`feat/...`, `fix/...`), PR piccole e a vita breve.
- Non restare bloccato: se aspetti una review, prendi la prossima slice sbloccabile.

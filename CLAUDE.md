# CLAUDE.md — Convenzioni di progetto Coscience

Questo progetto nasce dal **template Coscience**. Per lavorare, lancia `/coscience` dal tuo
branch: ti dice cosa c'è da fare, pianifica e porta avanti la roadmap.

## Stack
**Backend: FastAPI + PostgreSQL** (SQLAlchemy + Alembic per modelli/migrazioni, pytest per i
test). Scelta confermata: CoCIS è la reingegnerizzazione di un gestionale ospedaliero legacy
(vedi sezione Dominio sotto), coerente con la preferenza di default di Coscience.

## Dominio & modello dati

CoCIS sostituisce un vecchio gestionale ospedaliero (MySQL/MariaDB + DevExpress XAF/XPO
19.2, ~750 tabelle). Due fonti analizzate con `/graphify` (risultati in `graphify-out/`,
versionato — rigenerabile con `/graphify oldsystem`):
- `cocisdb_vuoto.sql` — dump vuoto dello schema DB legacy (tracciato in repo, riferimento
  storico).
- `oldsystem/` — codice sorgente C# reale delle business object XPO (`AccettazioneModule`,
  `GlobalModule`, `GlobalClinModule`, `GlobalFattModule`; **non tracciato in git**, vedi
  `.gitignore`). È la fonte più affidabile: il grafo attuale in `graphify-out/` è ricostruito
  da qui, scartando le tabelle SQL non referenziate da nessuna business object nel codice.

Struttura di dominio emersa dall'analisi (confermata dal dev, doppiamente validata: sia dalle
FK del DB sia dai riferimenti di tipo nel codice C#):

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

### Mappa delle dipendenze tra moduli legacy (guida ai bounded context)

Analisi dei riferimenti di tipo cross-modulo nel codice C# (`graphify path`/`query` su
`graphify-out/`):

```
AccettazioneModule ──192 rif.──> GlobalModule       (anagrafica organizzativa: Dipendenti,
                                                      Reparti, Medici, Letti, PresidiOsp)
AccettazioneModule ──34 rif.───> GlobalClinModule    (codifica clinica: ICD9/ICD10, DRG,
                                                      Procedure, Diagnosi)
AccettazioneModule ──7 rif.────> GlobalFattModule    (fatturazione: CodiciIVA, DRG_DX_PX,
                                                      ErroriGrouper)
GlobalClinModule ───2 rif.────> GlobalFattModule    (DRG → RegioniDRG/TariffariDRG)
```

**Nessun riferimento nel senso opposto**: i tre moduli `Global*` non dipendono mai da
`AccettazioneModule`. È un'architettura a livelli pulita nel legacy — i moduli `Global*` sono
dati di riferimento/fondazione, `AccettazioneModule` è il layer applicativo/paziente che li
consuma. Guida per i confini dei moduli nel nuovo backend:
- Un modulo "anagrafica organizzativa" (staff, reparti, presidi — da `GlobalModule`).
- Un modulo "codifiche cliniche" (ICD9/ICD10, DRG, procedure — da `GlobalClinModule`).
- Un modulo "fatturazione" (IVA, DRG-fatturazione — da `GlobalFattModule`).
- Il core clinico/paziente (da `AccettazioneModule`) dipende dai tre sopra, mai viceversa.

God nodes reali del codice (esclusi tipi primitivi/enum/namespace): `Ricoveri`, `Dipendenti`,
`Rulli` (lookup enumerativa condivisa), `SchedeRic` (= `schederic` nel DB, confermata base
polimorfica anche nel codice), `ContattiPz`, `Reparti`, `Medici`, `ProcedureEffettuate`,
`Prericoveri`, `Prenotazioni`, `Pazienti` — stesso set di entità centrali trovato dall'analisi
del DB, doppia conferma del modello di dominio sopra.

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

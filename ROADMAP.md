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

## Backlog
- [ ] Anagrafica Paziente + ContattoPz (base) + Ricovero (sottotipo) — prima slice MVP
- [ ] Modello Scheda Clinica polimorfica (Schederic→Schede, discriminatore + JSONB)
- [ ] Prericovero, Prenotazione Ambulatorio, Prestazione Ambulatoriale (altri sottotipi di ContattoPz)
- [ ] Rilevazioni (parametri vitali, esami di laboratorio) collegate al Ricovero
- [ ] Procedure previste / effettuate collegate al Ricovero
- [ ] SDO / SDO10 (scheda dimissione ospedaliera)

## Fatto
- [x] Definire lo stack del progetto (FastAPI + PostgreSQL) e documentarlo in `CLAUDE.md` — 2026-07-10
- [x] Analisi del db legacy (`cocisdb_vuoto.sql`) con `/graphify` per informare il modello dati — 2026-07-10
- [x] Ricostruzione del grafo da codice sorgente legacy (`oldsystem/`, business object XPO) e mappa delle dipendenze tra moduli — 2026-07-13
<!-- - [x] Titolo slice — 2026-06-01, PR #1 -->

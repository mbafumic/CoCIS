# CLAUDE.md — Convenzioni di progetto Coscience

Questo progetto nasce dal **template Coscience**. Per lavorare, lancia `/coscience` dal tuo
branch: ti dice cosa c'è da fare, pianifica e porta avanti la roadmap.

## Stack
Le scelte tecnologiche sono **libere per progetto**: scegli ciò che serve al dominio.
Coscience ha una **preferenza** (non un obbligo) per **FastAPI + PostgreSQL** sul backend:
adottala se non ci sono motivi per fare diversamente, altrimenti documenta qui la scelta.

> Dichiara in questa sezione lo stack effettivo del progetto appena lo definisci
> (linguaggio, framework, DB, strumenti di test e qualità). È la prima slice del Backlog.

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

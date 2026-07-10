---
name: coscience
description: Loop di sviluppo Coscience. Invocala da qualsiasi branch per sapere cosa c'è da fare (legge ROADMAP.md), pianificare la prossima implementazione e portarla avanti aggiornando roadmap e documentazione. Usala all'inizio di ogni sessione di lavoro su un progetto Coscience.
---

# Coscience — loop di sviluppo

Sei l'assistente di sviluppo della startup Coscience. Quando questa skill è attiva guidi il
dev attraverso un loop unico e semplice: **cosa c'è da fare → pianifica → implementa →
aggiorna roadmap e doc**. Funziona da qualsiasi branch, perché lo stato del progetto vive in
`ROADMAP.md` versionato nel repo.

## Principi (non negoziabili)
- **Incrementale, MVP → produzione.** Una fetta verticale funzionante alla volta. Mai big-bang.
- **Codebase autodichiarativa.** Nomi espliciti, moduli con confini netti, doc che dichiara
  l'intento. Chi arriva dopo capisce leggendo, non chiedendo.
- **La conoscenza vive nel repo.** Ogni avanzamento aggiorna `ROADMAP.md` e la doc toccata.
- **Non bloccarsi.** Se la tua PR è in review, prendi un altro item sbloccabile dal Backlog.

Le scelte tecnologiche sono libere per progetto (vedi `CLAUDE.md`); Coscience ha solo una
*preferenza* per FastAPI + PostgreSQL sul backend, non un obbligo. Adatta i comandi allo
stack effettivo del progetto.

## Passi

### 1. Leggi lo stato
- Leggi `ROADMAP.md` (sezioni *In corso*, *Backlog*, *Fatto*).
- Controlla git: branch corrente e modifiche non committate
  (`git branch --show-current`, `git status --short`).
- Leggi `CLAUDE.md` per stack, convenzioni e Definition of Done.

### 2. Di' "cosa c'è da fare"
- Riassumi in modo conciso cosa è *In corso* (con i relativi branch) e i primi item del
  *Backlog*.
- Se il branch corrente corrisponde a un item *In corso*, proponi di proseguire quello.
- Altrimenti proponi il primo item del *Backlog* che è sbloccabile (nessuna dipendenza
  aperta). Chiedi conferma al dev su cosa lavorare.

### 3. Pianifica
- Per l'item scelto **entra in plan mode** ed elabora un piano: fetta verticale minima, file
  da toccare, come testarla. Tieni il piano piccolo (un MVP della slice).
- Fai approvare il piano prima di implementare.

### 4. Implementa
- Esegui il piano sul branch corrente. Scrivi codice autodichiarativo e i relativi test,
  seguendo le convenzioni di `CLAUDE.md`.
- Verifica con gli strumenti dello stack scelto (test e controlli di qualità). Usa `/verify`
  o `/run` per provare l'app dal vivo se serve.
- Quando opportuno fai una pre-review con `/code-review`.

### 5. Porta avanti la roadmap
- Aggiorna `ROADMAP.md`: sposta l'item completato in *Fatto* (con data e, se c'è, PR#),
  oppure aggiornane lo stato in *In corso* annotando il branch.
- Aggiorna la documentazione toccata (`CLAUDE.md`, `README.md`, docstring) così che resti
  autodichiarativa.
- Verifica la **Definition of Done** in `CLAUDE.md` prima di considerare chiusa la slice.
- Opzionale: commit + PR (puoi usare la skill `commit-commands`) per la review asincrona su
  GitHub; poi torna al passo 2 per la prossima slice senza restare bloccato.

## Note
- Una sola slice per volta. Se emergono altre idee, aggiungile al *Backlog* di `ROADMAP.md`
  invece di allargare lo scope corrente.
- Non duplicare strumenti: usa i built-in (`/code-review`, `/simplify`, `/security-review`,
  `/verify`, `/run`) invece di reimplementarli.

# Sviluppare Codice con Coscience

Guida operativa per una startup Claude AI-native. Procedura interna: tienila nel repo e
migliorala in modo incrementale, esattamente come il codice che produciamo.

## 0. Filosofia

Coscience non "usa l'AI per scrivere codice": mette a sistema la produzione software attorno
a Claude Code. Tre principi guidano tutto:

- **Incrementale, MVP → produzione.** Si parte sempre da una fetta verticale funzionante
  (MVP), poi si consolida verso software professionale (test, osservabilità, sicurezza,
  documentazione). Mai big-bang.
- **Codebase autodichiarativa, chiara, modulare.** Il codice spiega sé stesso: nomi
  espliciti, moduli con confini netti, `README` e `CLAUDE.md` che dichiarano intento e
  convenzioni. Un nuovo arrivato (umano o agente) capisce il progetto leggendolo.
- **La conoscenza del team vive nel repo, non nelle teste.** Convenzioni e flusso si
  scrivono una volta (qui e in `CLAUDE.md`) e scalano a tutto il team.

## 1. Setup (una tantum, per ogni dev)

1. Crea il progetto dal template (vedi `README.md`) e clonalo.
2. In Claude Code aggiungi il marketplace ufficiale e installa l'essenziale:
   - `/plugin marketplace add anthropics/claude-plugins-official`
   - `/plugin install skill-creator` — per creare/mantenere le skill Coscience
   - *(opz.)* `/plugin install commit-commands` — commit/push/PR puliti
   - *(opz.)* il language server del tuo stack (es. `pyright-lsp` per Python)
3. Autenticati a GitHub: `gh auth login`.

> Review, semplificazione e analisi di sicurezza sono **già built-in**: `/code-review`,
> `/simplify`, `/security-review`. Non servono plugin per queste.

## 2. Il ciclo di lavoro: `/coscience`

Da qualunque branch, lancia **`/coscience`**. La skill esegue un loop unico:

1. **Cosa c'è da fare** — legge `ROADMAP.md` e lo stato git, ti dice cosa è in corso e cosa
   è sbloccabile nel Backlog.
2. **Pianifica** — entra in plan mode per la slice scelta e fa approvare un piano piccolo.
3. **Implementa** — scrive codice autodichiarativo e test sul branch corrente.
4. **Porta avanti la roadmap** — aggiorna `ROADMAP.md` e la documentazione, poi (opzionale)
   apre la PR.

## 3. Branch, PR e timeline condivisa

- Branch corti e tematici: `feat/...`, `fix/...`. Una slice = un branch = una PR piccola.
- `ROADMAP.md` è la **timeline condivisa**: versionata nel repo, la vedono tutti da ogni
  branch. Stati: *In corso* / *Backlog* / *Fatto*.
- **Review asincrona, non bloccante.** Apri la PR e continua: la review avviene su GitHub
  quando un collega è libero. Mentre aspetti, torna su `/coscience` e prendi la prossima
  slice sbloccabile dal Backlog. Nessuno resta fermo ad aspettare.

## 4. Definition of Done

Una slice è "fatta" quando: codice autodichiarativo + test verdi e qualità pulita + `ROADMAP`
e doc aggiornati + PR aperta. (Vedi `CLAUDE.md`.)

## 5. Far evolvere il metodo

Il template è esso stesso software incrementale: se una convenzione non funziona, aprila come
slice, migliorala e versiona il cambiamento. Le raffinazioni (skill aggiuntive, automazioni,
subagent specializzati) arrivano dopo, quando il bisogno è reale.

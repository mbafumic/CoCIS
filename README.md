# Coscience Template

Template per progetti software **Claude AI-native** della startup Coscience. Ogni nuovo
progetto parte da qui ed eredita un flusso di lavoro semplice e già pronto.

## Cosa contiene

| File | A cosa serve |
|------|--------------|
| `.claude/skills/coscience/` | La skill **`/coscience`**: il loop di sviluppo (cosa fare → pianifica → implementa → aggiorna roadmap). |
| `.claude/settings.json` | Permessi condivisi del progetto (versionati). |
| `ROADMAP.md` | La tabella di marcia condivisa: unica fonte di verità su cosa c'è da fare. |
| `CLAUDE.md` | Convenzioni di progetto e Definition of Done. |
| `CONTRIBUTING.md` | La guida "Sviluppare Codice con Coscience". |

Le scelte tecnologiche sono **libere per progetto**; Coscience preferisce (non impone)
**FastAPI + PostgreSQL** sul backend.

## Creare un nuovo progetto

1. Su GitHub: **"Use this template"** → crea il nuovo repo.
2. Clonalo e apri Claude Code nella cartella.
3. Segui il **Setup** in [CONTRIBUTING.md](CONTRIBUTING.md).
4. Lancia **`/coscience`** dal tuo branch e parti dalla prima slice del Backlog.

## Il loop in una riga

> Da qualsiasi branch lancia `/coscience`: ti dice cosa c'è da fare, pianifica la prossima
> slice e la porta avanti aggiornando roadmap e documentazione.

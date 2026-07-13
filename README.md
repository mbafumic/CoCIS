# CoCIS

Reingegnerizzazione di un gestionale ospedaliero legacy. Backend FastAPI + PostgreSQL — vedi
`CLAUDE.md` per stack, dominio e convenzioni.

## Avvio locale

Richiede un'istanza PostgreSQL raggiungibile (locale o remota) e [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync                                  # installa le dipendenze (crea .venv)
cp .env.example .env                     # poi modifica DATABASE_URL se necessario
createdb cocis                           # database di sviluppo
createdb cocis_test                      # database usato dai test (o esporta TEST_DATABASE_URL)
uv run alembic upgrade head              # applica le migration
uv run uvicorn app.main:app --reload     # avvia l'API su http://localhost:8000
```

Verifica: `uv run pytest` (test) e `uv run ruff check . && uv run ruff format --check .`
(qualità).

---

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

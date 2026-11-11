# Revisão: GitHub Actions + Docker

API de tarefas em Flask. Sem a variável `DATABASE_URL`, guarda as tarefas em
memória; com ela, usa um PostgreSQL.

| Método | Rota | Descrição |
|---|---|---|
| GET | `/saude` | `{"status": "ok"}` |
| GET | `/tarefas` | lista as tarefas |
| POST | `/tarefas` | cria uma tarefa — corpo JSON `{"titulo": "..."}` |

Ao longo da revisão você vai criar:

- `.github/workflows/ola.yml` e `.github/workflows/ci.yml`
- `Dockerfile` e `.dockerignore`
- `compose.yaml` e `compose.prod.yaml`

Testes (no CI, ou localmente se tiver Python): `pip install -r requirements-dev.txt && pytest -v`

Exemplos com curl:

```bash
curl http://localhost:5000/saude
curl -X POST -H "Content-Type: application/json" \
  -d '{"titulo": "Revisar Docker"}' http://localhost:5000/tarefas
curl http://localhost:5000/tarefas
```

PowerShell:

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5000/tarefas `
  -ContentType "application/json" -Body '{"titulo": "Revisar Docker"}'
```

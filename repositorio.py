"""Onde as tarefas são guardadas: em memória (padrão) ou no PostgreSQL."""

import os


class RepositorioMemoria:
    def __init__(self):
        self._tarefas = []

    def listar(self):
        return list(self._tarefas)

    def criar(self, titulo):
        tarefa = {"id": len(self._tarefas) + 1, "titulo": titulo, "feita": False}
        self._tarefas.append(tarefa)
        return tarefa


class RepositorioPostgres:
    def __init__(self, dsn):
        self._dsn = dsn
        with self._conectar() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tarefas ("
                " id SERIAL PRIMARY KEY, titulo TEXT NOT NULL, feita BOOLEAN DEFAULT false)"
            )

    def _conectar(self):
        import psycopg

        return psycopg.connect(self._dsn, autocommit=True)

    def listar(self):
        with self._conectar() as conn:
            linhas = conn.execute(
                "SELECT id, titulo, feita FROM tarefas ORDER BY id"
            ).fetchall()
        return [{"id": i, "titulo": t, "feita": f} for i, t, f in linhas]

    def criar(self, titulo):
        with self._conectar() as conn:
            (novo_id,) = conn.execute(
                "INSERT INTO tarefas (titulo) VALUES (%s) RETURNING id", (titulo,)
            ).fetchone()
        return {"id": novo_id, "titulo": titulo, "feita": False}


def criar_repositorio():
    """Usa o PostgreSQL se DATABASE_URL estiver definida; senão, memória."""
    dsn = os.environ.get("DATABASE_URL")
    return RepositorioPostgres(dsn) if dsn else RepositorioMemoria()

from flask import Flask, request

from repositorio import criar_repositorio


def criar_app(repo=None):
    app = Flask(__name__)
    app.json.ensure_ascii = False
    repo = repo or criar_repositorio()

    @app.get("/saude")
    def saude():
        return {"status": "ok"}

    @app.get("/tarefas")
    def listar():
        return repo.listar()

    @app.post("/tarefas")
    def criar():
        dados = request.get_json(silent=True) or {}
        titulo = str(dados.get("titulo", "")).strip()
        if not titulo:
            return {"erro": "informe um título"}, 400
        return repo.criar(titulo), 201

    return app


if __name__ == "__main__":
    criar_app().run(host="0.0.0.0", port=5000)

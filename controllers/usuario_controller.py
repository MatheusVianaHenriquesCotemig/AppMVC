from flask import jsonify, request
from services.usuario_service import UsuarioServices

class UsuarioController():
    @staticmethod
    def index():
        lista = UsuarioServices.lista_usuarios()

        usuarios = []

        for usuario in lista:
            usuarios.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "setor": usuario.setor
            })
        return jsonify(usuarios)
    @staticmethod
    def cadastrar():
        dados = request.json
        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400
        if dados.get("nome") is None:
            return jsonify({"erro": "Nome inválido"}), 400
        if dados.get("email") is None:
            return jsonify({"erro": "Email obrigatório"}), 400
        existe = UsuarioServices.pesquisa_email(dados.get("email"))

        if existe:
            return jsonify({"erro": "Email já cadastrado"}), 400
        
        usuario = UsuarioServices.cadastra_usuario(
            nome = dados["nome"],
            email = dados["email"],
            setor = dados["setor"]
        )

        return jsonify({
        "mensagem": "Usuário cadastrado",
        "id": usuario.id
        })
    @staticmethod
    def atualizar():
        dados = request.json
        id_usuario = dados["id"]

        kwargs = {
            "nome": dados["nome"],
            "email": dados["email"],
            "setor": dados["setor"]
        }

        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400
        usuario_atualizado = UsuarioServices.atualiza_usuario(
            id_usuario,kwargs
        )
        return jsonify({
                "mensagem": "Usuário atualizado",
                "id": usuario_atualizado.id
                })
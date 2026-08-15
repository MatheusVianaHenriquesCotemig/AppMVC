from flask import jsonify, request
from services.chamado_service import ChamadoServices
from services.usuario_service import UsuarioServices

class ChamadoController():
    @staticmethod
    def index():
        
            lista = ChamadoServices.lista_chamados()
    
            chamados = []
    
            for chamado in lista:
                chamados.append({
                    "titulo": chamado.titulo,
                    "descricao": chamado.descricao,
                    "prioridade": chamado.prioridade,
                    "status": chamado.status,
                    "tecnico": chamado.tecnico,
                    "data_abertura": chamado.data_abertura,
                    "usuario_id": chamado.usuario_id
                })
            return jsonify(chamados)
    @staticmethod
    def cadastrar():
        dados = request.json
        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400
            
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        
        if len(titulo) < 5:
            return jsonify({"erro": "Título inválido"}), 400
        if len(descricao) < 10:
            return jsonify({"erro": "Descrição inválida"}), 400
        if dados.get("usuario_id") is None:
            return jsonify({"erro": "Chamado inválido"}), 400
        if dados.get("prioridade") != "Baixa":
            if dados.get("prioridade") != "Média":
                if dados.get("prioridade") != "Alta":
                    return jsonify({"erro": "Prioridade inválida"}), 400
        
        chamado_numero = ChamadoServices.valida_chamado(dados.get("usuario_id"))
        if chamado_numero > 5:
            return jsonify({"erro": "Usuário indisponível"}), 400
        
        if dados.get("status") != "Aberto":
            if dados.get("status") != "Em atendimento":
                if dados.get("status") != "Encerrado":
                    return jsonify({"erro": "Status inválido"}), 400
        
        chamado = ChamadoServices.cadastra_chamado(
            titulo = dados["titulo"],
            descricao = dados["descricao"],
            prioridade = dados["prioridade"],
            status = dados["status"],
            tecnico = dados["tecnico"],
            data_abertura = dados["data_abertura"],
            usuario_id = dados["usuario_id"]
         )
    
        return jsonify({         
           "mensagem": "Chamado cadastrado",
           "id": chamado.id
          })
    @staticmethod
    def atualizar():
            dados = request.json
            id_chamado= dados["id"]
    
            kwargs = {
                "titulo": dados["titulo"],
                "descricao": dados["descricao"],
                "prioridade": dados["prioridade"],
                "status": dados["status"],
                "tecnico": dados["tecnico"],
            }
    
            if not dados:
                return jsonify({"erro": "JSON inválido"}), 400
            chamado_atualizado = ChamadoServices.atualiza_chamado(
                id_chamado,kwargs
            )
            return jsonify({
                    "mensagem": "Chamado atualizado",
                    "id": chamado_atualizado.id
                    })
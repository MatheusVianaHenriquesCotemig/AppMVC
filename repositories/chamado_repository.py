from models.chamado import Chamado
from database import db

class ChamadoRepository():
    @staticmethod
    def consulta_listar():
        resultado = Chamado.query.all()
        return resultado
    @staticmethod
    def consulta_quantidade_usuario(usuario_id):
        resultado = Chamado.query.filter(
            Chamado.usuario_id == usuario_id,
            Chamado.status.in_(["Aberto", "Em atendimento"])
        ).count()

        return resultado
    @staticmethod
    def cadastrar_chamado(dados):
        novo_chamado = Chamado(**dados)
        db.session.add(novo_chamado)
        db.session.commit
        return novo_chamado
    @staticmethod
    def atualiza_chamado(id_chamado, dados):
            chamado = Chamado.query.get(id_chamado)
            if not chamado:
                return None
            
            if 'titulo' in dados:
                chamado.titulo = dados['titulo']
            if 'descricao' in dados:
                chamado.descricao = dados['descricao']
            if 'prioridade' in dados:
                chamado.prioridade = dados['prioridade']
            if 'status' in dados:
                chamado.status = dados['status']
            if 'tecnico' in dados:
                chamado.tecnico = dados['tecnico']
            db.session.commit()
            return chamado
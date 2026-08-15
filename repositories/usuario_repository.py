from models.usuario import Usuario
from database import db

class UsuarioRepository():
    @staticmethod
    def consulta_listar():
        resultado = Usuario.query.all()
        return resultado
    @staticmethod
    def cadastra_usuario(dados):
        novo_usuario = Usuario(**dados)
        db.session.add(novo_usuario)
        db.session.commit
        return novo_usuario
    @staticmethod
    def atualiza_usuario(id_usuario, dados):
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return None
        
        if 'nome' in dados:
            usuario.nome = dados['nome']
        if 'email' in dados:
            usuario.email = dados['email']
        if 'setor' in dados:
            usuario.setor = dados['setor']

        db.session.commit()
        return usuario
    @staticmethod
    def consulta_email(email):
        return Usuario.query.filter_by(Usuario.email == email).first()
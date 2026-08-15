from repositories.usuario_repository import UsuarioRepository

class UsuarioServices():
    @staticmethod
    def lista_usuarios():
        usuarios = UsuarioRepository.consulta_listar()
        return usuarios
    @staticmethod
    def cadastra_usuario(**kwargs):
        usuario = UsuarioRepository.cadastra_usuario(kwargs)
        return usuario
    @staticmethod
    def atualiza_usuario(id,**kwargs):
        usuario_atualizado = UsuarioRepository.atualiza_usuario(id,kwargs)
        return usuario_atualizado
    @staticmethod
    def pesquisa_email(email):
        return UsuarioRepository.consulta_email(email)
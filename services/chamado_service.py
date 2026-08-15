from repositories.chamado_repository import ChamadoRepository

class ChamadoServices():
    @staticmethod
    def lista_chamados():
        chamados = ChamadoRepository.consulta_listar()
        return chamados
    @staticmethod
    def valida_chamado(usuario_id):
        chamado = ChamadoRepository.consulta_quantidade_usuario(usuario_id)
        return chamado
    @staticmethod
    def cadastra_chamado(**kwargs):
        chamado = ChamadoRepository.cadastrar_chamado(kwargs)
        return chamado
    @staticmethod
    def atualiza_chamado(id,**kwargs):
            chamado_atualizado = ChamadoRepository.atualiza_chamado(id,kwargs)
            return chamado_atualizado
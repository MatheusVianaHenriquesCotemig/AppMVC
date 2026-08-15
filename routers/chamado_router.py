from flask import Blueprint
from controllers.chamado_controller import ChamadoController

chamado_bp = Blueprint('chamados', __name__)


chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.index , methods=['GET'])
chamado_bp.add_url_rule('/chamados/', view_func=ChamadoController.cadastrar , methods=['POST'])
chamado_bp.add_url_rule('/usuarios', view_func=ChamadoController.atualizar , methods=['PUT'])
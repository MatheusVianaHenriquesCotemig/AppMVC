from flask import Blueprint
from controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuarios', __name__)

usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.index , methods=['GET'])
usuario_bp.add_url_rule('/usuarios/', view_func=UsuarioController.cadastrar , methods=['POST'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.atualizar , methods=['PUT'])

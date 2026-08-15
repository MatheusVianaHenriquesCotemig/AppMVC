from database import db
from datetime import datetime

class Chamado(db.Model):
    __tablename__ = 'chamados'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255))
    prioridade = db.Column(db.String(5))
    status = db.Column(db.String(120), default="aberto")
    tecnico = db.Column(db.String(120))
    data_abertura = db.Column(db.Datetime(timezone=True))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuarios
from src.infra.sqlalchemy.models.models import Usuario


class RepositorioUsuario():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: Usuarios):
        usuario_bd = Usuario(nome=usuario.nome, senha=usuario.senha, telefone=usuario.telefone)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listar(self):
        usuarios = self.session.execute(select(Usuario)).scalars().all()
        return usuarios

    def obter(self, user_id = int):
        statement = select(Usuario).where(Usuario.id == user_id)
        usuarios = self.session.execute(statement).one()
        return usuarios

    def remover():
        pass
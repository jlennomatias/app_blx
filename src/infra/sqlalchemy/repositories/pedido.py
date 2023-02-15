from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacao=pedido.observacao,
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        pedidos = self.session.query(models.Pedido).all()
        return pedidos
    
    def listar_id(self, id):
        listar_pedido = select(models.Pedido).where(models.Pedido.id == id)
        listar_pedido = self.session.execute(listar_pedido).first()
        return listar_pedido

    def editar(self, id_pedido: int, pedido: schemas.Pedido):
        update_pedido = update(models.Pedido).where(models.Pedido.id == id_pedido).values(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacao=pedido.observacao,
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id
        )
        self.session.execute(update_pedido)
        self.session.commit()

    def remover(self, id):
        delete_pedido = delete(models.Pedido).where(models.Pedido.id == id)
        self.session.execute(delete_pedido)
        self.session.commit()
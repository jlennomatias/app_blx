from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: schemas.Produtos):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponibilidade=produto.disponibilidade,
            tamanhos=produto.tamanhos,
            usuario_id=produto.usuario_id
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos
    
    def listar_id(self, id):
        listar_produto = select(models.Produto).where(models.Produto.id == id)
        listar_produto = self.session.execute(listar_produto).first()
        return listar_produto

    def editar(self, id_produto: int, produto: schemas.Produtos):
        update_produto = update(models.Produto).where(models.Produto.id == id_produto).values(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponibilidade=produto.disponibilidade,
            tamanhos=produto.tamanhos
        )
        self.session.execute(update_produto)
        self.session.commit()

    def remover(self, id):
        delete_produto = delete(models.Produto).where(models.Produto.id == id)
        self.session.execute(delete_produto)
        self.session.commit()
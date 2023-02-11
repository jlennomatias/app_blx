from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Produtos, ProdutoResponse
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto
from typing import List


router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoResponse)
def criar_produtos(produto: Produtos, session: Session = Depends(get_db)):
    produto_Criado = RepositorioProduto(session).criar(produto)
    return produto_Criado


@router.get('/produtos', response_model=List[Produtos])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.put('/produtos/{id_produto}', response_model=Produtos)
def atualizar_produtos(id_produto: int, produto: Produtos, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id_produto, produto)
    return produto

@router.delete('/produtos/{id_produto}')
def delete_produtos(id_produto: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id_produto)
    return {"msg": "produto removido"}
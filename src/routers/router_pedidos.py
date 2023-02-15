from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido, PedidoSimples
from src.infra.sqlalchemy.repositories.pedido import RepositorioPedido
from typing import List


router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=PedidoSimples)
def criar_pedido(pedido: PedidoSimples, session: Session = Depends(get_db)):
    produto_Criado = RepositorioPedido(session).criar(pedido)
    return produto_Criado

@router.get('/pedidos', response_model=List[Pedido])
def listar_pedidos(session: Session = Depends(get_db)):
    produtos = RepositorioPedido(session).listar()
    return produtos

@router.get('/pedidos/{id_pedido}')
def delete_pedidos(id_pedido: int, session: Session = Depends(get_db)):
    produto = RepositorioPedido(session).listar_id(id_pedido)
    if not produto:
        raise HTTPException(
            status_code=404, detail=f"Não existe um pedidos com o id={id_pedido}"
        )
    return produto

@router.put('/pedidos/{id_pedido}', response_model=Pedido)
def atualizar_pedidos(id_pedido: int, pedido: Pedido, session: Session = Depends(get_db)):
    RepositorioPedido(session).editar(id_pedido, pedido)
    return pedido

@router.delete('/pedidos/{id_pedido}')
def delete_pedidos(id_pedido: int, session: Session = Depends(get_db)):
    RepositorioPedido(session).remover(id_pedido)
    return {"msg": "pedidos removido"}
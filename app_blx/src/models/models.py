from pydantic import BaseModel
from typing import Optional, List

class Usuarios(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produtos]
    minhas_vendas: List[Pedidos]
    meus_pedidos: List[Pedidos]

class Produtos(BaseModel):
    id: Optional[str] = None
    usuario: Usuarios
    nome: str
    detalhes: str
    preco: float
    disponibilidade: bool = False

class Pedidos(BaseModel):
    id: Optional[str] = None
    usuario: Usuarios
    produto: Produtos
    quantidade: int
    entrega: bool = False
    local: str
    observacoes: Optional[str] = "Sem observações"
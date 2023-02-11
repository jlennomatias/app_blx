from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponibilidade: bool

    class Config:
        orm_mode = True

class Usuarios(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True

class Produtos(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponibilidade: bool = False
    tamanhos: str = None
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

class ProdutoResponse(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponibilidade: bool = False
    tamanhos: str
    usuario_id: Optional[int]

    class Config:
        orm_mode = True

class Pedidos(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    local: str
    observacoes: Optional[str] = "Sem observações"
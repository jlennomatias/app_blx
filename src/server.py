from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produtos, ProdutoResponse, Usuarios
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario

criar_db()

app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoResponse)
def criar_produtos(produto: Produtos, session: Session = Depends(get_db)):
    produto_Criado = RepositorioProduto(session).criar(produto)
    return produto_Criado


@app.get('/produtos', response_model=List[Produtos])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@app.put('/produtos/{id_produto}', response_model=Produtos)
def atualizar_produtos(id_produto: int, produto: Produtos, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id_produto, produto)
    return produto

@app.delete('/produtos/{id_produto}')
def delete_produtos(id_produto: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id_produto)
    return {"msg": "produto removido"}

@app.post('/usuarios')
def criar_usuarios(usuario: Usuarios, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuarios])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
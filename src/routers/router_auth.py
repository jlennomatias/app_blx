from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuarios, UsuarioSimples, Login, LoginSucesso
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def criar_usuarios(usuario: Usuarios, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(session).obter_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuario para este telefone")
    print(f"gerando o hash de {usuario.senha}")
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[Usuarios])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

@router.post('/token', response_model=LoginSucesso)
def login(login_data: Login, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Telefone incorreto")
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="senha incorreto")
    # Gerar token JWT
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return LoginSucesso(usuario=usuario, access_token=token)

@router.get('/me', response_model=UsuarioSimples)
def me(usuario: Usuarios = Depends(obter_usuario_logado)):
    return usuario
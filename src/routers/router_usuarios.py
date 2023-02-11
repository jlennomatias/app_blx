from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuarios
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario



router = APIRouter()

@router.post('/usuarios')
def criar_usuarios(usuario: Usuarios, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[Usuarios])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
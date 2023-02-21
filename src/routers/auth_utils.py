from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def obter_usuario_logado(session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        telefone = token_provider.verificar_access_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token invalido')
    if not telefone:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido'
        )

    usuario = RepositorioUsuario(session).obter_telefone(telefone)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido'
        )
    return usuario
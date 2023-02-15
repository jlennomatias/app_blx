from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_produtos, router_usuarios, router_pedidos
 

app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router_produtos.router)

app.include_router(router_usuarios.router)

app.include_router(router_pedidos.router)


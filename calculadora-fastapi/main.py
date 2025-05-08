from fastapi import FastAPI
from views.calculator_view import router as calculator_router

app = FastAPI()

# Incluindo as rotas da calculadora
app.include_router(calculator_router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Calculadora!"}
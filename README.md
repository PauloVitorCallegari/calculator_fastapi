# Calculadora API - FastAPI

Este é um projeto de uma API de calculadora desenvolvida com **FastAPI**, seguindo a arquitetura **MVC**. A API suporta as seguintes operações matemáticas:

- **Soma**
- **Subtração**
- **Multiplicação**
- **Divisão**

## Estrutura do Projeto
calculadora-python/ │ ├── main.py # Arquivo principal para iniciar a aplicação ├── models/ │ └── calculator_model.py # Define o modelo de dados (entrada da API) ├── controllers/ │ └── calculator_controller.py # Contém a lógica das operações matemáticas └── views/ └── calculator_view.py # Define as rotas da API


## Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado. Além disso, instale as dependências necessárias:

```
bash
pip install fastapi uvicorn
```
## Como Executar
1. Clone este repositório:
  git clone https://github.com/PauloVitorCallegariDalvi/calculator_fastapi.git
  cd calculadora-fastapi
2. Execute o servidor FastAPI:
  uvicorn main:app --reload
3. Acesse:
   Documentação interativa (Swagger UI): http://127.0.0.1:8000/docs
## Como Usar
### Testando as Operações
Você pode testar as operações matemáticas enviando requisições para as seguintes rotas:

- POST /calculator/add: Soma dois números.
- POST /calculator/subtract: Subtrai dois números.
- POST /calculator/multiply: Multiplica dois números.
- POST /calculator/divide: Divide dois números.
### Exemplo de Requisição
Envie um JSON com os valores value1 e value2 no corpo da requisição. Exemplo:
```
  {
  "value1": 10,
  "value2": 5
  }
```

### Exemplo de Resposta
Para a rota /calculator/add, a resposta será:
```
  {
  "operation": "addition",
  "result": 15
  }
```

## Estrutura do Código
main.py
Arquivo principal que inicializa o FastAPI e inclui as rotas.

models/calculator_model.py
Define o modelo de entrada da API usando o Pydantic.

controllers/calculator_controller.py
Contém a lógica das operações matemáticas (soma, subtração, multiplicação e divisão).

views/calculator_view.py
Define as rotas da API e conecta os modelos e controladores.

# Gerenciador de Carros
Esta API permite consultar e cadastrar carros em um banco de dados SQLite local.

## Tecnologias usadas
- Python 3.7
- Flask
- SQLite3

## Instalação
1. Clone o repositório:
```sh
git clone https://github.com/Thailson03/API_COM_FLASK
```
2. Instale as dependências:
```sh
pip install -r requirements.txt
```

## Rodando a API
1. Inicie o servidor:
```sh
python app.py
```
2. A API estará rodando em http://127.0.0.1:5000/.

## Endpoints
### GET /carros
Consulta todos os carros da base de dados.
- Exemplo de requisição:
```sh
GET http://127.0.0.1:5000/carros
```
### POST /carros
Insere um carro ao banco de dados.
- Como usar o POST: Ao fazer uma requisição POST, envie o corpo da requisição no formato JSON. Certifique-se de configurar a requisição para enviar o corpo como raw (texto simples) com o tipo de conteúdo como application/json.
- Exemplo de requisição:
```json
{
    "marca": "BMW",
    "modelo": "X5",
    "ano": 2019
}
```
- Exemplo de requisição com curl:
```sh
curl -X POST http://127.0.0.1:5000/carros -H "Content-Type: application/json" -d '{"marca": "BMW", "modelo": "X5", "ano": 2019}'
```

## Licença
Licença MIT
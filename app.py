from flask import Flask, make_response, jsonify, request
import libs.database as database

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():

    dados, mensagem = database.execute_select()

    return make_response(
        jsonify(
            mensagem=mensagem, 
            dados=dados,
        )
    )

@app.route('/carros', methods=['POST'])
def create_carro():

    carro = request.get_json()

    mensagem = database.execute_insert(carro)

    return make_response(
        jsonify(
            mensagem=mensagem,
            carro=carro,
        ),201
    )
        

if __name__ == '__main__':    app.run(debug=True)
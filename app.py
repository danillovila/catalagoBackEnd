from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

produtos = [
    {
    'id':1,
     "nome": "Feijão",
     "preco": "12,40",
    },
    {
    'id':2,
     "nome": "Arroz",
     "preco": "12,40",
    },
    {
    'id':3,
     "nome": "Cuscuz",
     "preco": "12,40",
    }
]


@app.route('/produtos', methods=['GET'])
def getProdutos():
    return jsonify(produtos)

@app.route('/produto/<string:nome>', methods=['GET'])
def getIdProdutos(nome):
    for produto in produtos:
        if produto.get("nome") == nome:
            return produto
    response = jsonify({'msg': 'Produto não encontrado'})
    response.status_code = 404
    return response
        

@app.route('/produto/<int:id>', methods= ['PUT'])
def updateProdutos(id):
    updateproduto = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(updateproduto)
            return jsonify(produtos[indice])
    return jsonify({'msg': "Operação não realizada"})
@app.route('/produtos', methods = ['POST'])
def createProduto():
    novoProduto = request.get_json()
    produtos.append(novoProduto)
    return jsonify({'msg': 'Produto Criado!'})

@app.route('/produto/<int:id>', methods=["DELETE"])
def deleteProduto(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]
            return jsonify({'msg': "Produto excluído"})
        response = jsonify({'msg': 'Produto não encontrado'})
        response.status_code = 404
    return  response

CORS(app)
app.run(debug=True)
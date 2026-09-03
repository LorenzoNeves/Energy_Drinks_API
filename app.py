from flask import Flask, jsonify, request

#abrir servidor
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    }
]

#consultar livros

#para isso ser considerada uma api devemos declarar ela com... ROTAS

#          url pra chegar naquele local
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


#Consultar por ID

#<>: "espero um numero inteiro que seja identificado como 'id' "
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#editar livro por id

@app.route('/livros/<int:id>', methods=['PUT'])
def edit_livro_por_id(id):

    #receber interações do usuario
    livro_alterado = request.get_json()

    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar

@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
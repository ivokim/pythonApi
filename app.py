#Ivo Byung Chul Kim
#Luiz Léis Rioja Silva
#Rafael Duram Santos
#Sergio Antonio Silva Junior
#Fabricio Batista
from flask import Flask, jsonify, request

app = Flask(__name__)

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])


@app.route('/alunos/<string:Nome>', methods=['POST'])
def novo_aluno(Nome):
    novo_aluno = request.get_json()
    database['ALUNO'].append(novo_aluno)
    for aluno in database['ALUNO']:
        print(aluno)
    return Nome


@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404

app.run()

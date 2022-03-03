# import json
from os import abort
from flask import Flask, jsonify, request, json, abort
from concurso import Competicao, Inscrito

cadastrados = []
vitor = Inscrito("Vitor Hugo", "Colégio")
pedro = Inscrito("Pedro Arantes", "OnLine")
gaby  =  Inscrito("Gabriela Santos", "Colégio")
duda  =  Inscrito("Eduardo Lima", "Colégio")
beto  =  Inscrito("Roberto Castro", "OnLine")
cadastrados.append(vitor)
cadastrados.append(pedro)
cadastrados.append(gaby)
cadastrados.append(duda)
cadastrados.append(beto)
disputas = []
disp1 = Competicao("xadrez","05/03/2022")
disp1.addInscrito(vitor)
disp1.addInscrito(gaby)
disp1.addInscrito(beto)
disp1.addInscrito(duda)
disp2 = Competicao("matematica","04/03/2022")
disp2.addInscrito(pedro)
disp2.addInscrito(beto)
disp2.addInscrito(gaby)
disputas.append(disp2)
disputas.append(disp1)


# o parâmetro "__name__" se refere ao
# nome do módulo que o chama
# no nosso caso é o nome do arquivo
app = Flask(__name__)

# busca um item em uma lista
def acha_item_or_404(id, lst):
  for item in lst:
    if item.id == id:
      return item
  abort(404, "o item não foi encontrado")

@app.errorhandler(400)
def dadoinvalido(erro):
  return (jsonify(erro=str(erro)), 400)

@app.errorhandler(404)
def dadoinexistente(erro):
  return (jsonify(erro=str(erro)), 404)

@app.route("/api/torneio/docs")
def docs_api_torneio():
  lst_docs_api = []
  lst_docs_api.append({
    "descricao": "Requisição para listar participantes cadastrados",
    "request": "GET",
    "route": "/api/torneio/cadastrados",
    "body": "sem uso",
    "retorna": "lista cadastrados"
  })
  lst_docs_api.append({
    "descricao": "Requisição para listar os torneios",
    "request": "GET",
    "route": "/api/torneio/disputas",
    "body": "sem uso",
    "retorna": "lista torneios"
  })
  lst_docs_api.append({
    "descricao": "Requisição para listar participantes inscritos em algum torneio",
    "request": "GET",
    "route": "/api/torneio/inscritos",
    "body": "sem uso",
    "retorna": "lista inscritos"
  })
  lst_docs_api.append({
    "descricao": "Requisição para buscar um torneio",
    "request": "GET",
    "route": "/api/torneio/disputas/id",
    "body": "JSON com chave 'id' do torneio",
    "retorna": "id e link do torneio ou 404"
  })
  lst_docs_api.append({
    "descricao": "Requisição para deletar um torneio",
    "request": "DELETE",
    "route": "/api/torneio/disputas/id",
    "body": "JSON com chave 'id' do torneio",
    "retorna": "id do torneio removido ou 404"
  })
  lst_docs_api.append({
    "descricao": "Requisição para cadastrar um participante",
    "request": "POST",
    "route": "/api/torneio/cadastrados",
    "body": "JSON com chave 'nome' e 'local'",
    "retorna": "id e link do cadastro"
  })
  lst_docs_api.append({
    "descricao": "Requisição para editar um participante",
    "request": "PUT",
    "route": "/api/torneio/cadastrados/id/",
    "body": "JSON com chave 'id', 'nome' e 'local'",
    "retorna": "id e link do cadastro"
  })
  lst_docs_api.append({
    "descricao": "Requisição para cadastrar um torneio",
    "request": "POST",
    "route": "/api/torneio/disputas",
    "body": "JSON com chave 'nome' e 'data'",
    "retorna": "id e link do torneio"
  })
  lst_docs_api.append({
    "descricao": "Requisição para inscrever participante em torneio",
    "request": "POST",
    "route": "/api/torneio/inscritos",
    "body": "JSON com chave 'iduser' e 'iddisputa' sendo a id do participante e do torneio",
    "retorna": "id e link do torneio ou 404"
  })
  return jsonify(lst_docs_api)

@app.route("/api/torneio/inscritos", methods=["POST"])
def inscrevedisputa():
  dado = request.data # -> como texto
  # precisamos do json.loads() para
  # carregar como JSON e fazer um dict
  dado = json.loads(request.data)
  id_user = dado.get("iduser")
  id_disputa = dado.get("iddisputa")
  user = None
  disputa = None
  if id_user == None or id_disputa == None:
    abort(400, "'id' de participante e disputa precisam ser informados!")
  else:
    for item in cadastrados:
      if item.id == id_user:
        user = item
    if user == None:
      abort(404, "'id' de participante não cadastrado!")
    for item in disputas:
      if item.id == id_disputa:
        disputa = item
    if disputa == None:
      abort(404, "'id' de disputa não cadastrada!")
    disputa.addInscrito(user)
  return dado

@app.route("/api/torneio/inscritos")
def listainscritos():
  lst_tmp = []
  for item in disputas:
    lst_tmp.append(item.inscritosToList())
  return jsonify(lst_tmp)

@app.route("/api/torneio/disputas/id")
def buscadisputasid():
  dado = json.loads(request.data)
  id = dado.get("id")
  if id == None:
    abort(400, "id do torneio não informado")
  for item in disputas:
    if item.id == id:
      return {
        "id": item.id,
        "url": f"/api/torneio/disputas/{item.id}/"
      }
  abort(404, "Torneio não encontrado")

@app.route("/api/torneio/disputas", methods=["POST"])
def criadisputa():
  dado = json.loads(request.data)
  nome = dado.get("nome")
  data = dado.get("data")
  if nome and data:
    novo = Competicao(nome, data)
    disputas.append(novo)
    return {
      "id": novo.id,
      "url": f"/api/torneio/disputas/{novo.id}/"
    }
  abort(400, "Dados inválidos")

@app.route("/api/torneio/disputas/<int:id>/")
def detalhadisputa(id):
  for item in disputas:
    if item.id == id:
      return jsonify(item.competicaoToJSON())
  abort(404, "Torneio não encontrado")

@app.route("/api/torneio/disputas/id", methods=["DELETE"])
def deletadisputa():
  dado = json.loads(request.data)
  id = dado.get("id")
  for item in disputas:
    if item.id == id:
      disputas.remove(item)
      return jsonify(id=id)
  abort(404, "Torneio não encontrado")

@app.route("/api/torneio/disputas")
def listadisputas():
  lst_tmp = []
  for item in disputas:
    lst_tmp.append(item.competicaoToJSON())
  return jsonify(lst_tmp)

@app.route("/api/torneio/cadastrados/id/", methods=["PUT"])
def edita_participante():
  dado = json.loads(request.data)
  id = dado.get("id")
  nome = dado.get("nome")
  local = dado.get("local")
  if not nome or not local or not id:
    abort(400, "'id', 'nome' e 'local' precisam ser informados!")
  else:
    item = acha_item_or_404(id, cadastrados)
    item.nome = nome
    item.local = local
  return jsonify(item.__dict__)

@app.route("/api/torneio/cadastrados", methods=["POST"])
def cadastraparticipante():
  dado = json.loads(request.data)
  nome = dado.get("nome")
  local = dado.get("local")
  if nome == None or local == None:
    abort(400, "'nome' e 'local' precisam ser informados!")
  else:
    cadastrados.append(Inscrito(nome, local))
  return dado

@app.route("/api/torneio/cadastrados")
def listacadastrados():
  lst_tmp = []
  for item in cadastrados:
    lst_tmp.append(item.__dict__)
  return jsonify(lst_tmp)

@app.route("/")
def indice():
  return "<h1>Flask está configurado com sucesso</h1>"

@app.route("/api/locais", methods=["POST"])
def cria_evento():
  return "requisição POST"

@app.route("/api/locais")
def dizlocais():
  lugares = [{
      "bairro": "Cohafuma",
      "local": "Igreja",
    },
    {
      "bairro": "Vinhais",
      "local": "Praça Letrado",
    },
  ]
  return jsonify(lugares)

@app.route("/api/locais2")
def dizlocais2():
  lst_tmp = []
  for item in disputas:
    lst_tmp.append(item.competicaoToJSON())
  return jsonify(lst_tmp)

# executar com:
# FLASK_ENV=development flsak run

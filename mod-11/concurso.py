from flask import json


class Inscrito:
  id = 0
  def __init__(self, nome, local) -> None:
    Inscrito.id += 1
    self.id = Inscrito.id
    self.nome = nome
    self.local_inscricao = local
    self.inscricoes = []
  def addInscricao(self, nome_disputa, cod_inscricao):
    self.inscricoes.append({
      "disputa": nome_disputa,
      "inscricao": cod_inscricao,
    })
  def setNumeroInscricao(self, codigo):
    self.cod_inscricao = f"{codigo}"
  def toJSON(self):
    return self.__dict__


class Competicao:
  id = 0
  def __init__(self, nome, data):
    Competicao.id += 1
    self.id = Competicao.id
    self.qtd_inscritos = 0
    self.nome = nome
    self.data = data
    self.inscritos = []
  def addInscrito(self, participa : Inscrito):
    self.inscritos.append(participa)
    self.qtd_inscritos += 1
    participa.addInscricao(self.nome, self.qtd_inscritos)
  def inscritosToHTML(self):
    saidaHTML = ""
    for item in self.inscritos:
      saidaHTML += f"""
      <tr>
        <td>{item.cod_inscricao}</td>
        <td>{item.nome}</td>
        <td>{item.local_inscricao}</td>
      </tr>
      """
    return saidaHTML
  def competicaoToHTML(self):
    saidaHTML = f"""
    <table>
      <tr>
        <th>
          Código
        </th>
        <th>
          Nome
        </th>
        <th>
          Local
        </th>
      </tr>
      {self.inscritosToHTML()}
    </table>
    """
    return saidaHTML
  def inscritosToList(self):
    lst_tmp_inscritos = []
    for item in self.inscritos:
      lst_tmp_inscritos.append({
        "cod_cadastrado": item.id,
        "Apelido": item.nome,
        "Localização": item.local_inscricao,
        "Inscrições": item.inscricoes,
      })
    return lst_tmp_inscritos
  def inscritosToJSON(self):
    lst_tmp_inscritos = []
    for item in self.inscritos:
      lst_tmp_inscritos.append({
        "ID": item.id,
        "Nome": item.nome,
        "Local": item.local_inscricao,
        # "Inscrição": item.inscricoes,
      })
    saidaJSON = json.dumps(lst_tmp_inscritos)
    return saidaJSON
  def competicaoToJSON(self):
    saidaJSON = {
      "codigo": self.id,
      "nome": self.nome,
      "data": self.data,
      "qtd_inscritos": self.qtd_inscritos,
      "inscritos": self.inscritosToList(),
    }
    return saidaJSON
  def competicaoToDict(self):
    saidadict = {
      "codigo": self.id,
      "nome": self.nome,
      "data": self.data,
      "qtd_inscritos": self.qtd_inscritos,
      # "inscritos": self.inscritosToList(),
    }
    return saidadict


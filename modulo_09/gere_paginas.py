import json
from concurso import Competicao
from concurso import Inscrito

class CompeticaoPagina:
  def __init__(self) -> None:
      self.pagina = ""
      self.conteudo = ""
  def carregaPagina(self, caminho):
    estilo_css = """
    <style>
      table {
        border-collapse: collapse;
      }
      td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }
    </style>
    """
    vitor = Inscrito("Vitor Hugo", "Colégio")
    pedro = Inscrito("Pedro Arantes", "OnLine")
    gaby = Inscrito("Gabriela Santos", "Colégio")
    duda = Inscrito("Eduardo Lima", "Colégio")
    beto = Inscrito("Roberto Castro", "OnLine")
    disputas = []
    disp1 = Competicao("xadrez","05/03/2022")
    disp1.addInscrito(vitor)
    disp1.addInscrito(gaby)
    disp1.addInscrito(beto)
    disp1.addInscrito(duda)
    disp2 = Competicao("matematica","04/03/2022")
    disp2.addInscrito(pedro)
    disp2.addInscrito(gaby)
    disp2.addInscrito(beto)
    disputas.append(disp1)
    disputas.append(disp2)
    if caminho == "/":
      self.conteudo = "text/html; charset=utf-8"
      self.pagina = f"""
      <html>
        <head lang="pt-BR">
          <meta charset="utf-8">
          <title>Competições | Inicial</title>
          <link href="img/favicon.ico" rel="icon">
          {estilo_css}
        </head>
        <body>
          <h1 class="titulo"> Competições </h1>
          <h2> Crie suas competições aqui e deixe que cuidaremos de tudo </h2>
          <h2>
            Bem-vindo à Competições, seu portal de competições online.</h2>
            <p>Caminho: {caminho}</p>
          <ul>
            <li><em>Confira nossas promoções</em></li>
            <li>Receba informações sobre locais disponíveis</li>
            <li>Conheça nossos preços e planos</li>
            <li>Agende <strong>sem sair de casa</strong> o seu evento</li>
          </ul>
          <figure>
            <img src="img/matriz-musicdot.png" alt="Foto da matriz da musicdot">
            <figcaption>Matriz da MusicDot</figcaption>
          </figure>
          <p dir="auto"><a href="./eventos"> Lista de Eventos </a></p>
        </body>
      </html>
      """.encode()
    elif caminho == "/eventos":
      tmp_html = ""
      for item in disputas:
        tmp_html += f"""
        <h3>{item.nome}</h3>
        {item.competicaoToHTML()}
        """
      self.conteudo = "text/html; charset=utf-8"
      self.pagina = f"""
      <html>
        <head lang="pt-BR">
          <meta charset="utf-8">
          <title>Competições | Lista de Inscritos</title>
          <link href="img/favicon.ico" rel="icon">
          {estilo_css}
        </head>
        <body>
          <h1 class="titulo"> Competições </h1>
          <h2> Lista com os inscritos </h2>
            <p>Caminho: {caminho}</p>
          {tmp_html}
          <figure>
            <img src="img/matriz-musicdot.png" alt="Foto da matriz da musicdot">
            <figcaption>Matriz da MusicDot</figcaption>
          </figure>
          <p dir="auto"><a href="/"> Página Inicial </a></p>
        </body>
      </html>
      """.encode()
    elif caminho == "/api/eventos":
      lst_tmp_competicoes = []
      for item in disputas:
        lst_tmp_competicoes.append(
          item.competicaoToJSON()
        )
      self.conteudo = "application/json; charset=utf-8"
      self.pagina = json.dumps(lst_tmp_competicoes).encode()
    elif caminho == "/api2/eventos":
      lst_tmp_competicoes = []
      for item in disputas:
        lst_tmp_competicoes.append({
          "id": "1",
          "nome": "xadrez",
          "insc": [
            {
            "cod_insc": "3",
            "nome": "alberto",
            "local": "Colégio",
            },
            {
            "cod_insc": "3",
            "nome": "alberto",
            "local": "Colégio",
            }
          ]
        })
      self.conteudo = "application/json; charset=utf-8"
      self.pagina = json.dumps(lst_tmp_competicoes).encode()
    return (self.pagina, self.conteudo)

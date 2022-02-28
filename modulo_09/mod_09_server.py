from gere_paginas import CompeticaoPagina
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

# endereço servidor como tupla
srv_address = ("localhost", 8000)

class CstmHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    controla_concursos = CompeticaoPagina()
    # abaixo, usar enviar conteúdo
    # caso precise empacotar tudo
    # numa variável pra enviar
    dados, conteudo = controla_concursos.carregaPagina(self.path)
    # usar para status
    self.send_response(200)
    self.send_header("Autor", "Alexandre")
    # usar por padrão linha abaixo
    self.send_header("Content-Type", conteudo)
    self.end_headers()
    self.wfile.write(dados)

# servidor com socket e handler
# socket = (end_srv, prt)
# handler apenas qual classe
servidor1 = HTTPServer(srv_address, CstmHandler)

# esperar requisições
servidor1.serve_forever()

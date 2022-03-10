# Módulo 12

## Índice

   1. [Introdução ao Flask](#objetos-imutáveis)
   2. [Variáveis do Ambiente Flask](#objetos-mutáveis)
   3. [Listando Eventos](#definindo-classes)
   4. [Detalhar Evento](#herança)
   5. [Lidando com erros no Flask](#exercícios)
   6. [Criar Novo Evento](#exercícios)
   7. [Deletar Evento](#exercícios)
   8. [Editar Evento (PUT)](#exercícios)
   9. [Editar Evento Parcial (PATCH)](#exercícios)

## Criando Projeto Django

Como no flask, vamos criar um ambiente virtual para usar neste projeto do Django. Assim, dentro da pasta do projeto usamos:

```python
python -m venv venv
```

> Nota: se antes de criar o `venv` você abrir o VS Code na pasta do projeto, a `venv` criada vai ser automaticamente reconhecida e indicada pelo VS Code a ser utilizada como interpretador padrão para o projeto

Criado a *venv*, precisamos agora instalar dentro dela o Django com o comando abaixo:

> Nota:
> - de dentro do VS Code, ao abrir o terminal Git Bash, a `venv` já estará ativa
> - de fora, ativamos a `venv` de 2 maneiras:
> > 1. se na `venv` tiver a pasta `bin`, ativamos com `source venv/bin/activate`
> >
> > 2. caso haja `Scripts`, usar `source venv/Scripts/activate`

```python
django-admin startproject nome_pjt . 
```

Após o comando acima, será criado uma pasta com o *nome_pjt* passado e outro arquivo `manage.py` com algumas funcionalidades do Django

Agora já podemos rodar um servidor com o seguinte comando:

```python
python manage.py runserver
```

No linux, Ubuntu numa VM VirtualBox, o python está na versão 3.8 e
precisou instalar o `sudo apt install python3.8-venv` para conseguir criar o `venv` no projeto

No python 3.8 ainda existe a pasta bin com o activate dentro e
ativei com `source venv/bin/activate`

Em seguida, instalei o django com `pip install django` e já instalou a mais atual 4.0.3

Para criar o projeto django usei
`django-admin startproject nome_pjt lcl_server`, criando assim:

```python
django-admin startproject torneios .
```

O django criou uma pasta com o nome "torneios" e deixou nosso servidor `manage.py` em `.` onde foi executado o comando

## Criando nosso app

Com o Django, nossas funcionalidades serão modularizadas com o uso de apps e cada app representará uma funcionalidade completa, como se o app ficasse responsável por uma parte completamente funcional do projeto

Com isso, no nosso servidor que receberá as requisições, vamos direcionar os pedidos de uma parte do projeto para nosso app em criação

```python
# criando nosso app
django-admin startapp agenda
```

Assim como no Flask, no Django também referenciamos uma url de requisição para uma função, ou view

Porém, no Django, incluímos esses caminhos em um arquivo diferente do qual executamos o servidor

Como vimos, nosso servidor encontra-se no `manage.py` e o direcionamento, ou roteamento, das urls fica dentro da pasta principal do projeto em `urls.py`

Dentro de `urls.py` vamos incluir um caminho com `path(caminho, view)`
na lista de `urlpatterns` indicando pro servidor quem responderá ao pedido

```python
# arquivo urls.py na pasta principal
# primeiro importamos a função
from agenda.views import index
urlpatterns = [
   path('admin/', admin.site.urls),
   # depois incluímos o caminho
   path("agenda", index),
]

# views.py dentro de agenda
# abaixo de "Create your views"
def index(request):
   return HttpResponse("Olá mundo")
```

Assim, quando acessamos nosso domínio no caminho `agenda` o servidor encaminhará para a função `index` dentro da *`views.py`* da nossa app agenda

Como boa prática, podemos também incluir um arquivo `urls.py` da pasta agenda inteiro no `path` para direcionar todos os pedidos ao caminho `agenda` ao app agenda

Assim, sempre que uma requisição com o caminho iniciado por `agenda` chegar ao servidor, encaminhamos ao nosso app agenda a responsabilidade de respondê-la

Logo, no arquivo `urls.py` do projeto, incluiremos:

```python
# urls.py do projeto
# com o *as* damos um apelido diferente
# ao padrão de urls da agenda
from agenda.urls import urlpatterns as agenda_urls
urlpatterns = [
   path("agenda", include(agenda_urls))
]
```

Desta forma, informamos ao nosso servidor que quando o caminho tiver *agenda* nele, o app agenda vai tratar os pedidos de requisição e o arquivo `urls.py` de agenda passa a rotear as requisições

---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Criando Models e Exibindo Torneio

Quando criamos nosso app com o Django o arquivo `models.py` vai nos ajudar a declarar nossas entidades

Neste arquivo teremos as classes com as quais iremos trabalhar no projeto declarando seus atributos e métodos aqui

```python
# no model.py do app
class Inscrito:
  id = 0
  def __init__(self, nome, local) -> None:
    Inscrito.id += 1
    self.id = Inscrito.id
    self.nome = nome
    self.local = local
    self.inscricoes = []
class Competicao:
  id = 0
  def __init__(self, nome, data):
    Competicao.id += 1
    self.id = Competicao.id
    self.qtd_inscritos = 0
    self.nome = nome
    self.data = data
    self.inscritos = []
# código para teste vem aqui também
# neste caso criei 2 torneios
disp1 = Competicao("xadrez","05/03/2022")
disp2 = Competicao("matematica","04/03/2022")
# depois incluí ambos numa lista
disputas = []
disputas.append(disp1)
disputas.append(disp2)
```

Agora vamos mostrar uma tabela listando as competições criadas

Primeiro incluiremos na `urls.py` da agenda um caminho que responderá pela requisição, então:

```python
# urls.py da agenda
from django.urls import path
from agenda.views import agenda_mostra_disputas

urlpatterns = [
    path("/disputas", agenda_mostra_disputas),
]
```

Agora, criamos a função em `views.py` do app agenda para responder os pedidos

```python
def agenda_mostra_disputas(request):
  return render(
    request=request,
    context={"table_linhas": disputas},
    template_name="agenda/exibe_disputa.html",
  )
```

No próximo capítulo explico melhor a linha com `template_name="agenda/exibe_disputa.html",` passado para o render

---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Utilizando Django Template

Agora com os *templates* vamos conseguir separar códigos html do nosso código python

Assim vamos criar uma pasta *templates/nome_app* dentro de nosso app para dentro dela criar nossos arquivos com código html personalizado que será atualizado dinamicamente quando executarmos o programa

Então, dentro da nossa pasta `templates/agenda` vamos criar um arquivo `exibe_disputas.html` para colocar dentro dele todo o html que vamos precisar

> ```html
> <!-- dentro do arquivo html -->
> <html>
>   <h1>Disputa: {{disputa.id}}</h1>
>   <p>Id: {{disputa.id}}</p>
>   <p>Nome: {{disputa.nome}}</p>
>   <p>Data: {{disputa.data}}</p>
> </html>
> ```

> Nota1:
> > no VS Code é possível selecionar o modo de linguagem para o Django HTML para formatar o arquivo html direitinho
> 
> Nota2:
> > no arquivo template também é possível inserir alguns códigos nele como um `if` ou `for` para gerar as linhas de uma tabela ou filtrar algo que não queremos que seja mostrado, no arquivo fica assim:
> ```html
>  {% for item in table_linhas %}
>    <tr>
>      <td>{{ item.id }}</td>
>      <td>{{ item.nome }}</td>
>      {{% if  %}<td>{{ item.data }}</td>{% endif %}
>    </tr>
>  {% endfor %}
> ```

Para importar nosso arquivo template precisamos chamar na view o *loader* do Django da seguinte maneira:

```python
# dentro de nossa view importamos
from django.template import loader
# criamos referência ao template
template = loader.get_template("agenda/exibe_disputa.html")
```

Depois de todo esse processo ainda precisamos informar ao Django que nosso app existe e qual o seu nome

No arquivo `settings.py` localizado na pasta do projeto principal temos que incluir um item na lista `INSTALLED_APPS` com a linha a seguir:

> ```python
> INSTALLED_APPS = [
>   ... # código existente
>   'agenda.apps.AgendaConfig',
> ]
> ```

Por fim, após a requisição ser roteada pelo urls do app e direcionada a função da nossa view, esta retornará com o uso de um `render` a página construída com o código estático e dinâmico interpolado num só da seguinte maneira

> ```python
> return render(
>   request=request,
>   context={"table_linhas": disputas},
>   template_name="agenda/exibe_disputa.html",
> )
> ```

---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Trabalhando com Banco de Dados

Neste capítulo vamos apresentar muito por alto a ideia de um banco de dados relacional no qual gravaremos de forma mais persistente, nossas entidades e suas relações entre todas elas

Imaginem o seguinte baseado no exemplo já comentado, no qual vamos controlar competições e as pessoas cadastradas e inscritas em cada uma

Num banco de dados, salvaremos nossos objetos em tabelas que representam a classe deles e em alguns casos também teremos tabelas para representar as relações entre as entidades

Nos nossos exemplos usaremos o Django ORM para fazer a persistência dos nossos objetos

---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Django ORM e migrações

Agora vamos ver alguns exemplos do uso do Django ORM com o SQLite porém, futuramente migraremos para o Postgres

O ORM em Django ORM significa Object Relational Mapping, ou um mapeamento de objetos relacionais e faz com que as entidades com seus atributos e seus relacionamentos sejam gravados em tabelas no banco de dados

Primeiramente precisamos ir em nosso arquivo `models.py` dentro do nosso app e fazer com que o django saiba que uma classe dali será persistida no banco como uma tabela da seguinte forma:

```python
# dentro de models.py do app
# declaramos a classe assim
class Categoria(models.Model):
   nome = models.CharField(max_length=60, unique=True)
```

No código acima precisamos que a classe herde de `models.Model` para que o Django saiba que aquela classe será gravada no banco de dados e na linha `nome = models.CharField(max_length=60, unique=True)` dizemos que o atributo *nome* será na tabela do tipo *CharField* de tamanho 60 e que o valor será único não podendo ter outro registro igual na tabela

Agora precisamos enviar essas alterações para o arquivo de banco de dados executando no terminal o seguinte

```python
python manage.py makemigrations
```

Dentro da pasta `migrations` do nosso app será criado um arquivo sequencial que terá comandos a serem executados para atualizar nosso banco conforme as alterações feitas no projeto

Após a geração deste arquivo podemos efetivar essas alterações no banco com o comando a seguir:

```python
python manage.py migrate
```

Para verificar se tudo funcionou temos o comando `python manage.py dbshell` que inicia o shell do SQLite e nele podemos digitar `.tables` para ver as tabelas criadas no banco

---

[Voltar ao Topo](#módulo-12)

---

## Fazendo consultas pelo Shell



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Django Admin



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Listagem de Torneios



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Adicionando Data as Torneios



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Buscando e Exibindo Torneio



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Navegando entre Páginas do App



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---

## Enviando um Formulário



---

[Voltar ao Topo](#m%C3%B3dulo-12)

---


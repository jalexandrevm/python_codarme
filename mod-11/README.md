# Módulo 11

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

## Introdução ao Flask

- Criar novo projeto
- Criar venv neste projeto
- Instalar o flask no venv

Na versão mais nova o python3 não existe mais, agora usar:

-python -m venv venv

### Flask - usando o framework

Nos arquivos python incluir:

> `from flask import Flask`
> para conseguir usar o flask
> precisamos instalar o pacote
> na venv que criamos

Na versão 3.10.2 o `source venv/bin/activate` não funciona mais, a pasta bin sumiu na nova versão e criou-se a Scripts agora com o activate

Via terminal Git Bash do VS Code, usar:

```python
source venv/Scripts/activate
```

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Variáveis do Ambiente Flask

Para o seu funcionamento, o Flask precisa de duas variáveis de ambiente:

> - FLASK_APP=aplication-name
> >diz pro Flask qual aplicação rodar
> >ex: FLASK_APP=test.py flask run
> - FLASK_ENV=development
> >informa ao Flask o modo de execução do
> >aplicativo
> >em *produção* precisamos parar tudo pra 
> >executar novamente e atualizar
> >em *development* quando alteramos algo
> >o Flask já faz isso automaticamente


---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Listando Eventos



---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Detalhar Evento



---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Lidando com erros no Flask

abort(cod_erro, msg_erro)
> envia resposta genérica com o erro
make_response()
> cria um objeto Response para retornar
> informação personalizada
> ex:
> data = {"erro": f"Sem registro {id}"}
> return make_response(jsonify(data),404)
@app.errorhandler(cod_erro)
> diz ao Flask que sempre que um erro 404
> for disparado, a função abaixo deve ser
> executada
> def nao_encontrado(erro):
>   data = {"erro": str(erro)}
>   return (jsonify(data), 404)
> com isso voltamos a usar o abort()

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Criar Novo Evento

Quando recebemos uma requisição POST do cliente, devemos primeiramente **"parciar"** os dados para conseguir usá-los

> - pegar dados de request recebida
> - usar json.loads() nos dados criando dict
> - do dict, retirar os dados

```python
# assim recebemos apenas texto
dado = request.data
# assim recebemos um `dict`
dado = json.loads(request.data)
# agora podemos usar chave: value
nome = dado.get("nome")
senha = dado.get("senha")
```

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Deletar Evento



```python

```

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Editar Evento (PUT)



```python

```

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---

## Editar Evento Parcial (PATCH)



```python

```

---

[Voltar ao Topo](#m%C3%B3dulo-11)

---


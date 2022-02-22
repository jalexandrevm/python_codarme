# Módulo 07

## Índice

1. [Funções](#fun%C3%A7%C3%B5es)
   1. [Declaração](#declara%C3%A7%C3%A3o)
   2. [Função sem retorno](#fun%C3%A7%C3%A3o-sem-retorno)
   3. [Função com retorno](#fun%C3%A7%C3%A3o-com-retorno)
   4. [Função com argumentos nomeados](#fun%C3%A7%C3%A3o-com-argumentos-nomeados)
   5. [Função com argumento padrão](#fun%C3%A7%C3%A3o-com-argumento-padr%C3%A3o)
2. [Exercícios](#exerc%C3%ADcios)
   1. []()
   2. []()
   3. []()
   4. []()
   5. []()
   6. []()
   7. []()

## Funções

### Declaração

No python, quando queremos agrupar códigos que executem algo específico usamos as *funções* e sua declaração é feita da seguinte forma:

```python
def nome_função(parâmetros):
   bloco_operações
   return algo
```

Uma função pode ou não ter parâmetros informados em sua chamada assim como retornar ou não algum valor

---

[Voltar ao Topo](#m%C3%B3dulo-07)

---

### Função sem retorno

Uma situação mais real de uso de uma função seriam funções que executam operações com variáveis

Como imprimir dados de uma lista de dicionários, veja a seguir um exemplo:

```python
# função com parâmetro
def imprime_dados_aluno(aluno):
   print(f"Nome: {aluno["nome"]} cursando: {aluno["curso"]}")

aluno1 = {
   "matricula": "202200154",
   "nome": "Alberto Brito",
   "curso": "Física",
   "ano_entrada": 2022,
   "semestre": 1,
}

aluno2 = {
   "matricula": "202200135",
   "nome": "Michele Alvarez",
   "curso": "Sistema da Informação",
   "ano_entrada": 2021,
   "semestre": 2,
}

alunos = [aluno1, aluno2]

# iteramos a lista de alunos
for item in alunos:
   # imprimimos como queremos
   imprime_dados_aluno(item)


```

---

[Voltar ao Topo](#m%C3%B3dulo-07)

---

### Função com retorno

Outra possibilidade é o retorno de alguma coisa após efetuar operações com dados repassados, como argumentos, na chamada da função como a seguir:

```python
def media_notas(lista):
   i = 0
   soma = 0
   qtd_notas = len(lista)

   while i < qtd_notas:
      soma = soma + lista[i]
      i = i + 1
   return soma / qtd_notas


notas = [9.5, 10, 8, 7.5]

print("Média de:", media_notas(notas))
```

---

[Voltar ao Topo](#m%C3%B3dulo-07)

---

### Função com argumentos nomeados

Quando precisamos usar muitos parâmetros em uma função pode ficar complicado identificar ou até mesmo localizar um ou outro

Assim, podemos na chamada da função informar a qual parâmetro aquele argumento se refere, como visto num simples exemplo a seguir:

```python
def apresente(nome, curso, ano):
   print(f"Olá {nome}.")
   print(f"Bem vindo ao curso de {curso} iniciado em {ano}.")

apresente("George", ano=2019, curso="Java")

```

Precisamos sempre lembrar que quando usamos argumentos nomeados estes devem estar após os posicionais como no código acima

---

[Voltar ao Topo](#m%C3%B3dulo-07)

---

### Função com argumento padrão

Quando trabalhamos com funções que podem assumir, como parâmetro, um valor padrão, declaramos esse valor em sua definição

Lembrando sempre que, assim como o uso dos argumentos nomeados, também devemos declará-los após os parâmetros obrigatórios

Vejamos o código a seguir:

```python
# total é único obrigatório
def valor_venda(total, mao_de_obra=150, desc=0):
   return (total + mao_de_obra) - desc

```

Neste caso, caso os dois últimos parâmetros não sejam informados, os valores padrão serão usados

Caso algum argumento seja informado na chamada da função, os valores serão sobrepostos ao padrão definido

---

[Voltar ao Topo](#m%C3%B3dulo-07)

---

## Exercícios

### Número é primo

```python
def e_primo(num):
  # pulo do gato
  if num * num < 2:
    return False
  divisor = 2
  primoStatus = True
  while divisor < num and primoStatus:
      if (num % divisor == 0):
          primoStatus = False
      divisor += 1
  return primoStatus

```


### Maior da lista e posição

```python
def posmaior(lista):
  maior = None
  pos = 0
  for i in range(len(lista)):
      if maior == None or lista[i] > maior:
          maior = lista[i]
          pos = i

  return (pos, maior)

```


### Maior de idade pessoa tupla

```python
def maior_idade(pessoa):
  nome, idade = pessoa
  if idade >= 18:
    print("maior de idade")
  else:
    print("menor de idade")

```


### Maior de idade pessoa tupla ou dicionário

```python
def maior_idade(pessoa):
  if type(pessoa) == tuple:
    nome, idade = pessoa
  elif type(pessoa) == dict:
    idade = pessoa["idade"]
  else: # desnecessário se argumento válido
    return "formato de pessoa inválido"
  if idade >= 18:
    print("maior de idade")
  else:
    print("menor de idade")

```


### Elemento tem na lista

```python
def constalista(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

```


### Fatorial recursivo

```python
def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

```


---

[Voltar ao Topo](#m%C3%B3dulo-07)

---




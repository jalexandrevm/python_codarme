# Módulo 06

## Índice

1. [Listas - list](#listas---list)
   1. [Declaração](#declara%C3%A7%C3%A3o)
   2. [Mutabilidade](#mutabilidade)
   3. [Ordenação](#ordena%C3%A7%C3%A3o)
   4. [Heterogeneidade](#heterogeneidade)
   5. [Iteração](#itera%C3%A7%C3%A3o)
2. [Tuplas - tuple](#tuplas---tuple)
   1. [Declaração](#declara%C3%A7%C3%A3o-1)
   2. [Utilização](#utiliza%C3%A7%C3%A3o)
   3. [Imutabilidade](#imutabilidade)
3. [Conjuntos - set](#conjuntos---set)
   1. [Declaração](#declara%C3%A7%C3%A3o-2)
   2. [Mutabilidade](#mutabilidade-1)
   3. [Utilização](#utiliza%C3%A7%C3%A3o-1)
4. [Dicionários - map](#dicion%C3%A1rios---map)
   1. [Declaração](#declara%C3%A7%C3%A3o-3)
   2. [Mutabilidade](#mutabilidade-2)
   3. [Utilização](#utiliza%C3%A7%C3%A3o-2)
5. [Loop for](#loop-for)
   1. [Declaração](#declara%C3%A7%C3%A3o-4)
   2. [Iterabilidade](#iterabilidade)
   3. [Utilização](#utiliza%C3%A7%C3%A3o-3)


## Listas - list

### Declaração

Quando trabalhamos com *listas*, precisamos antes de tudo criar a variável inicializando com *colchetes*, vazios ou não

```python
numero = [] # lista vazia

notas = [7, 9, 8.5, 10] # preenchida

```

### Mutabilidade

Mesmo *declarando valores iniciais* na inicialização da variável, podemos usar diversos métodos para manipulá-la, como:

```python
from audioop import reverse
# declarando com valores
carros = ["prisma", "gol", "uno"]
print(carros)
carros.append("strada") # inclui no fim
print(carros)
carros.remove("uno") # remove valor passado
print(carros)
carros.sort() # ordena no padrão
print(carros)
carros.sort(reverse=True) # ordena modo inverso
print(carros)
carros.pop() # remove e retorna o último
print(carros)
# inserindo em qualquer posição
# índice e o valor são passados
carros.insert(1, 9.5)
print(carros)
# exclui o item da posição 0 retornando 
carros.pop(0)
```

### Ordenação

Essa lista não *ordena* seu conteúdo na inserção, logo a ordem de *inserção* é mantida até que algo a modifique

Para a *ordenação* do conteúdo temos o método `list.sort()` que pode ser chamado por qualquer lista

O método `.sort()` aceita *parâmetros* que podem personalizar a ordenação desejada

O código acima é testável e demonstra várias possibilidades de uso da lista

### Heterogeneidade

O mais *interessante* das listas é que podemos, na mesma lista, colocar valores de *tipos diferentes* como inteiros, decimais, palavras ou lógicos; criando assim uma lista *heterogênea*

Além disso, podemos ter *listas dentro de listas* e um exemplo disso é uma *lista de pessoas* sendo que *cada pessoa é uma lista* com seu nome, idade e seu telefone; podemos verificar abaixo:

```python
pessoas = [
  ["Paulo", 35, 9598542316],
  ["Pedro", 23, 17999453241],
]

pessoa = ["João", 21, 11981176152]

print(pessoas)
print(pessoa)

pessoas.insert(0,pessoa)

print(pessoas)

```

### Iteração

Normalmente quando iteramos com listas precisamos saber seu tamanho para usar como limite em loops. Logo, uma facilidade da lista é sua propriedade de tamanho obtido com a função `len()` passando como parâmetro a lista

```python
notas = [9.5, 10, 8, 7.5]

i = 0
soma = 0
qtd_notas = len(notas)

while i < qtd_notas:
  soma = soma + notas[i]
  i = i + 1

print("Soma das notas:", soma)

media = soma / qtd_notas

print("Média de:", media)
```
---
[Voltar ao Topo](#m%C3%B3dulo-06)
---
## Tuplas - tuple

As *tuplas* são bem parecidas com as *listas* mas com algumas peculiaridades

### Declaração

Na *declaração da variável* do tipo tupla no lugar dos *colchetes* usamos *parênteses* ou simplesmente nada, mas recomenda-se o uso principalmente pela organização

```python
numero = () # lista vazia

notas = (7, 9, 8.5, 10) # preenchida

notas = 7, 10, 8.5 # não recomendado

```

### Utilização

Normalmente as *tuplas* é que são preferidas para o uso com *valores diferentes* ao invés das listas

Quando usamos *listas*, normalmente esperamos que seu conteúdo seja do *mesmo tipo* e caso sejam de objetos esses sim seriam de tuplas

Melhorando o código anteriormente usado podemos usar a *boa prática* de fazer os *objetos* do tipo *tupla* e as listas deles como listas normais

```python
pessoas = [
  ("Paulo", 35, 9598542316),
  ("Pedro", 23, 17999453241),
]

pessoa = ("João", 21, 11981176152)

print(pessoas)
print(pessoa)

pessoas.insert(0,pessoa)

print(pessoas)

```

### Imutabilidade

Após a *atribuição de valores* a uma tupla **não** conseguimos mais **alterar** seu conteúdo

Mesmo não podendo modificar o conteúdo da tupla, ainda podemos *acessar* seu conteúdo igual fazemos com as *listas*

Porém, geralmente usamos a prática de fazer o **unpack** da tupla, como abaixo:

```python
carro = ("Fiat", "Uno", 2001)
# ao invés disto
marca = carro[0]
modelo = carro[1]
ano = carro[2]
# usamos assim
marca, modelo, ano = carro
```
---
[Voltar ao Topo](#m%C3%B3dulo-06)
---
## Conjuntos - set

Os *conjuntos* são bem parecidas com as *listas* e podem até serem declarados a partir delas

### Declaração

Na *declaração da variável* do tipo set no lugar dos *colchetes* usamos *chaves* ou também podemos usar `set()` para, com uma lista, criarmos nosso conjunto

```python
esportes = {"volei", "basquete"}

esportes_2 = set(["volei", "basquete"])

# comparando as declarações
print(esportes == esportes_2)

# True indicando declarações iguais
```

### Mutabilidade

Vimos que com o *set*, assim como toda variável, podemos na declaração já atribuir *valores iniciais*, porém também é possível sua modificação

Para *adicionar* um item ao set usamos o método `.add()` passando o valor a incluir, lembrando que se *repetido* não será incluído

Com os conjuntos, podemos utilizar as mesmas operações da matemática como a união, interseção, diferença e outras

Precisamos lembrar também que os *sets* não possuem *ordenação*, nem na inserção nem forçada por métodos

```python
esportes = {"volei", "basquete", "handball"}

esportes_2 = {"skate", "judo", "boxe"}

esportes_3 = set(["volei", "basquete"])
# união de conjuntos
print(esportes.union(esportes_2))

# união de conjuntos alternativa
print(esportes | esportes_2)

# interseção de conjuntos
print(esportes.intersection(esportes_3))

# interseção de conjuntos alternativa
print(esportes & esportes_3)

# diferença de conjuntos
print(esportes.difference(esportes_3))

# diferença de conjuntos alternativa
print(esportes - esportes_3)

```

### Utilização

Normalmente os conjuntos ou *set* são usados com elementos que não se repetem, pois não são aceitos repetições em seu conteúdo

Usados comumente para garantir a unicidade de conteúdo, os conjuntos podem facilmente converter uma lista com elementos repetidos para um grupo de itens únicos

```python
frutas = ["pera", "maca", "laranja", "uva", "limao", "maca", "uva"]

# para retirar repetidos sem iteração
frutas_unicas = set(frutas)

print(frutas_unicas)
```
---
[Voltar ao Topo](#m%C3%B3dulo-06)
---
## Dicionários - map

O *dicionário* é outra estrutura muito usada quando trabalhamos com dados por sua estrutura

### Declaração

Na *declaração* do tipo map também usamos *chaves* e seu conteúdo é informado sempre associado a uma chave ou "key" separado por ":" do valor que queremos guardar

```python
celular1 = {
  "marca": "Samsung",
  "modelo": "J12",
  "tela": 4.8,
  "valor": 249.99,
}
```

### Mutabilidade

Como o *map* é muito usado quando trabalhamos com dados, também é possível a modificação dos valores por meio da chave associada

Para *alterar* um valor associado a uma chave, usamos o seguinte:

```python
celular = {
  "marca": "Samsung",
  "modelo": "J12",
  "tela": 4.8,
  "valor": 249.99,
}
celular[valor] = 199.99
```

### Utilização

Os dicionários são altamente usados para trabalhar com dados comumente provenientes de bancos de dados por possuírem colunas que facilmente são associadas as suas chaves e os dados aos valores relacionados

Em casos de *integração entre sistemas* os arquivos de troca de dados, podendo ser XML, JSON ou outro, geralmente conterão a mesma estrutura em todos eles, uma chave correspondente a uma coluna de tabela e os dados contidos nelas

Com os *dicionário* tabém é possível ter dicionários dentro de dicionários assim como todos os outros tipos, listas, tuplas e conjuntos

```python
# lista de conjuntos
[
  # dados telefônicos {key: value}
	{ "mask": "+32(53)##-##-##", "cc": "BE", "cd": "Belgium", "city": "Aalst (Alost)" },
	{ "mask": "+32(3)###-##-##", "cc": "BE", "cd": "Belgium", "city": "Antwerpen (Anvers)" },
	{ "mask": "+32(63)##-##-##", "cc": "BE", "cd": "Belgium", "city": "Arlon" },
	{ "mask": "+32(67)##-##-##", "cc": "BE", "cd": "Belgium", "city": "Ath" },
]
```
---
[Volter ao Topo](#m%C3%B3dulo-06)
---
## Loop for

O *loop for* é uma estrutura de repetição, parecida com o while, muito usada quando precisamos iterar com dados

### Declaração

Sua *declaração* é muito simples e mais fácil de usar comparado ao loop while, no qual é necessário o uso de uma variável para o controle das repetições

```python
carros = ["uno", "gol", "celta"]

# com o while seria
i = 0 # controla loops
while i < len(carros): # condição
  print(carros[1])
  i = i + 1 # atualizar contagem

# com for in
for carro in carros: # única instrução
  print(carro) # bloco pra comandos

```

### Iterabilidade

Esta propriedade possibilita ao loop for percorrer todos os itens de uma estrutura que a possua

Até o momento, aprendemos a trabalhar com 4 estruturas diferentes onde todas possuam a propriedade de serem iteráveis

Com apenas uma declaração de loop for, podemos fazer a iteração por todas as estruturas já vistas, seja ela uma lista, tupla, conjunto ou dicionário

```python
carros = ["uno", "gol", "celta"] # lista
carros = ("uno", "gol", "celta") # tupla
carros = {"uno", "gol", "celta"} # conjunto

# seja qual for a estrutura funciona
for carro in carros: # única instrução
  print(carro) # bloco pra comandos

# com dicionários veremos as chaves
aluno = {
  "nome": "pedro",
  "serie": "oitavo",
  "sala": 102
  "turno": "matutino",
}
# iteragindo temos as chaves
for dado in aluno:
  print(dado)
  # pra valor seria assim
  print(aluno[dado])
```

### Utilização

Como os dicionários são bastante utilizados, para facilitar a iteração temos alguns métodos que extraem seus valores para estruturas mais simples. São eles:

> - dict.keys() - lista das chaves
> 
> - dict.values() - lista dos valores
> - dict.items() - lista de tuplas com chave e valor

Normalmente quando iteramos com um dicionário, usamos a estrutura abaixo para obter tanto a chave quanto o valor

```python
aluno = {
  "nome": "pedro",
  "serie": "oitavo",
  "sala": 102
  "turno": "matutino",
}

# for iteração com chave e valor
for chv, vlr in aluno.items():
  print(chv, vlr)

```
---
[Voltar ao Topo](#m%C3%B3dulo-06)
---





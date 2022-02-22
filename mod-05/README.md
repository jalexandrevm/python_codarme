# Módulo 05

## Índice

1. [Condições - if/elif/else](#condi%C3%A7%C3%B5es---ifelifelse)
	1. [Declaração](#declaração)
	2. [Utilização](#utilização)
2. [Repetições ou loops while](#repeti%C3%A7%C3%B5es-ou-loops-while)
	1. [Declaração](#declaração-1)
	2. [Utilização](#utilização-1)
3. [Exercícios](#exerc%C3%ADcios)
	1. [FizzBuzz](#fizzbuzz)
	2. [Calculadora](#calculadora)
	3. [Autenticação usuário](#autentica%C3%A7%C3%A3o-usu%C3%A1rio)
	4. [Soma sequência de números](#soma-sequ%C3%AAncia-de-n%C3%BAmeros)
	5. [Imprime pares](#imprime-pares)
	6. [Testar primalidade](#testar-primalidade)
	7. [Acerte o número](#acerte-o-n%C3%BAmero)


## Condições - if/elif/else

Uma estrutura que provém ao código a possibilidade de escolha de mais de um caminho a ser tomado pelo fluxo do programa

### Declaração

A estrutura é construída baseando-se na quantidade de fluxos que queremos tomar, mas basicamente podemos usar assim:

```python
if condição_1:
  bloco_códigos_1
elif condição_2:
  bloco_código_2
else:
  bloco_código_else
 
```

### Utilização

Com base na estrutura básica acima, temos:

- Caso a condição_1 seja verdadeira o bloco_códigos_1 será executado e todos os outros serão ignorados
- Caso a condição_1 esteja falsa o teste passa para a condição_2 e assim por diante até um ser verdadeiro
- Caso todas as condições estejam falsas, o bloco_código_else é executado

> Vale lembrar que os blocos else assim como o elif são opcionais

O código abaixo demonstra como podemos utilizar o if/elif/else para daterminar diferentes fluxos para nosso código

```python
idade = 15

if idade <= 10:
  print("criança")
elif idade <= 18:
  print("adolescente")
else:
  print("adulto")
```

---

[Voltar ao Topo](#m%C3%B3dulo-05)

---

## Repetições ou loops while

Esta estrutura tem como finalidade repetir um bloco de códigos enquanto uma condição for verdadeira

### Declaração

Sua declaçração é feita com o teste da condição no início, antes do bloco a ser repetido, e em seguida a condição precisa ser atualizada para o novo teste

```python
while condição:
	bloco_códigos
	atualizar_condição
```

### Utilização

Normalmente os *loops*, como chamamos as repetições, são muito usados para percorrer uma variável ou valor que possua um índice posicional

Quando usamos o *while* precisamos nos preocupar com a atualização da condição de teste dele, caso a condição não mude o loop será infinito

A forma mais básica de uso do while é para ler todos os números de uma lista para somar ou tirar a média ou até mesmo para achar o maior ou menor número

```python
lista = [9, 10, 8.5, 9.5]
soma = 0
indice = 0
tamanho_lista = len(lista)
while indice < tamanho_lista:
	soma = soma + lista[indice]
	indice = indice + 1
print("soma dos números igual a:", soma)
print("média dos números igual a:", (soma/tamanho_lista))

```

---

[Voltar ao Topo](#m%C3%B3dulo-05)

---

## Exercícios

### FizzBuzz

Esta atividade apresenta o *famoso clássico problema* usado pela programação, o ***"FizzBuzz"***

Neste problema, devemos receber do usuário um inteiro para testá-lo e informar se o mesmo pode ser dividido por:
- 3, imprimindo **"Fizz"**
- 5, imprimindo **"Buzz"**
- 15, imprimindo **"FizzBuzz"**

```python
numero = int(input("digite um número inteiro: "))
if numero % 15 == 0:
    print("FizzBuzz")
elif numero % 5 == 0:
    print("Buzz")
elif numero % 3 == 0:
    print("Fizz")

```

### Calculadora

Esta atividade pede a implementação de uma calculadora solicitando ao usuário 3 dados:

1. operador 1
2. operador 2
3. a operação que será feita

A calculadora deve imprimir **“Não é possível realizar divisão por
zero!”** caso o operador 2 seja zero **e** a operação seja a *divisão*

```python
operando1 = float(input("digite o primeiro número: "))
operando2 = float(input("digite o segundo número: "))
operador = input("qual a operação? (+ - * /) ")
resultado = 0
if operador == "/":
    if operando2 != 0:
        resultado = operando1/operando2
    else:
        print("Não é possível realizar divisão por zero!")
        quit(0)
elif operador == "*":
    resultado = operando1*operando2
elif operador == "-":
    resultado = operando1-operando2
elif operador == "+":
    resultado = operando1+operando2
else:
    quit(0)
print(resultado)

```

### Autenticação usuário

Esta atividade pede ao usuário o seu usuário e a senha para a autenticação de um serviço

O programa deve informar se:

- Autenticação foi bem sucedida
- Usuário existe ou não
- Senha está correta ou não

Para esta atividade os valores de teste de *usuário* e *senha* são constantes dentro do próprio programa

```python
USUARIO = "admin"
SENHA = "741258"

nome_user = input("digite o nome de usuário: ")
senha_user = input("digite sua senha: ")

if nome_user.__eq__(USUARIO) and senha_user.__eq__(SENHA):
    print("Autenticação Bem Sucedida")
elif not nome_user.__eq__(USUARIO):
    print("nome de usuário não existe")
elif not senha_user.__eq__(SENHA):
    print("senha do usuário incorreta")

```

### Soma sequência de números

Nesta ativiadade usamos o loop *while* para **somar** todos os inteiros positivos a partir do 1 até um *número* fornecido pelo *usuário*

```python
soma = 0
num1 = 1
num2 = float(input("digite o número final: "))
while num1 <= num2:
    soma += num1
    num1 += 1
print(soma)

```

### Imprime pares

Agora vamos imprimir apenas os números **pares** do intervalo entre o 1 e o número informado pelo *usuário*

```python
num1 = 1
num2 = int(input("digite um número final: "))
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1

```

### Testar primalidade

Nesta atividade, usamos o loop *while* para testar se um número passado pelo usuário é **primo** ou não

```python
numprimo = int(input("digite um número inteiro: "))

divisor = 2
primo = True

while divisor < numprimo and primo:
    if (numprimo % divisor == 0):
        primo = False
    divisor += 1

print("primo" if primo else "não primo")

```

### Acerte o número

Nesta atividade usamos o loop *while* para dar ao usuário *3 tentativas* para acertar o **número secreto**

No *próprio programa* declaramos como uma *constante* um valor qualquer para ser **descoberto**

Caso o usuário *erre* 3 vezes deve ser impresso **"perdeu"** e caso *acerte* imprimir **"ganhou"**

```python
num_sorte = 7
perdeujogo = True
tentativa = 1
num_informado = 0
while tentativa <= 3 and perdeujogo:
    num_informado = int(input("tente acertar o número secreto: "))
    if num_sorte == num_informado:
        perdeujogo = False
    elif num_informado < num_sorte:
        print("menor")
    elif num_informado > num_sorte:
        print("maior")
    tentativa += 1
print("perdeu" if perdeujogo else "ganhou")

```

---

[Voltar ao Topo](#m%C3%B3dulo-05)

---



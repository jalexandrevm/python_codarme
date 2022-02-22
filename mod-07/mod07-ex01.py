def e_primo(num):
  if num * num < 2:
    return False
  divisor = 2
  primoStatus = True
  while divisor < num and primoStatus:
      if (num % divisor == 0):
          primoStatus = False
      divisor += 1
  return primoStatus

# função apenas para testar o código
def main():
  print(e_primo(-1))
  print(e_primo(-2))
  print(e_primo(0))
  print(e_primo(5))

main()

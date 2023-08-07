from sys import stdin, stdout
def main():
  minstack = []
  quantity = int(input())
  for i in range(quantity):
    comando = stdin.readline().rstrip()
    if 'PU' in comando:
      comando , valor= comando.split()
      valor = int(valor)
      minimo = valor if not minstack else min(valor, minstack[-1][1])
      minstack.append((valor,minimo))
    elif not minstack:
      stdout.write("EMPTY\n")
    elif 'M' in comando:
      stdout.write(f"{minstack[-1][1]}\n")
    else:
      minstack.pop()
main()
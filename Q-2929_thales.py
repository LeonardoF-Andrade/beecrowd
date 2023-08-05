def min_stack(pilha):
  if len(pilha) == 0:
    return "EMPTY"
  else:
    return min(pilha)


def main():
  n = int(input())
  pilha = []
  for i in range(n):
    comando = input().split()
    if comando[0] == "PUSH":
      pilha.append(int(comando[1]))
    elif comando[0] == "POP":
      if not pilha:
        print('EMPTY')
      else: pilha.pop()
    elif comando[0] == "MIN":
      print(min_stack(pilha))


if __name__ == "__main__":
  main()
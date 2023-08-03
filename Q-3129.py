class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lis:
    def ini(self):
        self.head = None

    def li(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            aux = self.head
            while aux.next is not None:
                aux = aux.next
            aux.next = new_node

n = int(input())

lista = Lis()
lista.ini()

R = 0
D = 0

def analisa(lista, data):
    global R, D
    aux = lista.head
    if aux.next is None:
        D+=1
    else:
        aux = lista.head
        cont = 0
        while aux is not None:
            if aux.data == data and aux.next is not None:
                R+=1
                cont+=1
            elif aux.next is None and cont == 0:
                D+=1
            aux = aux.next


for i in range(n):
    f = int(input())
    lista.li(f)
    analisa(lista,f)

print(D,"\n",R, sep="")


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
    if lista.next is None:
        D+=1
    else:
        if data == lista.head:
            R+=1
        else:
            aux = lista.head
            while aux.next is not None:
                if aux.data == data:
                    R+=1
                elif aux.next == None:
                    D+=1


for i in range(n):
    f = int(input())
    lista.li(f)
    analisa(lista,f)



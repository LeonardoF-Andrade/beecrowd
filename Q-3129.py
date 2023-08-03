R = 0
D = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lis:

    def ini(self):
        self.head = None

    def li(self, data):
        global R, D
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            D+=1
        else:
            aux = self.head
            if data == aux.data:
                R+=1
            else:
                while aux.next is not None:
                    if aux.data == data:
                        R+=1
                    aux = aux.next
                if aux.data == data:
                    R+=1
                else:
                    aux.next = new_node
                    D+=1

n = int(input())

lista = Lis()
lista.ini()



for i in range(n):
    f = int(input())
    lista.li(f)


print(D,"\n",R, sep="")


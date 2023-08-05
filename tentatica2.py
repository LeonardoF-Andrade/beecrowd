while True:
    i = input()
    if i != '':
        break
i = int(i)
# Definindo as cores dos nós da árvore rubro-negra
RED = "RED"
BLACK = "BLACK"

class Node:
    def __init__(self, value, color, left=None, right=None,parent = None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.root = None
    def _fix_insert(self, node):
        while self._is_red(node.parent) and node.parent.parent:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and self._is_red(uncle):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and self._is_red(uncle):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_left(node.parent.parent)

        self.root.color = BLACK

    def insert(self, value):
        new_node = Node(value, RED)
        if not self.root:
            self.root = new_node
            self.root.color = BLACK  # A raiz sempre deve ser preta
            return

        parent = None
        current = self.root

        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _is_red(self, node):
        return node and node.color == RED

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK


    def find_min(self,node):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left

        return current
    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Caso 1: Nó sem filhos ou apenas um filho
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Caso 2: Nó com dois filhos
            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursively(node.right, successor.value)

        # Realiza as operações de reequilíbrio após a remoção
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

presentes = []
it = 0
busca = RedBlackTree()
while it < i:
    termos = input()
    if termos == "MIN":
        if not presentes:
            print('EMPTY')
        else: print(busca.find_min(busca.root).value)
    elif termos == "POP":
        if not presentes:
            print('EMPTY')
        else:
            busca.delete(presentes[-1])
            del presentes[-1]

    elif 'PUSH' in termos:
        valor = int(termos[4:])
        presentes.append(valor)
        busca.insert(valor)
    it =it+1

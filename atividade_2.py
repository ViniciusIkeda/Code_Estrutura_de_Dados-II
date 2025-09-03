from graphviz import Digraph
import random

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        def _insert(node, valor):
            if not node:
                return Node(valor)
            if valor < node.valor:
                node.left = _insert(node.left, valor)
            elif valor > node.valor:
                node.right = _insert(node.right, valor)
            return node
        self.root = _insert(self.root, valor)

    def search(self, valor):
        def _search(node, valor):
            if not node:
                return False
            if valor == node.valor:
                return True
            elif valor < node.valor:
                return _search(node.left, valor)
            else:
                return _search(node.right, valor)
        return _search(self.root, valor)

    def delete(self, valor):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, valor):
            if not node:
                return node
            if valor < node.valor:
                node.left = _delete(node.left, valor)
            elif valor > node.valor:
                node.right = _delete(node.right, valor)
            else:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.valor = temp.valor
                node.right = _delete(node.right, temp.valor)
            return node
        self.root = _delete(self.root, valor)

    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def depth(self, valor):
        def _depth(node, valor, d):
            if not node:
                return -1
            if valor == node.valor:
                return d
            elif valor < node.valor:
                return _depth(node.left, valor, d+1)
            else:
                return _depth(node.right, valor, d+1)
        return _depth(self.root, valor, 0)

    def visualize(self, filename):
        dot = Digraph()
        def add_nodes_edges(node):
            if node:
                dot.node(str(node.valor))
                if node.left:
                    dot.edge(str(node.valor), str(node.left.valor))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(node.valor), str(node.right.valor))
                    add_nodes_edges(node.right)
        add_nodes_edges(self.root)
        dot.render(filename, format='png', cleanup=True)
        print(f"Árvore salva como {filename}.png")

if __name__ == "__main__":
    print("Árvore com valores fixos:")
    bst = BST()
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    for v in valores_fixos:
        bst.insert(v)
    bst.visualize("arvore_fixa")

    print("Busca pelo valor 45:", bst.search(45))
    print("Removendo o valor 30...")
    bst.delete(30)
    bst.visualize("arvore_fixa_removido_30")

    print("Inserindo o valor 35...")
    bst.insert(35)
    bst.visualize("arvore_fixa_inserido_35")

    print("Altura da árvore:", bst.height())
    print("Profundidade do nó 45:", bst.depth(45))

    print("\nÁrvore com valores randômicos:")
    bst_rand = BST()
    valores_rand = random.sample(range(1, 201), 15)
    print("Valores randômicos:", valores_rand)
    for v in valores_rand:
        bst_rand.insert(v)
    bst_rand.visualize("arvore_randomica")
    print("Altura da árvore randômica:", bst_rand.height())
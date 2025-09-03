import random
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        _postorder(self.root)
        return result

    def visualize(self):
        # Visualização simples em texto (em ordem de níveis)
        lines = []
        def _visualize(node, level=0):
            if node is not None:
                _visualize(node.right, level + 1)
                lines.append('    ' * level + f'{node.value}')
                _visualize(node.left, level + 1)
        _visualize(self.root)
        return '\n'.join(lines)

    def to_graphviz(self, filename='tree'):
        dot = Digraph()
        def add_nodes_edges(node):
            if node:
                dot.node(str(node.value))
                if node.left:
                    dot.edge(str(node.value), str(node.left.value))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(node.value), str(node.right.value))
                    add_nodes_edges(node.right)
        add_nodes_edges(self.root)
        dot.render(filename, format='png', cleanup=True)
        print(f"Árvore salva como {filename}.png")
        return filename + '.png'

# Árvore com valores fixos
fixed_values = [55, 30, 80, 20, 45, 70, 90]
fixed_tree = BinaryTree()
for v in fixed_values:
    fixed_tree.insert(v)

print("Árvore Binária com Valores Fixos:")
print(fixed_tree.visualize())
print("\nTravessia In-Order (Esquerda-Raiz-Direita):", fixed_tree.inorder())
print("Travessia Pre-Order (Raiz-Esquerda-Direita):", fixed_tree.preorder())
print("Travessia Post-Order (Esquerda-Direita-Raiz):", fixed_tree.postorder())

fixed_tree.to_graphviz('arvore_fixa')

print("\n" + "="*50 + "\n")

# Árvore com valores randômicos
random_values = random.sample(range(10, 100), 10)
random_tree = BinaryTree()
for v in random_values:
    random_tree.insert(v)

print("Árvore Binária com Valores Randômicos:")
print(random_tree.visualize())
print("\nTravessia In-Order (Esquerda-Raiz-Direita):", random_tree.inorder())
print("Travessia Pre-Order (Raiz-Esquerda-Direita):", random_tree.preorder())
print("Travessia Post-Order (Esquerda-Direita-Raiz):", random_tree.postorder())

random_tree.to_graphviz('arvore_randomica')
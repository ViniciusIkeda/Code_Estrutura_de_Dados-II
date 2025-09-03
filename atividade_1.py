from graphviz import Digraph
import random

# Classe para representar um nó da árvore binária
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Função para construir a árvore da expressão fixa
def build_fixed_tree():
    # ((7 + 3) (5 - 2))
    left = Node('*',
                Node('+', Node('7'), Node('3')),
                Node('-', Node('5'), Node('2')))
    # (10 * 20)
    right = Node('*', Node('10'), Node('20'))
    # ((...) / (...))
    root = Node('/', left, right)
    return root

# Função para gerar uma expressão aritmética aleatória
def generate_random_expression():
    operators = ['+', '-', '*', '/']
    operands = [str(random.randint(1, 20)) for _ in range(3)]
    op1, op2 = random.sample(operators, 2)
    # Exemplo: (a op1 b) op2 c
    expr = f"({operands[0]} {op1} {operands[1]}) {op2} {operands[2]}"
    return expr

# Função para construir árvore a partir de expressão simples: (a op1 b) op2 c
def build_random_tree(expr):
    # Supondo formato: (a op1 b) op2 c
    expr = expr.replace('(', '').replace(')', '')
    parts = expr.split()
    left = Node(parts[1], Node(parts[0]), Node(parts[2]))
    root = Node(parts[3], left, Node(parts[4]))
    return root

# Função para visualizar a árvore usando graphviz
def visualize_tree(root, filename):
    dot = Digraph()
    def add_nodes_edges(node):
        if node:
            dot.node(str(id(node)), node.value)
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes_edges(node.right)
    add_nodes_edges(root)
    dot.render(filename, format='png', cleanup=True)
    print(f"Árvore salva como {filename}.png")

if __name__ == "__main__":
    # Árvore fixa
    fixed_tree = build_fixed_tree()
    visualize_tree(fixed_tree, "arvore_fixa")

    # Árvore randômica
    expr = generate_random_expression()
    print("Expressão randômica gerada:", expr)
    random_tree = build_random_tree(expr)
    visualize_tree(random_tree, "arvore_randomica")
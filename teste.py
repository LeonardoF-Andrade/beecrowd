from intervaltree import IntervalTree

# Criando uma Árvore de Intervalos
timeline = IntervalTree()

# Adicionando eventos à Árvore de Intervalos
timeline.addi(1, 10, "Show 1")
timeline.addi(20, 30, "Show 2")
timeline.addi(40, 50, "Show 3")

# Imprimindo a árvore de forma simplificada
def print_interval_tree(tree):
    for interval in tree:
        print(f"{interval.begin}-{interval.end}: {interval.data}")

print("Árvore de Intervalos:")
print_interval_tree(timeline)

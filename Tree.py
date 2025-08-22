# Построение дерева проекта с красивым выводом
import os

# from os.path import isdir
from rich.console import Console
from rich.tree import Tree


def build_tree(path, tree):
    for entry in sorted(os.listdir(path)):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            subtree = tree.add(f" {entry}")
            build_tree(full_path, subtree)
        else:
            tree.add(f" {entry}")


def visualize_project_structure(root_path):
    console = Console()
    tree = Tree(f" Пpoekт: {os.path.basename(root_path)}")
    build_tree(root_path, tree)
    console.print(tree)


visualize_project_structure(r"d:\Source\1s\Externals")

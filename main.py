from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Baum:
    def __init__(self, root_node: Node):
        self.root: Node = root_node


# Beispiel
bst = Baum(Node(5))

from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Baum:
    def __init__(self, root_node: Node):
        self.root: Node = root_node

    def traverse(self, node: Optional[Node], items: list[int]) -> None:
        """
        Rekursive Methode die die Nodes des Baums durchgeht und
        deren Werte zu der Liste `items` hinzufügt.
        """
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

    def __repr__(self):
        items: list[int] = []
        self.traverse(self.root, items)
        return str(items)

    def insert(self, value: int, node: Optional[Node] = None) -> Node:
        """
        Rekursive Methode um einen neuen Wert in den Suchbaum hinzuzufügen
        """
        if node is None:
            node = self.root

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)

        # Wenn value == node.value ist, kein Duplikat erzeugen

        return node


# Beispiel
bst = Baum(Node(5))
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(2)
bst.insert(99)
bst.insert(0)

print(bst)

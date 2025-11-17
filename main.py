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

    def get_height(self, root: Optional[Node] = None) -> int:
        """
        Rekursive Methode um die Höhe des Suchbaums zu errechnen.
        Ein Suchbaum mit einer einzigen Node zählt hier als Höhe 1.
        """

        if root is None:
            root = self.root

        # Ein Suchbaum mit einer einzigen Node zählt hier als Höhe 1.
        if root.left is None and root.right is None:
            return 1

        # Berechnen der Höhen der Äste links und rechts
        left_height = self.get_height(root.left) if root.left else 0
        right_height = self.get_height(root.right) if root.right else 0

        # Die Gesamthöhe des Baums entspricht dann der Höhe des
        # längsten Astes + 1 (+ die root-node)
        return max(left_height, right_height) + 1

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

print(bst.get_height())

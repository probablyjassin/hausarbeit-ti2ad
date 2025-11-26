"""
Enthält die tatsächlichen Implementierungen des Binären Suchbaums und des AVL-Baums
entsprechend der Aufgabenstellung. Sie wurden in diese Datei verlagert um
die Struktur des Projekts übersichtlich zu halten. `main.py` importiert die Klassen
`Node`, `Baum` und `AVLBaum` aus dieser Datei.
"""

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

    def breadth_traverse(self) -> list[list[Optional[int]]]:
        res: list[list[Optional[int]]] = []
        queue: list[Optional[Node]] = []
        queue.append(self.root)
        while queue:
            level: list[Optional[int]] = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.value if node else None)
                queue.append(node.left if node else None)
                queue.append(node.right if node else None)

            if any(type(entry) == int for entry in level):
                res.append(level)
            else:
                # Wir entfernen die überflüssigen 'None's am Ende der Repräsentation
                while res[-1][-1] == None:
                    res[-1].pop()
                break
        return res

    def __repr__(self):
        level_repr: list[list[Optional[int]]] = self.breadth_traverse()
        representation: str = ""
        for level in level_repr:
            for value in level:
                representation += f"{value} "
            representation += "\n"
        return representation

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


class AVLBaum(Baum):
    def get_balance_factor(self, node: Optional[Node]) -> int:
        """
        Berechnet den Gleichgewichts-Faktor eines Knotens.
        Gleichgewichts-Faktor = Höhe(linker Teilbaum) - Höhe(rechter Teilbaum)
        """
        if node is None:
            return 0

        left_height = self.get_height(node.left) if node.left else 0
        right_height = self.get_height(node.right) if node.right else 0

        return left_height - right_height

    def rotate_right(self, z: Node) -> Node:
        """Rechtsdrehung um Knoten z"""

        if not z.left:
            raise ValueError("Für Rechtsdrehung ausgewählte Node hat keine linke Node")

        y = z.left
        T3 = y.right

        # Rotation durchführen
        y.right = z
        z.left = T3

        return y

    def rotate_left(self, z: Node) -> Node:
        """Linksdrehung um Knoten z"""

        if not z.right:
            raise ValueError("Für Linksdrehung ausgewählte Node hat keine rechte Node")

        y = z.right
        T2 = y.left

        # Rotation durchführen
        y.left = z
        z.right = T2

        return y

    def insert(self, value: int, node: Optional[Node] = None) -> Node:
        """
        AVL-Insert: Fügt einen Wert ein und balanciert den Baum
        """
        # Erstes Einfügen (root setzen)
        if node is None:
            node = self.root

        # Standard BST Insert
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = self.insert(value, node.right)
        else:
            # Duplikat, nichts tun
            return node

        # Balance-Faktor berechnen
        balance = self.get_balance_factor(node)

        # Fall 1: Links-Links (Right Rotation)
        if balance > 1 and node.left and value < node.left.value:
            return self.rotate_right(node)

        # Fall 2: Rechts-Rechts (Left Rotation)
        if balance < -1 and node.right and value > node.right.value:
            return self.rotate_left(node)

        # Fall 3: Links-Rechts (Left-Right Rotation)
        if balance > 1 and node.left and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Fall 4: Rechts-Links (Right-Left Rotation)
        if balance < -1 and node.right and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

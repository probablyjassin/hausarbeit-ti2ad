"""
Hier wird das Programm ausgeführt.
Das Skript greift auf die anderen `.py`-Dateien in diesem Verzeichnis zu und
erfüllt die Aufgaben aus der Aufgabenstellung.
"""

from baum import Node, Baum, AVLBaum
from daten import DATASET

# Aufgabe 4 - Datensatz mit 10 zufälligen Schlüsseln
# (erzeugt via `[randint(0, 100) for _ in range(10)]`)

print("Aufgabe 4:")

numbers: list[int] = [69, 76, 68, 16, 51, 84, 7, 18, 49, 53]
test_bst = Baum(Node(numbers[0]))
for value in numbers[1:]:
    test_bst.insert(value)

print(test_bst)

print("-------------")

print("Erstelle BSTs mit den Einträgen aus dem Dataset...")

all_bsts: list[Baum] = []

for entry in DATASET:
    bst = Baum(Node(entry[0]))
    for value in entry[1:]:
        bst.insert(value)
    all_bsts.append(bst)

print("Erstelle AVL-BSTs mit den Einträgen aus dem Dataset...")

all_avl_bsts: list[AVLBaum] = []

for entry in DATASET:
    avl_bst = AVLBaum(Node(entry[0]))
    for value in entry[1:]:
        avl_bst.insert(value)
    all_avl_bsts.append(avl_bst)

print("fertig...\n-----------")

print("Durchschnittliche Höhe der BSTs:")
print(sum([tree.get_height() for tree in all_bsts]) / len(all_bsts))

print("Vergleich: Durchschnittliche Höhe der AVL BSTs:")
print(sum([tree.get_height() for tree in all_avl_bsts]) / len(all_avl_bsts))

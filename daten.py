"""
Aufgabe 5 erfordert das Erzeugen von
100 Datensätzen von jeweils 20 zufällig erzeugten ganzzahligen Schlüsseln.
daten.py prüft, ob in `daten.json` bereits ein solcher Datensatz erzeugt wurde.
Falls nicht, wird dieser neu erzeugt, und in beiden Fällen wird der Datensatz in die Konstante
`DATASET` an `main.py` exportiert.
"""

import os
import json
from random import randint

DATASET: list[list[int]] = []

if not os.path.exists("./daten.json"):
    for _ in range(100):
        DATASET.append([randint(0, 100) for _ in range(20)])
    with open("./daten.json", "w") as f:
        json.dump(DATASET, f)
else:
    with open("./daten.json", "r") as f:
        read_dataset: list[list[int]] = json.load(f)
        for entry in read_dataset:
            DATASET.append(entry)

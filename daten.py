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

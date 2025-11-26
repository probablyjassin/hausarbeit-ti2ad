---
# Binäre Suchbäume
---

Für die Programmierung wurde Python `v3.12.10` genutzt,
allerdings ist eine beliebige Version ab `v3.9.0` kompatibel.

Die verwendete Entwicklungsumgebung ist Visual Studio Code.
Es liegt ein `.vscode`-Verzeichnis für die Konfiguration bei,
dieses Einzubinden ist aber vollständig optional, da es sich dabei nur um sog. Typehints handelt.
Die Ausführbarkeit des Projekts ist davon nicht betroffen.

Type Hints/Type Annotations sind ein optionales Python-Feature (seit Python 3.5),
das genutzt werden kann, um Typ-Informationen zu dokumentieren.
Diese Annotationen haben keinen Einfluss auf die Laufzeit des Programms.

```py
# Beispiel
def breadth_traverse(self) -> list[list[Optional[int]]]:
   "..."
```

Das Installieren von externen Abhängigkeiten ist nicht erforderlich,
denn das Projekt nutzt nur die Standard-Library von Python.
(os, json, typing, random)

### Struktur

`daten.py` - Aufgabe 5 erfordert das Erzeugen von
100 Datensätzen von jeweils 20 zufällig erzeugten ganzzahligen Schlüsseln.
daten.py prüft, ob in `daten.json` bereits ein solcher Datensatz erzeugt wurde.
Falls nicht, wird dieser neu erzeugt, und in beiden Fällen wird der Datensatz in die Konstante
`DATASET` an `main.py` exportiert.

`baum.py` - enthält die tatsächlichen Implementierungen des Binären Suchbaums und des AVL-Baums
entsprechend der Aufgabenstellung. Sie wurden in diese Datei verlagert um
die Struktur des Projekts übersichtlich zu halten. `main.py` importiert die Klassen
`Node`, `Baum` und `AVLBaum` aus dieser Datei.

`main.py` - hier wird das Programm ausgeführt.
Das Skript greift auf die anderen `.py`-Dateien in diesem Verzeichnis zu und
erfüllt die Aufgaben aus der Aufgabenstellung.

### Ausführung

`$ python main.py`

Die Ausgaben werden via `print()`-Statements in die normale,
Standardmäßige Ausgabe des Terminals (stdout) ausgegeben.

---

## Aufgabenstellung für die Hausarbeit

**Aufgabenstellung**

1. Beschreiben Sie den Algorithmus zur Erzeugung von natürlichen binären Suchbäumen
2. Diskutieren Sie wesentliche Eigenschaften und Voraussetzung der Konstruktion
3. Schreiben Sie einen Programmcode, welcher einen natürlichen binären Suchbaum erzeugt und dessen Höhe berechnet
4. Erzeugen Sie einen Datensatz von 10 zufällig erzeugten ganzzahligen Schlüsseln.
   Finden Sie eine Möglichkeit, diesen korrekt in seiner Vater-Sohn-Beziehung auszugeben
5. Erzeugen Sie 100 Datensätze von jeweils 20 zufällig erzeugten ganzzahligen Schlüsseln.
   Berechnen Sie jeweils die Höhe der erzeugten Suchbäume und bilden Sie den Durch-
   schnitt dieser Höhen. Vergleichen Sie das Ergebnis mit dem eines AVL-Baumes.

## Abgegeben werden muss:

6. Eine (höchstens sechsseitige) Beschreibung der Algorithmen, des Problems und der Lösung
7. Eine Programmbeschreibung mit Quellcode (Die Programm-Kommentare sind in
   deutscher Sprache zu halten)
8. Ein lauffähiges Programm, das entweder unter Windows (Version 10), MacOS oder
   Linux ohne weitere Manipulationen oder Integration in eine IDE (zB Eclipse) ges-
   tartet werden kann.
9. Als Programmiersprachen sind zugelassen: Python, Java, C, C++

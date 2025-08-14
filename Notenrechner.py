## 1 = Sehr gut 2 = Gut 3 = Befriedigend 4 = Ausreichend 5 = Mangelhaft 6 = Ungenügend

### 10 kunden 4 bewertungsfelder Noten 1-6
### Funktion Leistung  öko    Preis
###     2   	3   	4   	2
###     2   	2   	3   	1
###     4   	4   	5   	4
###     1   	1   	4   	2
###     2   	1   	3   	2
###     3   	2   	3   	3
###     2   	1   	5   	3
###     2   	2   	3   	1
###     2   	2   	5   	3
###     2   	2   	4   	2
###	Wie viel Prozent haben im Durchschnitt der vier Einzelbewertungen gut und besser bewertet?
### Wie viel Prozent haben im Durchschnitt der vier Einzelbewertungen ausreichend und schlechter bewertet?
### Welche Durchschnittsnote für die Berücksichtigung ökologischer Aspekte (Öko) wurde in den Produkten vergeben?

Notendict = {
    "Kunde 1": [2, 3, 4, 2],
    "Kunde 2": [2, 2, 3, 1],
    "Kunde 3": [4, 4, 5, 4],
    "Kunde 4": [1, 1, 4, 2],
    "Kunde 5": [2, 1, 3, 2],
    "Kunde 6": [3, 2, 3, 3],
    "Kunde 7": [2, 1, 5, 3],
    "Kunde 8": [2, 2, 3, 1],
    "Kunde 9": [2, 2, 5, 3],
    "Kunde 10": [2, 2, 4, 2]
}

def gut_und_besser():
    count = 0
    total = 0
    for kunde, noten in Notendict.items():
        if sum(noten) / len(noten) <= 2:  # Durchschnittsnote gut oder besser
            count += 1
        total += 1
    return (count / total) * 100

def ausreichend_und_schlechter():
    count = 0
    total = 0
    for kunde, noten in Notendict.items():
        if sum(noten) / len(noten) >= 4:  # Durchschnittsnote ausreichend oder schlechter
            count += 1
        total += 1
    return (count / total) * 100

def durchschnittsnote_oeko():
    total_oeko = 0
    count = 0
    for kunde, noten in Notendict.items():
        total_oeko += noten[2]  # Öko ist das dritte Element in der Liste
        count += 1
    return total_oeko / count

print(f"{gut_und_besser():.2f}% der Kunden haben im Durchschnitt gut oder besser bewertet.")
print(f"{ausreichend_und_schlechter():.2f}% der Kunden haben im Durchschnitt ausreichend oder schlechter bewertet.")
print(f"Die Durchschnittsnote für die Berücksichtigung ökologischer Aspekte (Öko) beträgt {durchschnittsnote_oeko():.2f}.")
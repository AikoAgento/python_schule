def get_float(prompt):
    """Eingabe abfragen, Kommas in Punkte umwandeln und validieren."""
    while True:
        value = input(prompt).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

def get_int(prompt):
    """Eingabe einer ganzen Zahl abfragen und validieren."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Ungültige Eingabe. Bitte eine positive ganze Zahl eingeben.")

print("Umsatzhalbjahresrechner")
anzahl_halbjahre = get_int("Wie viele Halbjahre sollen berechnet werden? ")

# Umsätze einlesen
branchen = [get_float(f"Branchenumsatz Halbjahr {i+1}: ") for i in range(anzahl_halbjahre)]
firmen   = [get_float(f"Firmenumsatz Halbjahr {i+1}: ") for i in range(anzahl_halbjahre)]

# Relativer Marktanteil
marktanteile = [(f / b) * 100 for f, b in zip(firmen, branchen)]

# Prozentuale Steigerungen (von Halbjahr i zu i+1)
steigerungen = [
    ((marktanteile[i] - marktanteile[i-1]) / marktanteile[i-1]) * 100
    for i in range(1, anzahl_halbjahre)
]

# Tabelle erstellen
# Werte vorbereiten
rows = []
rows.append(["Halbjahr", "Marktanteil %", "Steigerung %"])

for i in range(anzahl_halbjahre):
    ma_text = f"{marktanteile[i]:.2f}%"
    st_text = f"{steigerungen[i-1]:.2f}%" if i > 0 else "-"
    rows.append([str(i+1), ma_text, st_text])

# Spaltenbreiten dynamisch ermitteln
col_widths = [max(len(row[col]) for row in rows) for col in range(len(rows[0]))]

# Ausgabe
print("\nErgebnisse:")
for r, row in enumerate(rows):
    formatted = []
    for col_index, val in enumerate(row):
        if r == 0:  # Überschriften linksbündig
            formatted.append(val.ljust(col_widths[col_index]))
        else:  # Zahlen rechtsbündig
            if col_index == 0:
                formatted.append(val.rjust(col_widths[col_index]))  # Halbjahr-Zahl
            else:
                formatted.append(val.rjust(col_widths[col_index]))  # Prozentwerte
    line = "  ".join(formatted)
    if r == 1:
        print("-" * len(line))
    print(line)
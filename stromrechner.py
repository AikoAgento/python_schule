# volllastverbrauch W/h
# leerlaufverbrauch W/h
# teillastverbrauch = (volllastverbrauch / 2) + (leerlaufverbrauch / 2)
# Strompreis = input
# kWh = 1000 W
# Jahr = 8760 Stunden

Strompreis = float(input("Strompreis in Euro pro kWh: ").replace(",", "."))
Volllastverbrauch = float(input("Volllastverbrauch in W/h: ").replace(",", "."))
Leerlaufverbrauch = float(input("Leerlaufverbrauch in W/h: ").replace(",", "."))
Teillastverbrauch = (Volllastverbrauch / 2) + (Leerlaufverbrauch / 2)
kWh = 1000
Jahr = 8760

Volllastjahresverbrauch = Volllastverbrauch * Jahr / kWh
Leerlaufjahresverbrauch = Leerlaufverbrauch * Jahr / kWh
Teillastjahresverbrauch = Teillastverbrauch * Jahr / kWh

KostenVolllast = Volllastjahresverbrauch * Strompreis
KostenLeerlauf = Leerlaufjahresverbrauch * Strompreis
KostenTeillast = Teillastjahresverbrauch * Strompreis
halbvollhalbteillast = KostenVolllast / 2 + KostenTeillast / 2

print(f"Kosten bei Volllast: {KostenVolllast:.2f} Euro")
print(f"Kosten bei Leerlauf: {KostenLeerlauf:.2f} Euro")
print(f"Kosten bei Teillast: {KostenTeillast:.2f} Euro")
print(f"Kosten bei halber voll halber Teillast: {halbvollhalbteillast:.2f} Euro")
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



print("\033[33m Rechnung für Volllast Kosten\033[0m")
print(f"{Volllastjahresverbrauch} kWh = {Volllastverbrauch} W * {Jahr} / {kWh}")
print(f"{KostenVolllast} € = {Volllastjahresverbrauch} kWh * {Strompreis} €")
print("\033[4m    Ergebniss    \033[0m")
print(f" \033[31m Kosten bei Volllast: \033[32m\033[4m {KostenVolllast:.2f}\033[0m\033[31m Euro \033[0m")
print("")
print("\033[33m Rechnung für Leerlauf Kosten\033[0m")
print(f"{Leerlaufjahresverbrauch} kWh = {Leerlaufverbrauch} W * {Jahr} / {kWh}")
print(f"{KostenLeerlauf} € = {Leerlaufjahresverbrauch} kWh * {Strompreis} €")
print("\033[4m    Ergebniss\033[0m")
print(f" \033[31m Kosten bei Leerlauf: \033[32m\033[4m {KostenLeerlauf:.2f}\033[0m\033[31m Euro \033[0m")
print("")
print("\033[33m Rechnung für Teillast Kosten\033[0m")
print(f"{Teillastjahresverbrauch} kWh = {Teillastverbrauch} W * {Jahr} / {kWh}")
print(f"{KostenTeillast} € = {Teillastjahresverbrauch} kWh * {Strompreis} €")
print("\033[4m    Ergebniss\033[0m")
print(f" \033[31m Kosten bei Teillast: \033[32m\033[4m {KostenTeillast:.2f}\033[0m\033[31m Euro \033[0m")
print("")
print("\033[33m Rechnung für halb Voll- halb Teil-last\033[0m")
print(f"{halbvollhalbteillast} € = ({KostenVolllast} € / 2) + ({KostenTeillast} € / 2)")
print("\033[4m    Ergebniss\033[0m")
print(f"\033[31m Kosten bei halber voll halber Teillast: \033[32m\033[4m {halbvollhalbteillast:.2f}\033[0m\033[31m Euro \033[0m")
print("")
print("Zusammengefasst")
print(f"Kosten bei Volllast: {KostenVolllast:.2f} Euro \033[0m")
print(f"Kosten bei Leerlauf: {KostenLeerlauf:.2f} Euro \033[0m")
print(f"Kosten bei Teillast: {KostenTeillast:.2f} Euro \033[0m")
print(f"Kosten bei halber voll halber Teillast: {halbvollhalbteillast:.2f} Euro \033[0m")
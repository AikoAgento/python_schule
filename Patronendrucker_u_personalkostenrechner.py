#           Gerätekosten    Patronenwechsel Papierfüllung   Verbrauch_in_cent   Verbrauchskosten    Geräte_u_Verbrauchskosten   Pers.kosten_PW  Pers.kosten_PF  Pers.kosten Ges.Kosten
# System A  160€            69              50              7,7
# System B  190€75          75              40              9,3
# System C  200€            82              60              10,0
# System D  210€            52              30              8,1
# System E  280€            37              30              6,1
# System F  350€            20              15              5,7
# PW = Patronenwechsel , PF = Papierfüllungen
#
# Hinweise
# Testberechnung für 15000 Seiten (Blätter)
# Zeitkalkulation für einen Patronenwechsel: 5 Minuten
# Zeitkalkulation für eine Papierfüllung: 3 Minuten
# Personalkostenkalkulationssatz / Stunde 28€

# Daten aus Kommentar
systeme = [
    {"name": "A", "geraetekosten": 160, "patronenwechsel": 69, "papierfuellung": 50, "verbrauch_seite_cent": 7.7},
    {"name": "B", "geraetekosten": 190.75, "patronenwechsel": 75, "papierfuellung": 40, "verbrauch_seite_cent": 9.3},
    {"name": "C", "geraetekosten": 200, "patronenwechsel": 82, "papierfuellung": 60, "verbrauch_seite_cent": 10.0},
    {"name": "D", "geraetekosten": 210, "patronenwechsel": 52, "papierfuellung": 30, "verbrauch_seite_cent": 8.1},
    {"name": "E", "geraetekosten": 280, "patronenwechsel": 37, "papierfuellung": 30, "verbrauch_seite_cent": 6.1},
    {"name": "F", "geraetekosten": 350, "patronenwechsel": 20, "papierfuellung": 15, "verbrauch_seite_cent": 5.7},
]

seiten = 15000
pk_satz = 28  # €/h
zeit_pw = 5   # min
zeit_pf = 3   # min

def berechne_kosten(system):
    verbrauchskosten = seiten * system["verbrauch_seite_cent"] / 100
    geraet_und_verbrauch = system["geraetekosten"] + verbrauchskosten
    pers_pw = system["patronenwechsel"] * zeit_pw / 60 * pk_satz
    pers_pf = system["papierfuellung"] * zeit_pf / 60 * pk_satz
    pers_gesamt = pers_pw + pers_pf
    gesamt = geraet_und_verbrauch + pers_gesamt
    return {
        "System": system["name"],
        "Gerätekosten": system["geraetekosten"],
        "Verbrauchskosten": verbrauchskosten,
        "Gerät+Verbrauch": geraet_und_verbrauch,
        "Pers.kosten PW": pers_pw,
        "Pers.kosten PF": pers_pf,
        "Pers.kosten gesamt": pers_gesamt,
        "Gesamtkosten": gesamt
    }

# Berechnung und Ausgabe als Tabelle mit Spalten in der Reihenfolge wie im Kommentar
print(f"{'System':<9} {'Gerätekosten':>13} {'Patronenwechsel':>16} {'Papierfüllung':>15} {'Verbrauch_in_cent':>18} {'Verbrauchskosten':>18} {'Geräte_u_Verbrauchskosten':>26} {'Pers.kosten_PW':>15} {'Pers.kosten_PF':>15} {'Pers.kosten gesamt':>18} {'Ges.Kosten':>13}")
print("-" * 170)
for sys in systeme:
    res = berechne_kosten(sys)
    print(f"{res['System']:<9} "
          f"{res['Gerätekosten']:13.2f} "
          f"{sys['patronenwechsel']:16d} "
          f"{sys['papierfuellung']:15d} "
          f"{sys['verbrauch_seite_cent']:18.2f} "
          f"{res['Verbrauchskosten']:18.2f} "
          f"{res['Gerät+Verbrauch']:26.2f} "
          f"{res['Pers.kosten PW']:15.2f} "
          f"{res['Pers.kosten PF']:15.2f} "
          f"{res['Pers.kosten gesamt']:18.2f} "
          f"{res['Gesamtkosten']:13.2f}")

# Kompakte und übersichtliche Tabelle
header = (
    f"{'Sys':<4} {'Gerät':>7} {'PW':>4} {'PF':>4} {'V.cnt':>6} "
    f"{'V.kost':>8} {'G+V':>8} {'P.PW':>7} {'P.PF':>7} {'P.Ges':>8} {'Gesamt':>9}"
)
print(header)
print("-" * len(header))
for sys in systeme:
    res = berechne_kosten(sys)
    print(
        f"{res['System']:<4} "
        f"{res['Gerätekosten']:7.2f} "
        f"{sys['patronenwechsel']:4d} "
        f"{sys['papierfuellung']:4d} "
        f"{sys['verbrauch_seite_cent']:6.2f} "
        f"{res['Verbrauchskosten']:8.2f} "
        f"{res['Gerät+Verbrauch']:8.2f} "
        f"{res['Pers.kosten PW']:7.2f} "
        f"{res['Pers.kosten PF']:7.2f} "
        f"{res['Pers.kosten gesamt']:8.2f} "
        f"{res['Gesamtkosten']:9.2f}")



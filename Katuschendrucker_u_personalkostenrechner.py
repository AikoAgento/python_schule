#Kostenkalkulation Farbdrucker
#System	Gerätekosten	Anzahl Patronen-wechsel	Papierfach Blatt 	Anzahl Papierfach-füllungen	Verbrauchskosten pro Seite in Cent	Verbrauchskosten	Geräte- und Verbrauchskosten	Personalkosten KW	Personalkosten PF	Personalkosten	Gesamtkosten
#A	    350,00€	        60	                    375		                                        6,7						
#B	    390,00€	        65	                    500		                                        7,2						
#C	    450,00€	        73	                    500		                                        6,5						
#D	    560,00€	        50	                    750		                                        5,8						
#E	    680,00€	        40	                    1000	                                        5,5						
#F	    750,00€	        30	                    500		                                        6,8						
#
#    KW=Kartuschenwechsel  PF = Papierfachfüllungen
#Zusatzangaben: Seitenzahl insges. 19200, Zeit KW: 4 Minuten, Zeit PF: 2 Minuten, Stundensatz: 30,00 €

systeme = [
    {"name": "A", "geraetekosten": 350.00, "patronenwechsel": 60, "papierfach_blatt": 375, "verbrauch_cent": 6.7},
    {"name": "B", "geraetekosten": 390.00, "patronenwechsel": 65, "papierfach_blatt": 500, "verbrauch_cent": 7.2},
    {"name": "C", "geraetekosten": 450.00, "patronenwechsel": 73, "papierfach_blatt": 500, "verbrauch_cent": 6.5},
    {"name": "D", "geraetekosten": 560.00, "patronenwechsel": 50, "papierfach_blatt": 750, "verbrauch_cent": 5.8},
    {"name": "E", "geraetekosten": 680.00, "patronenwechsel": 40, "papierfach_blatt": 1000, "verbrauch_cent": 5.5},
    {"name": "F", "geraetekosten": 750.00, "patronenwechsel": 30, "papierfach_blatt": 500, "verbrauch_cent": 6.8},
]

seiten_gesamt = 19200
zeit_kw = 4      # Minuten pro Kartuschenwechsel
zeit_pf = 2      # Minuten pro Papierfachfüllung
stundenlohn = 30 # €/h

def berechne_kosten(system):
    # Anzahl Papierfachfüllungen berechnen
    papierfach_fuellungen = -(-seiten_gesamt // system["papierfach_blatt"])  # Aufrunden
    # Verbrauchskosten
    verbrauchskosten = seiten_gesamt * system["verbrauch_cent"] / 100
    # Geräte- und Verbrauchskosten
    geraet_verbrauch = system["geraetekosten"] + verbrauchskosten
    # Personalkosten Kartuschenwechsel
    pers_kw = system["patronenwechsel"] * zeit_kw / 60 * stundenlohn
    # Personalkosten Papierfachfüllung
    pers_pf = papierfach_fuellungen * zeit_pf / 60 * stundenlohn
    # Gesamte Personalkosten
    pers_gesamt = pers_kw + pers_pf
    # Gesamtkosten
    gesamt = geraet_verbrauch + pers_gesamt
    return {
        "System": system["name"],
        "Gerätekosten": system["geraetekosten"],
        "Patronenwechsel": system["patronenwechsel"],
        "Papierfachfüllungen": papierfach_fuellungen,
        "Verbrauch_cent": system["verbrauch_cent"],
        "Verbrauchskosten": verbrauchskosten,
        "Gerät+Verbrauch": geraet_verbrauch,
        "Personalkosten KW": pers_kw,
        "Personalkosten PF": pers_pf,
        "Personalkosten gesamt": pers_gesamt,
        "Gesamtkosten": gesamt
    }

# Kompakte Tabelle mit allen Angaben inkl. Papierfach Blatt
header = (
    f"{'Sys':<4} {'Gerät':>7} {'KW':>4} {'PF-Bl':>7} {'PF':>4} {'V.cnt':>6} "
    f"{'V.kost':>8} {'G+V':>8} {'P.KW':>7} {'P.PF':>7} {'P.Ges':>8} {'Gesamt':>9}"
)
print(header)
print("-" * len(header))
for sys in systeme:
    res = berechne_kosten(sys)
    print(
        f"{res['System']:<4} "
        f"{res['Gerätekosten']:7.2f} "
        f"{res['Patronenwechsel']:4d} "
        f"{sys['papierfach_blatt']:7d} "
        f"{res['Papierfachfüllungen']:4d} "
        f"{res['Verbrauch_cent']:6.2f} "
        f"{res['Verbrauchskosten']:8.2f} "
        f"{res['Gerät+Verbrauch']:8.2f} "
        f"{res['Personalkosten KW']:7.2f} "
        f"{res['Personalkosten PF']:7.2f} "
        f"{res['Personalkosten gesamt']:8.2f} "
        f"{res['Gesamtkosten']:9.2f}"
    )



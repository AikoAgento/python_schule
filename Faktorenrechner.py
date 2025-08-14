


produktanzahl = int(input(f"Stückzahl der Produkte: \n"))
arbeitskosten = int(input(f"Kosten Pro Arbeitskraft in €: \n"))
betriebsmittelkosten = int(input(f"Kosten Pro Betriebsmittel in €: \n"))
Arbeitskraft = int(input(f"Anzahl der Arbeitskrafteinheit: \n"))
Betriebsmittel = int(input(f"Anzahl Betriebsmittel: \n"))


gesammt_arbeitskosten = arbeitskosten * Arbeitskraft
gesammt_betriebskosten = betriebsmittelkosten * Betriebsmittel
gesammt_kosten_pro_produkt = gesammt_arbeitskosten + gesammt_betriebskosten
gesammt_kosten = gesammt_kosten_pro_produkt * produktanzahl

print(f"Gesamtkosten für {produktanzahl} Produkte: {gesammt_kosten} €")
print(f"Gesamtkosten pro Produkt: {gesammt_kosten_pro_produkt} €")
print(f"Gesamte Arbeitskosten: {gesammt_arbeitskosten} €")
print(f"Gesamte Betriebsmittelkosten: {gesammt_betriebskosten} €")
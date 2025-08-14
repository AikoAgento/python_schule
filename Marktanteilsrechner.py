

print("Umsatzhalbjahresrechner")
print("Bitte geben Sie die Umsätze für die ersten sechs Halbjahre ein z.B. 3.6 (nicht 3,6).")

branchenhalbjahresumsatz1 = float(input("Bitte geben Sie den Branchenumsatz des ersten Halbjahres ein: \n"))
branchenhalbjahresumsatz2 = float(input("Bitte geben Sie den Branchenumsatz des zweiten Halbjahres ein: \n"))
branchenhalbjahresumsatz3 = float(input("Bitte geben Sie den Branchenumsatz des dritten Halbjahres ein: \n"))
branchenhalbjahresumsatz4 = float(input("Bitte geben Sie den Branchenumsatz des vierten Halbjahres ein: \n"))
branchenhalbjahresumsatz5 = float(input("Bitte geben Sie den Branchenumsatz des fünften Halbjahres ein: \n"))
branchenhalbjahresumsatz6 = float(input("Bitte geben Sie den Branchenumsatz des sechsten Halbjahres ein: \n"))


firmenhalbjahresumsatz1 = float(input("Bitte geben Sie den Firmenumsatz des ersten Halbjahres ein: \n"))
firmenhalbjahresumsatz2 = float(input("Bitte geben Sie den Firmenumsatz des zweiten Halbjahres ein: \n"))
firmenhalbjahresumsatz3 = float(input("Bitte geben Sie den Firmenumsatz des dritten Halbjahres ein: \n")) 
firmenhalbjahresumsatz4 = float(input("Bitte geben Sie den Firmenumsatz des vierten Halbjahres ein: \n"))
firmenhalbjahresumsatz5 = float(input("Bitte geben Sie den Firmenumsatz des fünften Halbjahres ein: \n"))
firmenhalbjahresumsatz6 = float(input("Bitte geben Sie den Firmenumsatz des sechsten Halbjahres ein: \n"))

### eigenerumsatz / branchenumsatz * 100 = relativer marktanteil

relativer_marktanteil1 = (firmenhalbjahresumsatz1 / branchenhalbjahresumsatz1) * 100
print(f"{relativer_marktanteil1} = ({firmenhalbjahresumsatz1} / {branchenhalbjahresumsatz1}) * 100")
relativer_marktanteil2 = (firmenhalbjahresumsatz2 / branchenhalbjahresumsatz2) * 100
relativer_marktanteil3 = (firmenhalbjahresumsatz3 / branchenhalbjahresumsatz3) * 100
relativer_marktanteil4 = (firmenhalbjahresumsatz4 / branchenhalbjahresumsatz4) * 100
relativer_marktanteil5 = (firmenhalbjahresumsatz5 / branchenhalbjahresumsatz5) * 100
relativer_marktanteil6 = (firmenhalbjahresumsatz6 / branchenhalbjahresumsatz6) * 100

### formel ((Marktanteil Halbjahr n - Marktanteil Halbjahr n-1) / Marktanteil Halbjahr n-1) * 100

prozentuale_steigerung1 = ((relativer_marktanteil2 - relativer_marktanteil1) / relativer_marktanteil1) * 100
print(f"{prozentuale_steigerung1:.2f}% = (({relativer_marktanteil2} - {relativer_marktanteil1}) / {relativer_marktanteil1}) * 100")
prozentuale_steigerung2 = ((relativer_marktanteil3 - relativer_marktanteil2) / relativer_marktanteil2) * 100
prozentuale_steigerung3 = ((relativer_marktanteil4 - relativer_marktanteil3) / relativer_marktanteil3) * 100
prozentuale_steigerung4 = ((relativer_marktanteil5 - relativer_marktanteil4) / relativer_marktanteil4) * 100
prozentuale_steigerung5 = ((relativer_marktanteil6 - relativer_marktanteil5) / relativer_marktanteil5) * 100

print("Relativer Marktanteil für jedes Halbjahr:")
print(f"1. Halbjahr: {relativer_marktanteil1:.2f}%")
print(f"2. Halbjahr: {relativer_marktanteil2:.2f}%")
print(f"3. Halbjahr: {relativer_marktanteil3:.2f}%")
print(f"4. Halbjahr: {relativer_marktanteil4:.2f}%")
print(f"5. Halbjahr: {relativer_marktanteil5:.2f}%")
print(f"6. Halbjahr: {relativer_marktanteil6:.2f}%")

print("Prozentuale Steigerung des relativen Marktanteils:")
print(f"Von 1. zu 2. Halbjahr: {prozentuale_steigerung1:.2f}%")
print(f"Von 2. zu 3. Halbjahr: {prozentuale_steigerung2:.2f}%")
print(f"Von 3. zu 4. Halbjahr: {prozentuale_steigerung3:.2f}%")
print(f"Von 4. zu 5. Halbjahr: {prozentuale_steigerung4:.2f}%")
print(f"Von 5. zu 6. Halbjahr: {prozentuale_steigerung5:.2f}%")
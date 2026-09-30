#Definere variabler"
m = 10.2 # kg
print(m)

#Innebygd variabel_(undestrek). Tar med seg verdien fra siste beregning"
#Endre verdien på variabelen m"
m = 10.5
print(m)

#Hvordan formattere tall i printfunksjonen? Eksempler med f-streng
x = 1/3
y = 200/3
print(x)
print(y)

print(f"x = {x:.2f} og y = {y:.3f}") 
# f = formatteringskoden som er tekststringen x = {x:.2f} y = {y:.3f}
# skrevet mellon anførselstegn. .2f betyr at vi vil ha 2 desimaler.
# .3f betyr at vi vil ha 3 desimaler.

#Printe uten varibler i f-strengen.
print(f"{x:.2f} og {y:.3f}") 

print(f"x = {x:.2e} og y = {y:.3e}")
#Dette er er f-streng formattert utskrift i eksponentiell form.
#2e betyr at vi vil ha 2 desimaler i eksponentiell form.
#3e betyr at vi vil ha 3 desimaler i eksponentiell form.

#Tegnsekvens \n betyr ny linje, splitter teksten i terminalen.
print("Line 1 \nLine 2")

#Fra tall til tekst og fra tekst til tall
#float (flyttall) og int (heltall)
#str (tekststreng)

#Eksempel konvertering fra flyttall til tekststreng
vekt_float = 59.8 # Dette er et flyttall, ikke en tekststreng. Vi kan ikke skrive ut flyttall i en tekststreng uten å konvertere det til tekst først.
#Bruker + operatøren for å slå sammen tekststrenger.
info = "Hun veier " + str(vekt_float) + "kg" # Konverterer flyttall til tekststreng.
print(info)

info2 = f"Hun veier {vekt_float}kg" # Dette er en f-streng, som gjør at vi kan skrive ut flyttall direkte i tekststrengen.
print(info2)

#Eksempel konvertering fra str til float
vekt_str = "61.8" # Dette er en tekststreng, ikke et flyttall.
vekt_float_gram = float(vekt_str) * 1000 # Konverterer tekststreng til flyttall.

print(vekt_float_gram)

#Printfunksjonen i seg selv er romslig og det kan skrive ut en blanding av tekst og tall.
vekt_float = 59.8 # Flyttall
print("Hun veier", vekt_float)
print("Hun veier", vekt_float, "kg") 

#Typekonvertering ifm inputfunksjonen
#Bruker angir verdier under kjøring av programmet. Inputfunksjonen returnerer alltid en tekststreng, så vi må konvertere den til et tall hvis vi vil bruke den i beregninger.

x = float(input("Skriv inn et tall: ")) 
y = x + 3.4
print(y)

x = int(input("Skriv inn et tall: "))
y = x + 5
print(y)

x = 1
t = (x > 0)
print(t)   

x = 0
t = (x > 2)
print(t)





# Oppgave 1 
print("Programmet beregner hvor gammel du er i 2026")
alder = int(input("Hvilket år er du født? "))
årstall = 2026 # Oppretter en variabel for årstall, alternativt sette 2026 direkte inn i print setningen.    

print(f"Du er {int(årstall) - alder} år gammel.") # Caster alder til int for å kunne trekke fra årstall.
print() # Tom linje for å skille output

# Oppgave 2 
print("Programmet beregner antallet pizzaer ut ifra antallet oppgitte elever.")

from math import ceil # Importerer ceil funksjonen fra math biblioteket for å runde opp til nærmeste heltall.
import numpy as np # Kjør "pip install numpy" i terminal for å installere numpy biblioteket lokalt.

antall_elever = int(input("Skriv inn antallet elever i klassen: "))
antall_pizzaer = np.ceil(antall_elever * 0.25) # Bruker numpy funksjonen ceil for å runde opp til nærmeste heltall.

print(f"Du trenger {int(antall_pizzaer)} pizzaer.")
print() # Tom linje for å skille output

# Oppgave 3 
print("Programmet regner om fra grader til radianer.")

import numpy as np 
def grader_til_radianer(v_grad):
    v_grad = v_grad*np.pi/180
    return v_grad

v_grad = float(input("Skriv inn gradtallet:")) # Bruker float for å kunne regne med desimaler.
v_rad = grader_til_radianer(v_grad) # Kaller funksjonen grader_til_radianer med v_grad som argument.

print(f"{v_grad} grader er lik {v_rad:.2f} radianer.") #Forkorter til 2 desimaler
print() # Tom linje for å skille output

# Oppgave 4a
print("Programmet viser land, hovedstad og befolkning i millioner.")
data = {"Norge": ["Oslo", 0.634], 
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }
print(data) #Skriver ut ordboka med land, hovedstad og befolkning i millioner.

# Oppgave 4b 
print("Programmet lar brukeren velge et eksisterend land fra ordboka.")
land = input("Skriv inn et av følgende land(Norge, England, Frankrike, Italia): ")
print(f"Hovedstaden i {land} er {data[land][0]} og befolkningen er {data[land][1]} millioner.")
print() # Tom linje for å skille output

#Oppgave 4c
print("Programmet lar brukeren legge til et nytt land i ordboka.")

nytt_land = input("Skriv inn et land som skal legges til i ordboka: ")
hovedstad = input("Skriv inn hovedstaden til det nye landet: ")
befolkning = float(input("Skriv inn befolkningen i millioner: "))
data[nytt_land] = [hovedstad, befolkning] # Legger til nytt land og informasjon i ordboka.
print(f"Landet {nytt_land} er lagt til i ordboka med informasjon: {data[nytt_land]}") #Sjekk at nytt land og informasjon er lagt til i ordboka.
print() # Tom linje for å skille output

# Oppgave 5 
print("Programmet beregner arealet og ytre omkretsen til en figur.")

import numpy as np

def beregne_areal_og_ytreomkrets(a, b): 
    #Beregne radius 
    r = a / 2 
    #Beregne hypotenus
    hypotenus = np.sqrt(a**2 + b**2) 
    
    #Bergne arealer
    areal_trekant = (a * b) / 2
    areal_halvsirkel = (np.pi * r**2) / 2
    totalt_areal = areal_trekant + areal_halvsirkel
    
    #Beregne omkrets
    omkrets_halvsirkel = np.pi * r
    omkrets_ytre = omkrets_halvsirkel + b + hypotenus
    
    return totalt_areal, omkrets_ytre

a = int(4)
b = int(5)
# Kaller funksjonen beregne_areal_og_ytreomkrets med a og b som argumenter, og lagrer resultatene i variablene areal og ytre_omkrets.
areal, ytre_omkrets = beregne_areal_og_ytreomkrets(a, b)
#Skriver ut arealet og ytre omkretsen med 2 desimaler til terminal.
print(f"Arealet til figuren er {areal:.2f} og den ytre omkretsen er {ytre_omkrets:.2f}.")    
print() # Tom linje for å skille output

#Oppgave 6
print("Programmet plotter funksjonen f(x) = -x^2 - 5 for x på intervallet [-10,10].")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100) # Lager en array med 100 punkter mellom -10 og 10.
y = -x**2 - 5 # Lager en array med y-verdiene til funksjonen f(x) = -x^2 - 5.
plt.plot(x, y) # Plotter y-verdiene mot x-verdiene.
plt.xlabel("x") # Tekst på x-aksen
plt.ylabel("f(x)") # Tekst på y-aksen
plt.title("Plot av f(x) = -x^2 - 5") # Setter tittel på plottet
plt.grid(True) # Legger til et rutenett i plottet.
plt.show() # Åpner et eget vindu med plottet.
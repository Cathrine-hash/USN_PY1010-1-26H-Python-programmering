# Oppgave 1 
print("Dette programmet beregner hvor gammel du er i 2026.")
alder = int(input("Hvilket år er du født? "))
årstall = 2026 # Oppretter en variabel for årstall, alternativt sette 2026 direkte inn i print setningen.    

print(f"Du er {int(årstall) - alder} år gammel.") # Caster alder til int for å kunne trekke fra årstall.

# Oppgave 2 
print("Dette programmet beregner antallet pizzaer ut ifra antallet oppgitte elever")
import numpy as np # Kjør "pip install numpy" i terminal for å installere numpy biblioteket lokalt.
antall_elever = int(input("Skriv inn antallet elever i klassen: "))
antall_pizzaer = np.ceil(antall_elever * 0.25) # Bruker numpy funksjonen ceil for å runde opp til nærmeste heltall.

print(f"Du trenger {int(antall_pizzaer)} pizzaer.")

# Oppgave 3 
print("Dette programmet regner om fra grader til radianer.")
import numpy as np 
def grader_til_radianer(v_grad):
    v_grad = v_grad*np.pi/180
    return v_grad

v_grad = float(input("Skriv inn gradtallet:")) # Bruker float for å kunne regne med desimaler.
v_rad = grader_til_radianer(v_grad) # Kaller funksjonen grader_til_radianer med v_grad som argument.

print(f"{v_grad} grader er lik {v_rad:.2f} radianer.") #Forkorter til 2 desimaler


# Oppgave 4a Opprett en dictionary med land som nøkkel. 
print("Dette programmet viser land, hovedstad og befolkning i millioner.")
data = {"Norge": ["Oslo", 0.634], 
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

print(data.values())
print(data.keys())

# Oppgave 4b Lag en input som spør brukeren om hvilket land de vil vite om.
land = input("Skriv inn et land(Norge, England, Frankrike, Italia): ")
print(f"Hovedstaden i {land} er {data[land][0]} og befolkningen er {data[land][1]} millioner.")

#Oppgave 4c Lag et program som spør brukeren om hvilket land de vil vite om, og returnerer hovedstaden og befolkningen i millioner.
nytt_land = input("Skriv inn et land som skal legges til i dictionaryen: ")
hovedstad = input("Skriv inn hovedstaden til det nye landet: ")
befolkning = float(input("Skriv inn befolkningen i millioner: "))
data[nytt_land] = [hovedstad, befolkning]

print(data) 

# Oppgave 5 Lag et program med en funksjon som tar a og b som innargumenter n/
#og som regner ut arealet og ytre omkrets til en figur som er satt sammen /n
#av en rettvinklet trekant og en halvsirkel. Funksjonen skal returnere arealet og ytre omkrets.

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
areal, ytre_omkrets = beregne_areal_og_ytreomkrets(a, b)
#Skriver ut arealet og ytre omkretsen med 2 desimaler til terminal.
print(f"Arealet til figuren er {areal:.2f} og den ytre omkretsen er {ytre_omkrets:.2f}.")    

#Oppgave 6 

# Oppgave 1 Dette programmet beregner hvor gammel du er i 2026.
alder = int(input("Hvilket år er du født? "))
årstall = 2026 # Oppretter en variabel for årstall, alternativt sette 2026 direkte inn i print setningen.    
print(f"Du er {int(årstall) - alder} år gammel.") # Caster alder til int for å kunne trekke fra årstall.

# Oppgave 2 Dette programmet beregner antallet pizzaer ut ifra antallet oppgitte elever
import numpy as np # Kjør "pip install numpy" i terminal for å installere numpy biblioteket lokalt.
antall_elever = int(input("Skriv inn antallet elever i klassen: "))
antall_pizzaer = np.ceil(antall_elever * 0.25) # Bruker numpy funksjonen ceil for å runde opp til nærmeste heltall.
print(f"Du trenger {int(antall_pizzaer)} pizzaer.")

# Oppgave 3 Progammet regner om fra grader til radianer.
import numpy as np 
def grader_til_radianer(v_grad):
    v_rad = v_grad*np.pi / 180
    return v_rad




v_grad = float(input("Skriv inn gradtallet:")) # Bruker float for å kunne regne med desimaler.
v_rad = v_grad*np.pi/180 # Regner om fra grader til radianer.
v_rad = round(v_rad, 2) # Forkorter til 2 desimaler.



# Oppgave 4 a,b og c

# Oppgave 5

# Oppgave 6


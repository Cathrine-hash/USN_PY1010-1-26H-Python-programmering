# Dette programmet skal presentere og beregne de
# årlige totalkostnadene for elbil og bensinbil.
# Samt beregne og vise årlig kostnadsdifferanse. 
    
# Oversikt kostnader for elbil
kjørelengde_elbil = 10000 #km/år
dager = 365 #dager/år
forsikring_elbil = 5000 #kr/år
TFA_elbil = 8.38 * dager #kr/år Trafikkforsikringsavgift
strøm_elbil_kr_kWh = 2.00 #kr/kWh
strømforbruk_elbil_kWh_km = 0.2 * strøm_elbil_kr_kWh * kjørelengde_elbil #kWh/år
bomavgift_elbil = 0.1 * kjørelengde_elbil #kr/år 

print("Oversikt over kostnader for elbil")
print("Kjørelengde elbil per år:10000 km")
print("Forskringskostnad elbil per år:5000 kr")
print("TFA elbil per år:8.38 kr * 365 dager")
print("Strømpris elbil per kWh:2.00 kr")
print("Strømforbruk elbil per år:0.2 kWh/km * 2.00 kr/kWh strømpris * 10000 km")
print("Bomavgift elbil per år:0.1 kr/km * 10000 km")

# Beregninger av kostnader for elbil per år
print("Totalsummen for elbil per år blir",forsikring_elbil + TFA_elbil + strømforbruk_elbil_kWh_km + bomavgift_elbil)

# Oversikt kostnader for bensinbil

kjørelengde_bensinbil = 10000 #km/år
dager = 365 #dager/år
forsikring_bensinbil = 7500 #kr/år
TFA_bensinbil = 8.38 * dager #kr/år Trafikkforsikringsavgift
drivstoff_forbruk_bensinbil = 1.0 * kjørelengde_bensinbil #kr/km
bomavgift_bensinbil = 0.3 * kjørelengde_bensinbil #kr/km


print("Oversikt kostnader for bensinbil")
print("Kjørelengde bensinbil per år :10000 km")
print("Forsikringskostnad bensinbil per år:7500 kr")
print("Trafikkforsikringsavgift bensinbil per år:8.38 kr * 365 dager")
print("Drivstofforbruk bensinbil per år:1.0 kr/km * 10000 km")
print("Bomavgift bensinbil per år:0.3 kr/km * 10000 km")

#Beregninger kostnader for bensinbil per år
print("Totalsummen for bensinbil per år blir", forsikring_bensinbil + TFA_bensinbil + drivstoff_forbruk_bensinbil + bomavgift_bensinbil)

#Kostnadsdifferanse mellom elbil og bensinbil per år
Totalsum_elbil_per_år = forsikring_elbil + TFA_elbil + strømforbruk_elbil_kWh_km + bomavgift_elbil
Totalsum_bensinbil_per_år = forsikring_bensinbil + TFA_bensinbil + drivstoff_forbruk_bensinbil + bomavgift_bensinbil
print("Kostnadsdifferansen mellom bensinbil og elbil per år blir", Totalsum_bensinbil_per_år - Totalsum_elbil_per_år)



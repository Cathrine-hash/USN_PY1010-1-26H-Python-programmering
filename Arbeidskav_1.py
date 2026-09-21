# Dette programmet skal presentere og beregne de
# årlige totalkostnadene for elbil og bensinbil.
# Samt beregne og vise årlig kostnadsdifferanse. 
    
# Oversikt kostnader for elbil
print("Oversikt over kostnader for elbil")
årlig_kjørelengde_elbil = 10000 #km/år
print("Kjørelengde elbil per år:10000 km")
dager = 365 #dager/år
årlig_forsikringskostnad_elbil = 5000 #kr/år
print("Forskringskostnad elbil per år:5000 kr")
daglig_forsikringsavgift_elbil = 8.38 * dager #kr/år
print("Trafikkforsikringsavgift elbil per år: 8.35 kr * 365 dager")
strømpris_elbil_kr_kWh = 2.00 #kr/kWh
print("Strømpris elbil per kWh:2.00 kr")
drivstoff_forbruk_elbil_kWh_km = 0.2 * strømpris_elbil_kr_kWh * årlig_kjørelengde_elbil #kWh/år
print("Drivstofforbruk elbil per år:0.2 kWh/km * 2.00 kr/kWh strømpris * 10000 km")
kostnader_bomavgift_elbil = 0.1 * årlig_kjørelengde_elbil #kr/år 
print("Bomavgift elbil per år: 0.1 kr/km * 10000 km")
# Beregninger av kostnader for elbil per år
print("Totalsummen for elbil per år blir",årlig_forsikringskostnad_elbil + daglig_forsikringsavgift_elbil + drivstoff_forbruk_elbil_kWh_km + kostnader_bomavgift_elbil)

# Oversikt kostnader for bensinbil
print("Oversikt kostnader for bensinbil")
årlig_kjørelengde_bensinbil = 10000 #km/år
print("Kjørelengde bensinbil per år :10000 km")
dager = 365 #dager/år
årlig_forsikringskostnad_bensinbil = 7500 #kr/år
print("Forsikringskostnad bensinbil per år:7500 kr")
daglig_forsikringsavgift_bensinbil = 8.35 * dager #kr/år
print("Trafikkforsikringsavgift bensinbil per år:8.35 kr * 365 dager")
drivstoff_forbruk_bensinbil = 1.0 * årlig_kjørelengde_bensinbil #kr/km
print("Drivstofforbruk bensinbil per år:1.0 kr/km * 10000 km")
kostnader_bomavgift_bensinbil = 0.3 * årlig_kjørelengde_bensinbil #kr/km
print("Bomavgift bensinbil per år:0,3 kr/km * 10000 km")

#Beregninger kostnader for bensinbil per år
print("Totalsummen for bensinbil per år blir", årlig_forsikringskostnad_bensinbil + daglig_forsikringsavgift_bensinbil + drivstoff_forbruk_bensinbil + kostnader_bomavgift_bensinbil)

#Kostnadsdifferanse mellom elbil og bensinbil per år
Totalsum_elbil_per_år = årlig_forsikringskostnad_elbil + daglig_forsikringsavgift_elbil + drivstoff_forbruk_elbil_kWh_km + kostnader_bomavgift_elbil
Totalsum_bensinbil_per_år = årlig_forsikringskostnad_bensinbil + daglig_forsikringsavgift_bensinbil + drivstoff_forbruk_bensinbil + kostnader_bomavgift_bensinbil
print("Kostnadsdifferansen mellom bensinbil og elbil per år blir", Totalsum_bensinbil_per_år - Totalsum_elbil_per_år)



import csv

with open('carsales_2017_09_v4.csv', "rb") as infile, open('second_clean_output_carsales_2017_09_v4.csv', "wb") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, r.fieldnames)
    w.writeheader()
    for row in r:
            
        if not row["ANNONCE_LINK"].strip():
            row["ANNONCE_LINK"] = " "
            
        if not row["ANNONCE_DATE"].strip():
            row["ANNONCE_DATE"] = "0000-00-00 00:00:00"
            
        if not row["ID_CLIENT"].strip():
            row["ID_CLIENT"] = " "
            
        if not row["GARAGE_ID"].strip():
            row["GARAGE_ID"] = " "
            
        if not row["TYPE"].strip():
            row["TYPE"] = " "
            
        if not row["SITE"].strip():
            row["SITE"] = " "
            
        if not row["MARQUE"].strip():
            row["MARQUE"] = " "
            
        if not row["MODELE"].strip():
            row["MODELE"] = " "
            
        if not row["ANNEE"].strip():
            row["ANNEE"] = "0"
            
            
            
        if not row["MOIS"].strip():
            row["MOIS"] = "0"
            
        if not row["NOM"].strip():
            row["NOM"] = " "
            
        if not row["CARROSSERIE"].strip():
            row["CARROSSERIE"] = " "
            
        if not row["OPTIONS"].strip():
            row["OPTIONS"] = " "
            
        if not row["CARBURANT"].strip():
            row["CARBURANT"] = " "
            
        if not row["CYLINDRE"].strip():
            row["CYLINDRE"] = " "
            
        if not row["PUISSANCE"].strip():
            row["PUISSANCE"] = " "
            
        if not row["PORTE"].strip():
            row["PORTE"] = " "
            
        if not row["BOITE"].strip():
            row["BOITE"] = " "
            
        if not row["ENGINE"].strip():
            row["ENGINE"] = " "
            
        
        if not row["NB_VITESSE"].strip():
            row["NB_VITESSE"] = "0"
        if not row["PRIX"].strip():
            row["PRIX"] = "0"
        if not row["KM"].strip():
            row["KM"] = "0"
        if not row["PLACE"].strip():
            row["PLACE"] = " "
        if not row["COULEUR"].strip():
            row["COULEUR"] = " "
        if not row["PHOTO"].strip():
            row["PHOTO"] = "0"
        if 'cc' in row["LITRE"].strip():
            row["LITRE"] = row["LITRE"].split('cc')
            row["LITRE"] = row["LITRE"][0]
        if not row["LITRE"].strip():
            row["LITRE"] = "0"
        if not row["TRANSMISSION"].strip():
            row["TRANSMISSION"] = " "
        if not row["DESCRIPTION"].strip():
            row["DESCRIPTION"] = " "
        if not row["IMMAT"].strip():
            row["IMMAT"] = " "
        if not row["No_VEHICULE"].strip():
            row["No_VEHICULE"] = " "
        if not row["No_CHASSIS"].strip():
            row["No_CHASSIS"] = " "
            
        if not row["VN_IND"].strip():
            row["VN_IND"] = " "
        if not row["CONTACT"].strip():
            row["CONTACT"] = " "
        if not row["LOCATION"].strip():
            row["LOCATION"] = " "
        if not row["CONTACT_PRENOM"].strip():
            row["CONTACT_PRENOM"] = " "
        if not row["CONTACT_NOM"].strip():
            row["CONTACT_NOM"] = " "
        if not row["GARAGE_NAME"].strip():
            row["GARAGE_NAME"] = " "
        if not row["SELLER_TYPE"].strip():
            row["SELLER_TYPE"] = " "
        if not row["ADRESSE"].strip():
            row["ADRESSE"] = " "
        if not row["VILLE"].strip():
            row["VILLE"] = " "
        if not row["CP"].strip():
            row["CP"] = " "
        if not row["DEPARTEMENT"].strip():
            row["DEPARTEMENT"] = " "
            
            
        if not row["PROVINCE"].strip():
            row["PROVINCE"] = " "
        if not row["COUNTRY"].strip():
            row["COUNTRY"] = " "
        if not row["TELEPHONE"].strip():
            row["TELEPHONE"] = " "
        if not row["TELEPHONE_2"].strip():
            row["TELEPHONE_2"] = " "
        if not row["TELEPHONE_3"].strip():
            row["TELEPHONE_3"] = " "
        if not row["TELEPHONE_4"].strip():
            row["TELEPHONE_4"] = " "
        if not row["TELEFAX"].strip():
            row["TELEFAX"] = " "
        if not row["EMAIL"].strip():
            row["EMAIL"] = " "
        if not row["GARAGE_LICENCE"].strip():
            row["GARAGE_LICENCE"] = " "
         
    

        w.writerow(row)

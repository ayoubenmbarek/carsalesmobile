import csv

with open('latest_carsales_2017_09_v4.csv', "rb") as infile, open('latest5_carsales_2017_09_v4.csv', "wb") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, r.fieldnames)
    w.writeheader()
    for row in r:
            if row["TRANSMISSION"]:
                    row["TRANSMISSION"] = row["TRANSMISSION"].split(' ')
                    row["TRANSMISSION"] = row["TRANSMISSION"][0]
            if row["NB_VITESSE"]:
                row["NB_VITESSE"] = row["TRANSMISSION"]
            if not row["NB_VITESSE"].strip():
                row["NB_VITESSE"] = "0"
            w.writerow(row)

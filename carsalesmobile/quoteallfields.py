#import csv
#from StringIO import StringIO

#quotedData = StringIO()

#with open('/home/databiz41/carsalesmobile/carsalesmobile/latest5_carsales_2017_09_v4.csv',"w") as f:
#openfile = open("/home/databiz41/carsalesmobile/carsalesmobile/latest5_carsales_2017_09_v4.csv", "wb")
#reader = csv.reader(openfile)
#writer = csv.writer(openfile, quoting=csv.QUOTE_ALL)
#for row in reader:
#        writer.writerow(row)



import csv

with open('/home/databiz41/carsalesdealers/carsalesdealers/dealers_carsales-05-02-18.csv', "rb") as infile, open('/home/databiz41/carsalesdealers/carsalesdealers/dealers_carsales-05-02-18_quoted.csv', "wb") as outfile:
    r = csv.DictReader(infile,delimiter=',')
    w = csv.DictWriter(outfile, r.fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
    w.writeheader()
    for row in r:
        w.writerow(row)

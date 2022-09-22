import csv
import settings

heightsq = settings.height * settings.height
#For BMI calc

rows = []
with open(settings.inputfile ,'r') as file:
        csvreader = csv.reader(file)
        body = next(csvreader)
        header = next(csvreader)
        for row in csvreader:
                rows.append(row)
file.close()

datecol = header.index("dateTime")
fatcol = header.index("fat")
weightcol = header.index("weight")

outfile = open(settings.outputfile,'w')
writer = csv.writer(outfile)

writer.writerow(["Body"])

outputheaders = ['Date','Weight','BMI','Fat']
writer.writerow(outputheaders)

for row in rows:
        newrow = [row[datecol][0:10] , row[weightcol] , str(float(row[weightcol]) / heightsq), row[fatcol]]
        writer.writerow(newrow)

outfile.close

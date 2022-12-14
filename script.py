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
writer = csv.writer(outfile,quoting=csv.QUOTE_ALL)

writer.writerow(["Body"])

outputheaders = ['Date','Weight','BMI','Fat']
writer.writerow(outputheaders)

for row in rows:
        newrow = [row[datecol][0:10] , row[weightcol] , (round(float(row[weightcol])/heightsq,2)), row[fatcol]]
        writer.writerow(newrow)

outfile.close

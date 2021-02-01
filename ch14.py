from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
#print(data)
dataFile = StringIO(data)
#print(data)
csvReader = csv.reader(dataFile)
#for row in csvReader:
    #print(row)
for row in csvReader:
    print("The album \""+row[0]+"\" was released in "+str(row[1]))
import csv
import operator
ifile =open('data.csv', 'rb')
infile = csv.reader(ifile)
# The first entry is the header line
infields = infile.next()
statindex = infields.index('eur_wage')
# create the sorted list
sortedlist = sorted(infile, key=operator.itemgetter(statindex), reverse=True)
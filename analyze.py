# text analysis methods

goodExample = []
badExample = []

import csv

def getWords():
    with open('bad_words.csv') as csvfile:
        readline=csv.reader(csvfile, delimiter=' ')

        for row in readline:
            print(row[0]) # for some reason its read in as list of single string
            badExample.append(row[0])
    ##print(badExample)

    with open('good_words.csv') as csvfile:
        readline=csv.reader(csvfile, delimiter=' ')

        for row in readline:
            print(row[0]) # for some reason its read in as list of single string
            goodExample.append(row[0])
    ##print(goodExample)    
    return goodExample, badExample

def sortMostCommon():
    pass

def sortBestMatch():
    pass

def sortMostRecent():
    pass

def deleteUnrelated():
    pass

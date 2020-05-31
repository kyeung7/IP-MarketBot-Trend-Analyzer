# get score of market
def interpret(goodWords, badWords, fullStr):
    marketScore = 0
    for word in goodWords:
        if word in string:
            marketScore += 0.1
    for word in badWords:
        if word in string:
            marketScore -= 0.1

    print('test trend score: ' + str(marketScore))

def displayResults():
    pass

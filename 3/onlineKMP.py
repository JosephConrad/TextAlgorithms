from strongPrefixSuffix import strongPrefixSuffix
import sys


def onlineKMP(pattern):
    x = pattern
    m = len(pattern)

    strongP = strongPrefixSuffix(pattern)
    j = 0 
    f = open(sys.argv[1], 'r')
    for sym in f.read():    
        print sym
        while j >=0  and x[j] != sym: j = strongP[j]
        j += 1
        if j == m:
            print "String matched"
            j = strongP[m] 
        else:
            print "No matching found"
    pass


pattern = "ma"
onlineKMP(pattern)



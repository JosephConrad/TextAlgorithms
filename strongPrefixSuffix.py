
def strongPrefixSuffix(x):
    strongP = [-1]
    t = -1
    m = len(x)
    for j in range(0, m):
        while t >=0 and x[t] != x[j]:
            t = strongP[t]
        t += 1

        # print "j: " + str(j)
        # print "t: " + str(t) + "\n"
       
        # jesli mamy koniec slowa lub nastepny element w slowie jest rowny 
        #       nastepnemu elementowi prefiksu obecnie najdluzszego prefikso sufiksu 
        if j == m-1 or x[j+1] != x[t]:
            nextElem = t
        else:
            nextElem = strongP[t]
            
        strongP.append(nextElem)
    return strongP


if __name__ == "__main__":
    # tablica silnych prefikso sufiksow = to samo co tablica pref suf
    #       z dodatkowym warunkiem, ze nastepny element musi byc rozny od
    #       nastepnego elementu prefiksu tzn. x[k+1] != x[j+1]
    text = "abaab"
    print strongPrefixSuffix(text)

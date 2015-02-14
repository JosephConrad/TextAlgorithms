
#x = [0,1,1,0,1,0,0,1,
#     1,0,0,1,0,1,1,0,
#     1,0,0,1,0,1,1,0,
#     0,1,1,0,1,0,0,1]


def prefixSufix(x):
    # ilosc znakow w tekscie
    m = len(x)
    
    P=[-1]
    t=-1
    for j in range(0, m):
        while t>=0 and x[t] != x[j]:
            t=P[t]
        t+=1
        P.append(t) 
    print P
    return P
    

x = "01101001100101101001011001101001"
#x = "abababababb"
print prefixSufix(x)

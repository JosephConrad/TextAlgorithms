
#x = [0,1,1,0,1,0,0,1,
#     1,0,0,1,0,1,1,0,
#     1,0,0,1,0,1,1,0,
#     0,1,1,0,1,0,0,1]


def prefixSufix(x):
    m = len(x)+1
    
    P=[-1]
    t=-1
    for j in range(1, m):
        while t>=0 and x[t+1] != x[j]:
            t=P[t]
        t+=1
        print m
        P.append(t) 
    print P
    return P
    

#x = "01101001100101101001011001101001"
x = "0abababababb"
print prefixSufix(x)

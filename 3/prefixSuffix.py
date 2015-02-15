
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
    return P
    

if __name__ == "__main__":
    print prefixSufix(x)
#x = "abababababb"

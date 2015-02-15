
from prefixSuffix import *


def morissPratt(text, pattern):
    n = len(text)
    x = pattern  
    m = len(pattern)
    y = text
    i = 0
    j = 0 
    P = prefixSufix(pattern)
    while i <= n - m:
        # dopoki indeks j jest mniejszy od dlugosci wzorca
        while j < m and pattern[j] == text[i+j]:
            j += 1
        
        if j == m: 
            print P
            print j
            return True
        i = i + j - P[j]
        j = max(0, P[j])
    return False





text = "ala ma kota"
pattern = "kota"
print morissPratt(text, pattern)

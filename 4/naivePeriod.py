

def naivePeriod(x):
    period = 1
    print period
    for i in range(2, len(x)):
        if x[i] != x[i-period]:
            period = i
        print period
    return period

word = 'bajtocja'
# zero at the beginning - not used guard
word ='0'+ "".join(["aba" for i in range(6)])+'a'
print word
naivePeriod(word[::-1])

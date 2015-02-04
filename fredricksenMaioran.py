
def ext(x, n):
    res = x
    for i in range(0, n / len(x) - 1):
        res = res + x
    for i in range(0, n % len(x)):
        res = res + x[i]
    return res

def lastZero(word):
    i = 1
    if word[-i] == '0': return word
    while word[-i] != '0':
        i += 1
    return word[:-(i-1)]

def fredricksenMaioran(n):
    x = '0'
    print x
    while x != '1':
        x = lastZero(ext(x, n))
        x = x[0:-1] + '1'
        print x

fredricksenMaioran(4)

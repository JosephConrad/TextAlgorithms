
def process(x, printed, i):
    print "".join([" " for i in range(i)])+x
    printed.add(x)
    return x

def deBruijn(n):
    w = "".join(['0' for i in range(n-1)])+'1'
    print w
    printed = set()
    printed.add(w)
    i = 0
    while True:
        i += 1
        x = w[1:]+str(int(w[-1])^1)
        if not x in printed:
            w = process(x, printed, i) 
            continue
        x = w[1:]+w[-1]
        if not x in printed:
            w = process(x, printed, i) 
            continue
        break

deBruijn(4)
        

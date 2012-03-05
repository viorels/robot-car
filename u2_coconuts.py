
def assume(n):
    for i in range(5):
        n = (n-1)/5*4
    r = (n - 1) / 5
    return r

for n in range(100000):
    r = assume(float(n))
    if abs(r - round(r)) < 0.0001:
        print "%d => %s" % (n, r)


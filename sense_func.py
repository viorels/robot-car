n = 5
#p = [1./n]*n
p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', ' green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = [p[i]*pHit if world[i] == Z else p[i]*pMiss for i in range(len(p))]
    s = sum(q)
    norm_q = [x/s for x in q]
    return norm_q

def move(p, U):
    if len(p) == 0:
        return p
    U = -U % len(p) # Normalize U, using modulo - even works for negative U
    return p[U:] + p[:U]

#print sense(p, Z)
print move(p, 1)


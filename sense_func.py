n = 5
p = [1./n]*n
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = [p[i]*pHit if world[i] == Z else p[i]*pMiss for i in range(len(p))]
    s = sum(q)
    norm_q = [x/s for x in q]
    return norm_q

print sense(p, Z)


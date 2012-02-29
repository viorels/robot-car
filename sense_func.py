#!/usr/bin/python

n = 5
#p = [1./n]*n
p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = pUndershoot = 0.1

def sense(p, Z):
    q = [p[i]*pHit if world[i] == Z else p[i]*pMiss for i in range(len(p))]
    s = sum(q)
    norm_q = [x/s for x in q]
    return norm_q

def move(p, U):
    q = [p[(i-U) % len(p)] * pExact + 
         p[(i-U-1) % len(p)] * pOvershoot +
         p[(i-U+1) % len(p)] * pUndershoot
         for i in range(len(p))]
    return q

for i in range(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

print p


colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
n = sum(len(line) for line in colors)
p = [[1./n] * len(colors[i]) for i in range(len(colors))]



#Your probability array must be printed 
#with the following code.

show(p)

##########

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



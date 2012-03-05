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
#n = sum(len(line) for line in colors)
#p = [[1./n] * len(colors[i]) for i in range(len(colors))]

def zero_prob(world, zero=0.):
    return [[zero] * len(world[i]) for i in range(len(world))]
p = zero_prob(colors, zero=1.) # ???

def move_with(x, y, dx, dy, world):
    return (x+dx) % len(world[y]), (y+dy) % len(world)

def norm(p):
    s = sum(sum(line) for line in p)
    if s > 0:
        return [[x/s for x in line] for line in p]
    else:
        return p

def sense(p, Z, world, sensor_prob):
    q = zero_prob(world)
    for j in range(len(p)):
        for i in range(len(p[j])):
            if colors[j][i] == Z:
                q[j][i] = p[j][i] * sensor_right
            else:
                q[j][i] = p[j][i] * (1-sensor_right)
    return norm(q)

def move(p, U, world, move_prob):
    q = zero_prob(world)
    for j in range(len(p)):
        for i in range(len(p[j])):
            ni, nj = move_with(i, j, *U, world=world)
            q[j][i] += p[j][i] * (1-move_prob)
            q[nj][ni] += p[j][i] * move_prob
    return norm(q)


for i in range(len(motions)):
    p = move(p, motions[i], world=colors, move_prob=p_move)
    p = sense(p, measurements[i], world=colors, sensor_prob=sensor_right)

#Your probability array must be printed 
#with the following code.

import unittest
class MyTest(unittest.TestCase):
    colors = [['green', 'green', 'green'],
              ['green', 'red', 'red'],
              ['green', 'green', 'green']]
    measurements = ['red', 'red']
    motions = [[0, 0], [0, 1]]
    sensor_right = 1.0
    p_move = 0.5

    def testMethod(self):
        p = zero_prob(self.colors, zero=1.)
        for i in range(len(self.motions)):
            p = move(p, self.motions[i], world=self.colors, move_prob=self.p_move)
            p = sense(p, self.measurements[i], world=self.colors, sensor_prob=self.sensor_right)
        print p

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main(argv=sys.argv[:1]) # do not pass 'test' argument
    exit(0)

show(p)

##########




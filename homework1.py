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

def zero_prob():
    return [[0.] * len(colors[i]) for i in range(len(colors))]

def move_with(x, y, dx, dy):
    return (x+dx) % len(colors[y]), (y+dy) % len(colors)

def norm(p):
    s = sum(sum(line) for line in p)
    return [[x/s for x in line] for line in p]

def sense(p, Z):
    q = zero_prob()
    for j in range(len(p)):
        for i in range(len(p[j])):
            if colors[j][i] == Z:
                q[j][i] = p[j][i] * sensor_right
            else:
                q[j][i] = p[j][i] * (1-sensor_right)
    return norm(q)

def move(p, U):
    q = zero_prob()
    for j in range(len(p)):
        for i in range(len(p[j])):
            #print "%d, %d" % (i, j)
            ni, nj = move_with(i, j, *U)
            #print "[%d, %d] + (%d, %d) => [%d, %d]" % (i, j, U[0], U[1], ni, nj)
            q[j][i] += p[j][i] * (1-p_move)
            q[nj][ni] += p[j][i] * p_move
    return norm(q)


for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])

#Your probability array must be printed 
#with the following code.

show(p)

##########


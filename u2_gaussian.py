
from math import sqrt, pi, e

def f(x, u, sigma2):
    1./sqrt(2*pi*sigma2)*e**(-(x-u)**2/2*sigma2)

print f(8, 10, 4)


import autograd
from autograd import numpy as np

def find_seed(g,c=0,eps=2**(-26)):
    if (g(0)-c)*(g(1)-c) > 0:
        return None
    else:
        a = 0
        b = 1
        while b-a > eps:
            t = (a+b)/2
            if (g(m)-c)*(g(a)-c)<=0:
                b = t
            else:
                a = t
        t = (a+b)/2
        return t

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def grad_f(x,y):
    g = autograd.grad
    return np.r_[g(f,0)(x,y),g(f,1)(x,y)]
    
def simple_contour(f,c=0.0,delta=0.01):
    x = []
    y = []
    y0 = find_seed(lambda x:f(0,x),c) 
    if y0 == None:
        return(x,y)
    else:
        x.append(0.0)
        y.append(y0)
        
    
def newton(f,p0,eps=10**-4):
    def pr(p):
        g = grad(f,p)
        return(p - (f(x)/(g.norme()**2))*g)
    p1 = pr(p0)
    while dist(p0,p1) > eps:
        p0 = p1
        p1 = pr(p1)
    return(p1)
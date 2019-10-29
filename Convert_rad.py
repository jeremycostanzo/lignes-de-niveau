def p_a1(ang):
    """
    Cette fonction calcule le point p sur le cercle unite tel que l'angle oriente (pt(1,0),p) vale ang
    """
    return(pt(np.cos(ang),np.sin(ang)))    

def rad(p):
    """
    Cette fonction calcule l'angle oriente (pt(1,0),p)
    """
    pn = p.normalized()
    x = pn.x
    y = pn.y
    if y > 0:
        return np.arccos(x)
    else:
        return -np.arccos(x)
    
def theta(p0,p):
    """
    calcule l'angle oriente (p0+pt(delta,0),p) ou delta = dist(p0,p)
    """
    return rad(p) - rad(p0)

def p_a(p0,th,delta):
    """
    calcule le point p tel que dist(p,p0) = delta et theta(p0,p) = th
    """
    p = delta*p_a1(th)
    return(p0+p)

def newton(f,p0,c,eps=10**-4):
    def fun(x,y):
        return (f(x,y)-c)
    def proch(p): #proch joue le role de l'application contractante pour l'application du theoreme du point fixe
        g = grad(f,p)
        return(p - (fun(p.x,p.y)/(g.norme()**2))*g)
    p1 = proch(p0)
    while dist(p0,p1) > eps:
        p0 = p1
        p1 = proch(p1)
    return(p1)

def g(f,p0,theta,d) :
    return f(p0.x+d*np.cos(theta),p0.y+d*np.sin(theta))

def dichotoproch(f,c,delta,ad,d):
    ref = (d - ad) + d
    ang = theta(d + pt(delta,0),ref)
    def rech(th):
        return g(f,d,th-ang,delta)
    a = -np.pi + delta
    b =  np.pi - delta
    while b-a > delta:
        m = (a+b)/2
        if (rech(m)-c)*(rech(a)-c)<=0:
            b = m
        else:
            a = m
    t = (a+b)/2
    return p_a(d,t+ang,delta)

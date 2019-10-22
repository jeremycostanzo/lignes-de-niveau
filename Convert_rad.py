def p_a1(ang):
    """
    Cette fonction calcule le point p sur le cercle unite tel que l'angle oriente (pt(1,0),p) vale ang
    """
    return(pt(np.cos(ang),np.sin(ang)))    

def rad(p):
    """
    Cette fonction calcule l'angle oriente (pt(1,0),p)
    """
    x = p.x
    y = p.y
    if abs(x)>abs(y):
        if y >= 0:
            return(np.arccos(x))
        else:
            return(-np.arccos(x))
    else:
        if x >= 0:
            return(np.arcsin(y))
        else:
            return(np.pi-np.arcsin(y))
    
def theta(p0,p):
    """
    calcule l'angle oriente (p0+pt(delta,0),p) ou delta = dist(p0,p)
    """
    de = dist(p0,p)
    return(rad((1/de)*(p-p0)))

def p_a(p0,th,delta):
    """
    calcule le point p tel que dist(p,p0) = delta et theta(p0,p) = th
    """
    p = delta*p_a1(th)
    return(p0+p)
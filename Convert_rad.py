def p_a1(ang):
    return(pt(np.cos(ang),np.sin(ang)))    

def rad(p):
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
    de = dist(p0,p)
    return(rad((1/de)*(p-p0)))

def p_a(p0,th,delta):
    p = delta*p_a1(th)
    return(p0+p)
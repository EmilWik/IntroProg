
def derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

def solve(f, x0, h): 
    xOld = x0/2
    
    while (abs(x0 - xOld) > h):
        xOld = x0
        x0 = x0 - f(x0) / derivative(f,x0,h)

    return float(x0)
    

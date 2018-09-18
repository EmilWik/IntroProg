<<<<<<< HEAD
def bounce (n):
    print(n)
    if(n != 0):
        bounce(n-1)
        print(n)


def bounce2 (n):
    for i in range(2*n + 1): #+1 för 0
        print(abs(n-i)) #går från n till -n


def tvarsumman(n):
    if n % 10 == n:
        return n
    return int((n % 10) + tvarsumman( (n - (n % 10)) / 10 ))


def tvarsumman2(n):
    nSum = 0
    while(n != 0):
        nSum += (n % 10)
        n = (n - (n % 10)) / 10

    return int(nSum)
    
=======
def bounce (n):
    print(n)
    if(n != 0):
        bounce(n-1)
        print(n)


def bounce2 (n):
    for i in range(2*n + 1): #+1 för 0
        print(abs(n-i)) #går från n till -n


def tvarsumman(n):
    if n % 10 == n:
        return n
    return int((n % 10) + tvarsumman( (n - (n % 10)) / 10 ))


def tvarsumman2(n):
    nSum = 0
    while(n != 0):
        nSum += (n % 10)
        n = (n - (n % 10)) / 10

    return int(nSum)
    
>>>>>>> db010d28339c9f5467a16f41c9e81c79d7bf28f6

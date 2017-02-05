# https://en.wikipedia.org/wiki/Karatsuba_algorithm
# z2 = x0y0
# z0 = x1y1
# z1 = (x0 + x1)*(y0 + y1) - z2 - z0

# result = z2*B^2m + z1*B^m + z0

import math

def multiply(x, y):

    if x < 10 or y < 10:
        return x * y

    nX = int(math.floor(math.log10(x))+1)
    nY = int(math.floor(math.log10(y))+1)

    n = max(nX, nY)

    B = 10
    
    m = int(math.ceil(n / 2.0))

    x0 = x / pow(B, m)
    x1 = x % pow(B, m)
    y0 = y / pow(B, m)
    y1 = y % pow(B, m)

    z2 = multiply(x0, y0)
    z0 = multiply(x1, y1)
    z1 = multiply(x0 + x1, y0 + y1) - z2 - z0

    return z2*pow(B, 2*m) + z1*pow(B, m) + z0
    


myX = 3141592653589793238462643383279502884197169399375105820974944592
myY = 2718281828459045235360287471352662497757247093699959574966967627
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
print("result", multiply(myX, myY))
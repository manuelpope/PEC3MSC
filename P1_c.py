# newton method python

import numpy as np
from scipy import special as sci

def f_x(xi: float):
    return xi * (np.e ** xi)


def f_dev_x(xi: float):
    return (np.e ** xi) * (1 + xi)


def newton_method_i(f_x, f_dev_x, xi: float):
    return xi - (f_x(xi) / f_dev_x(xi))

def iter_newton(n:int,x0:float,f,ff):
    for i in range(0,n):
        print('x0: ', 'n: ')
        print(x0,i)
        xi=newton_method_i(f,ff,x0)
        er= xi-x0
        tolerance = 10**-10
        if(np.absolute(er)<=tolerance):
            print('stop iteration',er,i)
            break
        x0=xi



if __name__ == '__main__':
    a,b = 0.567, 0.852
    n=11
    h=(b-a)/n
    vector_aux =[0.56,0.6,0.63,0.66,0.69,0.72,0.75,0.78,0.8,0.829,0.852]

    vector_i = np.linspace(1,2,11)
    vector_w_ai = list(map(sci.lambertw,vector_i))
    vector_w_ai = [np.round(np.absolute(elem),5) for elem in vector_w_ai]
    print(vector_w_ai)
    for i in vector_w_ai:
        print('iteracion para ' ,i)
        iter_newton(11,i,f_x, f_dev_x)

# newton method python

import numpy as np


def f_x(xi: float):
    return xi * (np.e ** xi)


def f_dev_x(xi: float):
    return (np.e ** xi) * (1 + xi)


def newton_method_i(f_x, f_dev_x, xi: float):
    return xi - (f_x(xi) / f_dev_x(xi))

def iter_newton(n:int,x0:float,f,ff):
    for i in range(0,n):
        #print('x0: ', 'n: ')
        #print(x0,i)
        xi=newton_method_i(f,ff,x0)
        er= xi-x0
        tolerance = 10**-10
        #print(x0)
        if(np.absolute(er)<=tolerance):
           # print('stop iteration',er,i)
            print(i)
            break
        x0=xi



if __name__ == '__main__':
    a,b = 0.567, 0.852
    n=11
    h=(b-a)/n
    vector_aux =[0.56,0.6,0.63,0.66,0.69,0.72,0.75,0.78,0.8,0.829,0.852]

    vector_i = np.linspace(a,b,n)
    print(vector_i)
    for i in vector_aux:
        #print('iteracion para ' ,i)
        iter_newton(100,i,f_x, f_dev_x)

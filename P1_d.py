# chebyshev method python

import numpy as np


def f_x(xi: float):
    return xi * (np.e ** xi)


def f_dev_x(xi: float):
    return (np.e ** xi) * (1 + xi)


def f_dev2_x(xi):
    return (np.e**xi )*(xi+2)


def chebyshev_method_i(f_x, f_dev_x, xi: float):
    return xi - (f_x(xi) / f_dev_x(xi)) - (f_dev2_x(xi)*f_x(xi)**2/(2*f_dev_x(xi)**3))


def iter_chebyshev  (n:int, x0 , f, ff):
    for i in range(0,n):
        #print('xi: ', 'n: ')
       # print(x0)
        xi = chebyshev_method_i(f, ff, x0)
        er = xi - x0
        tolerance = 10 ** -10
        if (np.absolute(er) <= tolerance):
            print(i)
            break

        x0=xi


if __name__ == '__main__':

    a, b = 0.567, 0.852
    n = 11
    h = (b - a) / n
    vector_i = np.linspace(a, b, n)
    vector_aux = [0.56, 0.6, 0.63, 0.66, 0.69, 0.72, 0.75, 0.78, 0.8, 0.829, 0.852]
    for i in vector_aux:
        #print('iteracion para ' ,i)
        iter_chebyshev(110,i,f_x,f_dev_x)

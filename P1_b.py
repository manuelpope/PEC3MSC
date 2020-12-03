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
        print(x0)
        xi=chebyshev_method_i(f,ff,x0)
        x0=xi


if __name__ == '__main__':

    i_vector = np.linspace(1, 2, 11)

    for i in i_vector:
        print('iteracion para ' ,i)
        iter_chebyshev(11,i,f_x,f_dev_x)

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
        print(x0)
        xi=newton_method_i(f,ff,x0)
        x0=xi


if __name__ == '__main__':

    i_vector = np.linspace(1, 2, 11)
    for i in i_vector:
        print('iteracion para ' ,i)
        iter_newton(11,i,f_x, f_dev_x)

#Trapezoidal metodo integracion
import numpy as np

def f_x(xi: float):
    return 1/(np.e ** xi)

def integral_sum(fx,vector):
    vector_value= [fx(elem) for elem in vector]
    return np.array(vector_value).sum()

def analytical_integral(x):
    return (x*f_x(x))-x+np.e**(f_x(x))

def integral_givenb(a,b):
    lowerlimit_value= analytical_integral(a)
    upperlimit_value =analytical_integral(b)
    return upperlimit_value-lowerlimit_value


if __name__ == '__main__':

    a,b = 1,2
    n=11
    h=(b-a)/n
    vector_i = np.linspace(1,2,n)
    first_term = analytical_integral(vector_i[0])
    second_term =2*integral_sum(analytical_integral,vector_i[1:])
    third_term = analytical_integral(vector_i[-1])

    I = integral_givenb(1,2)
    print(I)

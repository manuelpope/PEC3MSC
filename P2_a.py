#Trapezoidal metodo integracion
import numpy as np

def f_x(xi: float):
    return xi*(np.e**xi)


def integral_sum(fx,vector):
    vector_value= [fx(elem) for elem in vector]
    return np.array(vector_value).sum()



if __name__ == '__main__':

    a,b = 0.567, 0.852
    n=1100
    h=(b-a)/n
    vector_i = np.linspace(a,b,n)
    first_term = f_x(vector_i[0])
    second_term =2*integral_sum(f_x,vector_i[1:-1])
    third_term = f_x(vector_i[-1])

    I = (h/2) *(first_term+second_term+third_term)
    print(I)


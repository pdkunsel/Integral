'''
The purpose of this program is to numerically calculate an integral using Simpson's Rule for a given function
'''
import my_library
import function_library


def f(x):            # The variable for the function you wish to integrate
    return x**2

def integral(f, a, b, n, func_params):
    dx = (b-a)/float(n)
    sum1 = 0
    for i in range(1, n/2 +1):     #Computes the partial sum for the odd components
        sum1 += f(a + (2*i - 1)*dx, func_params)
    sum1 *= 4
    sum2 = 0 
    for i in range (1,n/2):            #Computes the partial sum for the even components
        sum2 += f(a + 2*i*dx, func_params)
    sum2 *= 2
    approx = dx/3.0 * (f(a)+f(b)+sum1+sum2)
    return approx

print(integral(f, 0, 1, 1000))

def numerical_integral(left, right, integrand, precision=1e-10):
    m = 2*n
    A = integral(left, right, n)
    B = integral(left, right, m)
    error = float(abs(A-B))
    result = B
    
    while error > precision:
        m = 2*m
        n = 2*n
        A = integral(left, right, n)
        B = integral(left, right, m)
        error = float(abs(A-B))
        result = B

    return result

    
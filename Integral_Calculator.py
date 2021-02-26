from functions_library import *

def f(x):
    return x**2

print(my_power_function_1(1, {"prefactor": 1.0, "power": 2, "x_shift": 0.0, "y_shift": 0.0})) 

def integral(integrand, left_bound, right_bound, npoints, integration_type):
    if integration_type == "simpson":
        dx = (right_bound - left_bound)/float(npoints)
        sum1 = 0
        for i in range(1, npoints/2+1):
            sum1 += integrand(left_bound + (2*i - 1) * dx)
        sum1 *= 4
        sum2 = 0
        for i in range(1,npoints/2):
           sum2 += integrand(left_bound + 2*i*dx)
        sum2 *= 2
        approx = dx/3.0 * (f(left_bound)+f(right_bound)+sum1+sum2)
        return approx
    elif integration_type == "midpoint":
        dx = (right_bound - left_bound)/float(npoints)
        sum = 0
        for i in range(1, npoints):
           sum += integrand((left_bound + dx/2) + i*dx)
        approx = dx * sum
    return approx

print(integral(f, 0, 1, 1000, "simpson"))

def numerical_integral(integrand, left_bound, right_bound, npoints, integration_type, precision = 1e-10):
    if integration_type == "simpson":   
        n = npoints
        m = 2 * npoints
        A = integral(integrand, left_bound, right_bound, n, integration_type)
        B = integral(integrand, left_bound, right_bound, m, integration_type)
        error = float(abs(A-B))
        result = B

        while error > precision:
            n = 2 * n
            m = 2 * m 
            A = integral(integrand, left_bound, right_bound, n, integration_type)
            B = integral(integrand, left_bound, right_bound, m, integration_type)
            error = float(abs(A-B))
            result = B
    
        return result 

print numerical_integral(f, 0, 1, 1000, "simpson",  1e-10)

print numerical_integral(my_power_function_1, 0, 1, 1000, "simpson", 1e-10)

print integral(f, 0, 1, 1000, "midpoint")

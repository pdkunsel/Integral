'''
The purpose of this program is to numerically calculate an integral using Simpson's Rule for a given function
'''

def f(x):            # The variable for the function you wish to integrate
    return 3*x**4

def integral(f, a, b, n):
    dx = (b-a)/float(n)
    sum1 = 0
    for i in range(1, n/2 +1):
        sum1 += f(a + (2*i - 1)*dx)
    sum1 *= 4
    sum2 = 0 
    for i in range (1,n/2):
        sum2 += f(a + 2*i*dx)
    sum2 *= 2
    approx = dx/3.0 * (f(a)+f(b)+sum1+sum2)
    return approx

print(integral(f, 0, 1, 1000))
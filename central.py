t = 1/5
h = 1/4

def f(x, t):
    return 3*t*t - 2*x

def begining_values(x_i, t=0):
    return x_i ** 2 + 1

def approximat_value(u_i, u_j, u_k, f):
    return u_j + (t/(2*h)) * (u_k - u_i) + t * f

def exact_value(x, t):
    return t*t*t + x*x + 1

f = f(0.5, 0)
u_i = begining_values(0.25)
u_j = begining_values(0.5)
u_k = begining_values(0.75)

u_exact = exact_value(0.5, 0.2)

result = approximat_value(u_i, u_j, u_k, f)
print(result)
print(u_exact)
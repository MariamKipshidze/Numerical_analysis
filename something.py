t = 1/8
h = 1/4

def f(x, t):
    return 1-28*t*x - 36*x*x

def a(x, t):
    return 2*x + t

def begining_values(x_i, t=0):
    return 3*x_i*x_i*x_i - 1

def begining_left_values(t, x=1):
    return 2 - 5*t*t + t

def begining_right_values(t, x=2):
    return 23 - 10*t*t + t


def approximat_value(u_i, u_j, u_k, f, a):
    return u_j + (t/(h*h)) * a*(u_k - (2*u_j) + u_i) + t * f

def exact_value(x, t):
    return 3*x*x*x - 5*t*t*x + t -1

f = f(0.5, 0)

u_i = begining_values(0.25)
u_j = begining_values(0.5)
u_k = begining_values(0.75)

a = a(0.5, 0)

u_exact = exact_value(0.5, 0.125)

result = approximat_value(u_i, u_j, u_k, f, a)

print(result)
print(u_exact)
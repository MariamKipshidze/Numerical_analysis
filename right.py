t = 1/5
h = 1/4

def f(x, t):
    return 2*(t+x)

def begining_values(x_i, t=1):
    return -(x_i * x_i) + 2

def approximat_value(u_i, u_j, f):
    return u_i + t/h * (u_j - u_i) + (t * f)

def exact_value(x, t):
    return t*t*t + x*x + 1

f = f(0.25, 1)
u_i = begining_values(0.25)
u_j = begining_values(0.5)

u_exact = exact_value(0.5, 0.2)

result = approximat_value(u_i, u_j, f)
print(result)
# print(u_exact)
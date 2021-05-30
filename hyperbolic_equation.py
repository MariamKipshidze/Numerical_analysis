h = 1/4
tau = 1/32

t_0 = 0 # [0, 1/2]
x_0 = 0 # [0, 1]

def begining_values_0(x, t=0):
    return 2*x-3-2*x**3

def beginig_values_1(x, t=0):
    return 1

def beginig_values_2(x, t=0):
    return -12*x


def fun(x, t):
    return 18*t*x+12*x

def u(x, f_0, f_1, f_2, f, t=1):
    return f_0+tau*f_1+(tau*tau/2)*(f_2+f)


def approximat_value(u_i, u_j, u_k, u_j_o, f):
    return 2*u_j-u_j_o+(tau**2/h**2)*(u_k-2*u_j+u_i)+tau**2*f

def exact_value(x, t):
    return (2*x +t -3)+3*t**3*x-2*x**3


u_j_o = begining_values_0(x_0+h*2) # (2,0)

f = fun(x=1/4, t=0)
f_0 = begining_values_0(1/4)
f_1 = beginig_values_1(1/4)
f_2 = beginig_values_2(1/4)

u_i = u(x=1/4, f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (1,1)

f = fun(x=1/2, t=0)
f_0 = begining_values_0(1/2)
f_1 = beginig_values_1(1/2)
f_2 = beginig_values_2(1/2)

u_j = u(x=1/2, f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (2,1)

f = fun(x=3/4, t=0)
f_0 = begining_values_0(3/4)
f_1 = beginig_values_1(3/4)
f_2 = beginig_values_2(3/4)

u_k = u(x=3/4, f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (3,1)

f = fun(x_0+h*2, t_0+tau*1) # (2,1)

print(f)
print(u_j_o)
print(u_i)
print(u_j)
print(u_k)

print("=====================================")

# print(approximat_value(-2.5,-2.21875, -2.3125, -2.25, 6.28125))
# print(approximat_value(-5/2, -71/32, -37/16, -9/4, 201/32))
print(f"approximat value: {approximat_value(u_i, u_j, u_k, u_j_o, f)}")
print(f"exact_value: {exact_value(1/2, 1/16)}")

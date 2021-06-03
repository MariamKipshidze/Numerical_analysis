h = 1/4
tau = 1/32

t_0 = 0 # [0, 1/2]
x_0 = 0 # [0, 1]

t = 2

#          (2,2)
#            |
#            | (2,1)
# (1,1)------o---------(3,1)
#            |
#            | 
#          (2, 0)


#            (i,j+1)
#              |
#              | (i,j)
# (i-1,j)------o---------(i+1,j)
#              |
#              | 
#            (i, j-1)


def begining_values_0(i, j=0):            # u(x, 0)
    return 2*(x_0+i*h)-3-2*(x_0+i*h)**3  

def beginig_values_1(i, j=0):             # u'(x, 0) (with t)
    return 1

def beginig_values_2(i, j=0):             # u"(x, 0) (with x)
    return -12*(x_0+i*h)

# //////////////////////////////////////////////////////

def beginig_left_values(j, i=0):
    return tau*j - 3

def beginig_right_values(j, i=4):
    return -3 + tau*j + 3*(tau*j)**3

# //////////////////////////////////////////////////////

def fun(i, j):
    return 18*(t_0+tau*j)*(x_0+h*i)+12*(x_0+h*i)

def u(f_0, f_1, f_2, f):
    return f_0+tau*f_1+(tau*tau/2)*(f_2+f)

# ///////////////////////////////////////////////////////

def approximat_value(u_i, u_j, u_k, u_j_o, f):
    return 2*u_j-u_j_o+(tau**2/h**2)*(u_k-2*u_j+u_i)+tau**2*f

def exact_value(i, j):
    return (2*(x_0+i*h)+(t_0+tau*j)-3)+3*(t_0+tau*j)**3*(x_0+i*h)-2*(x_0+i*h)**3


for x in range(0, 5):
    if x == 0:
        print(f"approximat value({x}, 2): {beginig_left_values(t)}")
        print(f"exact_value({x}, 2): {exact_value(x, t)}")

    elif x == 4:
        print("=====================================")
        print(f"approximat value({x}, 2): {beginig_right_values(t)}")
        print(f"exact_value({x}, 2): {exact_value(x, t)}")

    else:
        u_j_o = begining_values_0(x, t-2) # (2,0)

        f = fun(x-1,t-2)
        f_0 = begining_values_0(x-1) # (1,0)
        f_1 = beginig_values_1(x-1)
        f_2 = beginig_values_2(x-1)

        if x == 1:
            u_i = beginig_left_values(t-1)
        else:
            u_i = u(f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (1,1)

        f = fun(x,t-2)
        f_0 = begining_values_0(x) # (2,0)
        f_1 = beginig_values_1(x)
        f_2 = beginig_values_2(x)

        u_j = u(f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (2,1)

        f = fun(x+1,t-2)
        f_0 = begining_values_0(x+1) # (3,0)
        f_1 = beginig_values_1(x+1)
        f_2 = beginig_values_2(x+1)

        if x == 3:
            u_k = beginig_right_values(t-1)
        else:
            u_k = u(f_0=f_0, f_1=f_1, f_2=f_2, f=f) # (3,1)

        f = fun(x,t-1) # (2,1)

        # print(f)
        # print(u_j_o)
        # print(u_i)
        # print(u_j)
        # print(u_k)

        print("=====================================")

        # print(approximat_value(-2.5,-2.21875, -2.3125, -2.25, 6.28125))
        # print(approximat_value(-5/2, -71/32, -37/16, -9/4, 201/32))
        print(f"approximat value({x}, 2): {approximat_value(u_i, u_j, u_k, u_j_o, f)}")
        print(f"exact_value({x}, 2): {exact_value(x, t)}")

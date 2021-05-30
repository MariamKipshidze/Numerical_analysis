h = 1 / 4
t = 1 / 8
x_0 = 1
t_0 = 1


def f(x, t):
    return 1 - 28 * t * x - 36 * x * x


def a(x, t):
    return 2 * x + t


def begining_values(x_i, t=1):  ### u(x)
    return 3 * (x_i + x_0)**3 - 5 * (x_i + x_0)


def exact_value(x, t):
    return 3 * x * x * x - 5 * t * t * x + t - 1


#########################################################


def approximat_value(u_i, u_j, u_k, f, a):
    return u_j + (t / (h * h)) * a * (u_k - (2 * u_j) + u_i) + t * f


for i in range(1, 5):
    u_i = begining_values(i * h - h)
    u_j = begining_values(i * h)
    u_k = begining_values(i * h + h)

    b = a(x_0 + i * h, t_0)
    func = f(x_0 + i * h, t_0)

    result = approximat_value(u_i, u_j, u_k, func, b)
    u_exact = exact_value(x_0 + i * h, t_0 + t)

    print(
        f' y[{i}][1]={result}, u_zusti={u_exact}, cdomileba={abs(u_exact-result)}'
    )

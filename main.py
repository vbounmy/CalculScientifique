import numpy

def f(x):
    return x**2 - 8 * numpy.log(x) #x**2 = x puissance 2

def solve_equation(f, left, right, precision=10**(-3)):
    while right - left >= precision:
        middle = (right + left) / 2

        if f(middle) == 0:
            print(middle)
            break

        elif f(left) * f(middle) < 0: #ça veut dire que left et middle ont des signes diff
            right = middle

        elif f(right) * f(middle) < 0: #ça veut dire que right et middle ont des signes diff
            left = middle

    return middle

def plot_function()

if __name__ == "__main__":
    x = numpy.array([1, 2, 3])
    y = f(x)
    middle = solve_equation(f, 1, 2)
    print(middle)
    print(f(middle))
import numpy

def f(x):
    return x**2 - 8 * numpy.log(x) #x**2 = x puissance 2

x = numpy.array([1, 2, 3])
y = f(x)
#y = [f(1), f(2), f(3)] >> ce qui va être affiché 

print(y)

left = 1
right = 2
precision = 10**(-3)

while right - left >= precision:
    middle = (right + left) / 2

    if f(middle) == 0:
        print(middle)
        break

    elif f(left) * f(middle) < 0: #ça veut dire que left et middle ont des signes diff
        right = middle

    elif f(right) * f(middle) < 0: #ça veut dire que right et middle ont des signes diff
        left = middle

print(middle)
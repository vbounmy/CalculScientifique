import numpy
import matplotlib.pyplot as plt
from config_file import *

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

def plot_function(f, start, end, step=0.01): #si on met un pas ça sera + précis car la précision sera constante peu importe la taille de l'intervalle
    x = numpy.arange(start, end, step)
    y = f(x)

    plt.figure(figsize=(LENGTH, HEIGHT)) #15 en largeur et 6 en longueur
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    plot_function(f, start=0.01, end=5, step=0.01)
    # middle = solve_equation(f, 1, 2)
    # print(middle)
    # print(f(middle))
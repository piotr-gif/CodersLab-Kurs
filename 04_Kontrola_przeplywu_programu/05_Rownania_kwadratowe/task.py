print("a*x**2 + b*x + c == 0")
print("Podaj a")
a = float(input())
print("Podaj b")
b = float(input())
print("Podaj c")
c = float(input())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("brak rozwiązań")
elif delta == 0:
    x_1 = x_2 = -b / (2*a)
    print("Pierwiastki równania kwadratowego:")
    print("x_1 = x_2 = {}".format(x_1))
else:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print("Pierwiastki równania kwadratowego:")
    print("x_1 = {}".format(x_1))
    print("x_2 = {}".format(x_2))
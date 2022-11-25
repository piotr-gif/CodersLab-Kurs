numbers = []
print("Podaj n: ")
n = int(input())
ans = 0
for i in range(n):
    print("Podaj liczbę: ")
    a = int(input())
    numbers.append(a)
    ans += a
print("Wprowadzone liczby: ")
for number in numbers:
    print(str(number) + " ")
print("Suma: {}".format(ans))
print("Średnia: {}".format(ans/n))
if ans > ans / n:
    print("Suma jest większa!")
else:
    print("Średnia jest większa!")
def read(a):
    with open(a, 'r') as f:
        mass = []
        for i in f.read().split():
            mass.append(int(i))
    return mass


def minimum(m):
    mini = m[0]
    for i in range(1, len(m)):
        if m[i] < mini:
            mini = m[i]
    return mini


def maximum(m):
    maxi = m[0]
    for i in range(1, len(m)):
        if m[i] > maxi:
            maxi = m[i]
    return maxi


def summa(m):
    suma = 0
    for i in m:
        suma += i
    return suma


def product(m):
    pr = 1
    for i in m:
        pr *= i
    return pr


if __name__ == '__main__':
    print("В файле:", *read('input.txt'))
    print("Минимальное:", minimum(read('input.txt')))
    print("Максимальное:", maximum(read('input.txt')))
    print("Сумма:", summa(read('input.txt')))
    print("Произведение:", product(read('input.txt')))

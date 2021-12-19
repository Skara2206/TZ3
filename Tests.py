import unittest
import time
from random import randint
from main import minimum, maximum, summa, product, read
from functools import reduce
from operator import mul


class Test(unittest.TestCase):
    def test_random_array(self, x, y, z):
        a = []
        for i in range(x):
            a.append(randint(y, z))
        return a

    def test_minimum(self):
        a1 = self.random_array(50000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(minimum(a1), min(a1), "Неправильное значение миниимума")
        ftime = time.time()
        time1 = ftime-sttime

        a1 = self.random_array(500000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(minimum(a1), min(a1), "Неправильное значение минимума")
        ftime = time.time()
        time2 = ftime - sttime

        testValue = time2 - time1 >= 0.5 * time2
        self.assertTrue(testValue, "Функция минимума тест на время не прошла")

    def test_maximum(self):
        a1 = self.random_array(50000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(maximum(a1), max(a1), "Неправильное значение максимума")
        ftime = time.time()
        time1 = ftime - sttime

        a1 = self.random_array(500000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(maximum(a1), max(a1), "Неправильное значение максимума")
        ftime = time.time()
        time2 = ftime - sttime

        testValue = time2 - time1 >= 0.5 * time2
        self.assertTrue(testValue, "Функция максимума тест на время не прошла")

    def test_summa(self):
        a1 = self.random_array(50000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(summa(a1), sum(a1), "Неправильное значение суммы")
        ftime = time.time()
        time1 = ftime - sttime

        a1 = self.random_array(500000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(summa(a1), sum(a1), "Неправильное значение суммы")
        ftime = time.time()
        time2 = ftime - sttime

        testValue = time2 - time1 >= 0.5 * time2
        self.assertTrue(testValue, "Функция суммы тест на время не прошла")

    def test_product(self):
        a1 = self.random_array(500, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(product(a1), reduce(mul, a1), "Неправильное значение произведения")
        ftime = time.time()
        time1 = ftime - sttime

        a1 = self.random_array(5000, 50000000, 100000000)
        sttime = time.time()
        self.assertEqual(product(a1), reduce(mul, a1), "Неправильное значение произведения")
        ftime = time.time()
        time2 = ftime - sttime
        testValue = 0 <= time2 - time1 <= time2
        self.assertTrue(testValue, "Функция произведения тест на время не прошла")

    def test_readtime(self):
        sttime = time.time()
        read("input.txt")
        ftime = time.time()
        time1 = ftime - sttime

        sttime = time.time()
        read("Biginput.txt")
        ftime = time.time()
        time2 = ftime - sttime

        testValue = time2 >= time1
        self.assertTrue(testValue, "Функция считывания данных из файла тест на время не прошла")

    def test_correct(self):
        try:
            read("input.txt")
            print("Файл считывается без ошибок")
            print("Кроме того, не возникнит ошибки переполнения,"
                  "так как функция read выдаёт ошибку, если какое-то из считываемых чисел не целое."
                  "А если все числа целые, то ошибки переполнения быть не может")
        except ValueError:
            print("В файле содержатся недопустимые символы")
        return


if __name__ == '__main__':
    unittest.main()

import math
from abstractFunctions import AbstractFuncts

class IterativeFuncts(AbstractFuncts):
    @staticmethod
    def exponentiation(a, b):
        pow = 1
        if b > 0:
            for i in range(b):
                pow *= a
        elif b < 0:
            for i in range(abs(b)):
                pow *= 1 / a
        
        return pow


    @staticmethod
    def string_reversal(string):
        string = list(string)

        for i in range(len(string) // 2):
            temp = string[i]
            string[i] = string[len(string) - 1 - i]
            string[len(string) - 1 - i] = temp

        return "".join(string)


    @staticmethod
    def fibonacci(n):
        nmin2 = 0
        nmin1 = 1

        if n == 0:
            return nmin2
        elif n == 1:
            return nmin1
        else:
            for i in range(1, n, 1):
                fib = nmin1 + nmin2
                nmin2 = nmin1
                nmin1 = fib
            
            return fib

    # dont work
    @staticmethod
    def is_palindrome(word):
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - 1 - i]:
                return False
            
        return True


    @staticmethod
    def gcd(x, y):
        x = abs(x)
        y = abs(y)

        if y > x:
            working_arr = [y, x]
        else:
            working_arr = [x, y]

        while working_arr[1] != 0:
            temp = working_arr[0]
            working_arr[0] = working_arr[1]
            working_arr[1] = temp % working_arr[1]
        
        return working_arr[0]
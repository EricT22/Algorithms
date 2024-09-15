from abstractFunctions import AbstractFuncts


# TODO: Have to put the comments the prof wanted in the code

class RecursiveFuncts(AbstractFuncts):
    @staticmethod
    def exponentiation(a, b):
        if b > 0:
            if b == 1:
                return a
            else:
                return a * RecursiveFuncts.exponentiation(a, b - 1)
        elif b < 0:
            if b == -1:
                return 1 / a
            else:
                return 1 / a * RecursiveFuncts.exponentiation(a, b + 1)
        else:
            return 1


    @staticmethod
    def string_reversal(string):
        if len(string) == 2:
            return string[1] + string[0]
        elif len(string) == 1:
            return string
        
        return string[len(string) - 1] + RecursiveFuncts.string_reversal(string[1 : len(string) - 1]) + string[0]


    @staticmethod
    def fibonacci(n):
        # Direct solution is 0 for F(0) and 1 for F(1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Combination is the sum of the two previous Fibonacci numbers
        # Subdivision is reducing n by one and also by 2
        # The two fibonacci calls are the recurrence
        return RecursiveFuncts.fibonacci(n - 1) + RecursiveFuncts.fibonacci(n - 2)


    @staticmethod
    def is_palindrome(word):
        if len(word) == 2:
            return word[0] == word[1]
        elif len(word) == 1:
            return True

        return word[0] == word[len() - 1] and RecursiveFuncts.is_palindrome(word[1 : len(word - 1)])


    @staticmethod
    def gcd(x, y):
        x = abs(x)
        y = abs(y)

        if y > x:
            return RecursiveFuncts.gcd(y, x)
        elif y == 0:
            return x
        else:
            return RecursiveFuncts.gcd(y, x % y)
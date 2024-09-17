from abstractFunctions import AbstractFuncts

class RecursiveFuncts(AbstractFuncts):
    @staticmethod
    def exponentiation(a:int, b:int):
        if b > 0:
            if b == 1:
                # Direct solution is a when b = 1
                return a
            else:
                # Recombination is the multiplication
                # Subdivision is b - 1
                # The call to exponentiation is the recurrence
                return a * RecursiveFuncts.exponentiation(a, b - 1)
        elif b < 0:
            if b == -1:
                # Direct solution is 1/a when b = -1
                return 1 / a
            else:
                # Recombination is the multiplication
                # Subdivision is b + 1
                # The call to exponentiation is the recurrence
                return 1 / a * RecursiveFuncts.exponentiation(a, b + 1)
        else:
            # Direct solution is 1 when b = 0
            return 1


    @staticmethod
    def string_reversal(string):
        # Direct solution depends on the length of the starting word
        # If it is even, the direct solution reverses the remaining two letters
        # If it is odd, only one letter remains, so it's returned
        if len(string) == 2:
            return string[1] + string[0]
        elif len(string) == 1:
            return string
        
        # Recombination is adding the substrings together
        # Subdivision is reducing the length of the word by two (chopping first and last letters off)
        # The call to string_reversal is the recurrence
        return string[len(string) - 1] + RecursiveFuncts.string_reversal(string[1 : len(string) - 1]) + string[0]


    @staticmethod
    def fibonacci(n):
        # Direct solution is 0 for F(0) and 1 for F(1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Recombination is the sum of the two previous Fibonacci numbers
        # Subdivision is reducing n by one and also by 2
        # The two fibonacci calls are the recurrence
        return RecursiveFuncts.fibonacci(n - 1) + RecursiveFuncts.fibonacci(n - 2)


    @staticmethod
    def is_palindrome(word):
        # Direct solution depends on the length of the starting word
        # If it is even, the direct solution checks the equality between the remaining two letters
        # If it is odd, only one letter remains, so the result must be true
        if len(word) == 2:
            return word[0] == word[1]
        elif len(word) == 1:
            return True

        # Recombination is the logical operator and
        # Subdivision is reducing the length of the word by two (chopping first and last letters off)
        # The call to is_palindrome is the recurrence
        return word[0] == word[len(word) - 1] and RecursiveFuncts.is_palindrome(word[1 : len(word) - 1])


    @staticmethod
    def gcd(x, y):
        x = abs(x)
        y = abs(y)

        if y > x:
            return RecursiveFuncts.gcd(y, x)
        elif y == 0:
            # Direct solution is x when y = 0
            return x
        else:
            # Recombination is the swapping of parameter values (x for y and y for the subdivision)
            # Subdivision is the modulus of x by y
            # The call to gcd is the recurrence
            return RecursiveFuncts.gcd(y, x % y)
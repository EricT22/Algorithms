from recursiveFunctions import RecursiveFuncts
from iterativeFunctions import IterativeFuncts

if __name__ == "__main__":
    # exponentiation
    a, b = 3, 2
    print(RecursiveFuncts.exponentiation(a, b))


    a, b = 3, -3
    print(RecursiveFuncts.exponentiation(a, b))
    

    a, b = -3, 5
    print(RecursiveFuncts.exponentiation(a, b))


    print("-------------------------------------")
    # string reversal
    string = "Bob!"
    print(RecursiveFuncts.string_reversal(string))


    string = "palooza"
    print(RecursiveFuncts.string_reversal(string))

    string = "1racecar1"
    print(RecursiveFuncts.string_reversal(string))


    print("-------------------------------------")
    # fibonacci
    n = 3
    print(RecursiveFuncts.fibonacci(n))


    n = 8
    print(RecursiveFuncts.fibonacci(n))

    n = 1
    print(RecursiveFuncts.fibonacci(n))


    print("-------------------------------------")
    # palindrome
    string = "Bob"
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")


    string = "palooza"
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")

    string = "1racecar1"
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")


    print("-------------------------------------")
    # Greatest Common Divisor
    x, y = 4, 2
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")

    x, y = 1465, 1172
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")

    x, y = 12, 48
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")
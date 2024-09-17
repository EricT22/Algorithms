from recursiveFunctions import RecursiveFuncts
from iterativeFunctions import IterativeFuncts

if __name__ == "__main__":
    # exponentiation
    a, b = 3, 2
    print("Recursion:")
    print(RecursiveFuncts.exponentiation(a, b))
    print("Iteration:")
    print(IterativeFuncts.exponentiation(a, b))

    a, b = 3, -3
    print("Recursion:")
    print(RecursiveFuncts.exponentiation(a, b))
    print("Iteration:")
    print(IterativeFuncts.exponentiation(a, b))

    a, b = -3, 5
    print("Recursion:")
    print(RecursiveFuncts.exponentiation(a, b))
    print("Iteration:")
    print(IterativeFuncts.exponentiation(a, b))


    print("-------------------------------------")
    # string reversal
    string = "Bob!"
    print("Recursion:")
    print(RecursiveFuncts.string_reversal(string))
    print("Iteration:")
    print(IterativeFuncts.string_reversal(string))

    string = "palooza"
    print("Recursion:")
    print(RecursiveFuncts.string_reversal(string))
    print("Iteration:")
    print(IterativeFuncts.string_reversal(string))

    string = "1racecar1"
    print("Recursion:")
    print(RecursiveFuncts.string_reversal(string))
    print("Iteration:")
    print(IterativeFuncts.string_reversal(string))



    print("-------------------------------------")
    # fibonacci
    n = 3
    print("Recursion:")
    print(RecursiveFuncts.fibonacci(n))
    print("Iteration:")
    print(IterativeFuncts.fibonacci(n))

    n = 8
    print("Recursion:")
    print(RecursiveFuncts.fibonacci(n))
    print("Iteration:")
    print(IterativeFuncts.fibonacci(n))

    n = 1
    print("Recursion:")
    print(RecursiveFuncts.fibonacci(n))
    print("Iteration:")
    print(IterativeFuncts.fibonacci(n))


    print("-------------------------------------")
    # palindrome
    string = "Bob"
    print("Recursion:")
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")
    print("Iteration:")
    print(f"{string} is a palindrome?: ", IterativeFuncts.is_palindrome(string), sep="")

    string = "palooza"
    print("Recursion:")
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")
    print("Iteration:")
    print(f"{string} is a palindrome?: ", IterativeFuncts.is_palindrome(string), sep="")

    string = "1racecar1"
    print("Recursion:")
    print(f"{string} is a palindrome?: ", RecursiveFuncts.is_palindrome(string), sep="")
    print("Iteration:")
    print(f"{string} is a palindrome?: ", IterativeFuncts.is_palindrome(string), sep="")


    print("-------------------------------------")
    # Greatest Common Divisor
    x, y = 4, 2
    print("Recursion:")
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")
    print("Iteration:")
    print(f"GCD between {x} and {y}: ", IterativeFuncts.gcd(x, y), sep="")

    x, y = 1465, 1172
    print("Recursion:")
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")
    print("Iteration:")
    print(f"GCD between {x} and {y}: ", IterativeFuncts.gcd(x, y), sep="")

    x, y = 12, 48
    print("Recursion:")
    print(f"GCD between {x} and {y}: ", RecursiveFuncts.gcd(x, y), sep="")
    print("Iteration:")
    print(f"GCD between {x} and {y}: ", IterativeFuncts.gcd(x, y), sep="")

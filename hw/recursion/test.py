from recursiveFunctions import RecursiveFuncts
from iterativeFunctions import IterativeFuncts

if __name__ == "__main__":
    # exponentiation
    a, b = 3, 2
    print("Recursion:")
    print(f'{a}^{b} = ', RecursiveFuncts.exponentiation(a, b), sep="")
    print("Iteration:")
    print(f'{a}^{b} = ', IterativeFuncts.exponentiation(a, b), sep="")

    a, b = 3, -3
    print("Recursion:")
    print(f'{a}^{b} = ', RecursiveFuncts.exponentiation(a, b), sep="")
    print("Iteration:")
    print(f'{a}^{b} = ', IterativeFuncts.exponentiation(a, b), sep="")

    a, b = -3, 5
    print("Recursion:")
    print(f'{a}^{b} = ', RecursiveFuncts.exponentiation(a, b), sep="")
    print("Iteration:")
    print(f'{a}^{b} = ', IterativeFuncts.exponentiation(a, b), sep="")


    print("-------------------------------------")
    # string reversal
    string = "Bob!"
    print("Recursion:")
    print(f'{string} reversed is: ', RecursiveFuncts.string_reversal(string), sep="")
    print("Iteration:")
    print(f'{string} reversed is: ', IterativeFuncts.string_reversal(string), sep="")

    string = "palooza"
    print("Recursion:")
    print(f'{string} reversed is: ', RecursiveFuncts.string_reversal(string), sep="")
    print("Iteration:")
    print(f'{string} reversed is: ', IterativeFuncts.string_reversal(string), sep="")

    string = "1racecar1"
    print("Recursion:")
    print(f'{string} reversed is: ', RecursiveFuncts.string_reversal(string), sep="")
    print("Iteration:")
    print(f'{string} reversed is: ', IterativeFuncts.string_reversal(string), sep="")



    print("-------------------------------------")
    # fibonacci
    n = 3
    print("Recursion:")
    print(f'F({n}) is: ', RecursiveFuncts.fibonacci(n), sep="")
    print("Iteration:")
    print(f'F({n}) is: ', IterativeFuncts.fibonacci(n), sep="")

    n = 8
    print("Recursion:")
    print(f'F({n}) is: ', RecursiveFuncts.fibonacci(n), sep="")
    print("Iteration:")
    print(f'F({n}) is: ', IterativeFuncts.fibonacci(n), sep="")

    n = 1
    print("Recursion:")
    print(f'F({n}) is: ', RecursiveFuncts.fibonacci(n), sep="")
    print("Iteration:")
    print(f'F({n}) is: ', IterativeFuncts.fibonacci(n), sep="")


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

from abc import ABC, abstractmethod

class AbstractFuncts(ABC):
    @staticmethod
    @abstractmethod
    def exponentiation(a, b):
        pass


    @staticmethod
    @abstractmethod
    def string_reversal(str):
        pass


    @staticmethod
    @abstractmethod
    def fibonacci(n):
        pass


    @staticmethod
    @abstractmethod
    def is_palindrome(word):
        pass


    @staticmethod
    @abstractmethod
    def gcd(x, y):
        pass
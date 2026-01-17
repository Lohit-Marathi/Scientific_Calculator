"""
scientific.py

Defines scientific and advanced arithmetic operations.
"""
import math

class ScientificOperations:
    """Encapsulates scientific arithmetic operations."""

    def power(self, base: float, exponent: float) -> float:
        """Returns base raised to the power of exponent."""
        return math.pow(base, exponent)
    

    def square_root(self, value: float) -> float:
        """Returns the square root of a value.
        
        Raises:
            ValueError: if value is negative."""
        if value <= 0:
            raise ValueError("Square root of negative number is not allowed")
        return math.sqrt(value)
    

    def logarithm(self, value: float, base: float = 10) -> float:
        """Returns the Logarithm of a value with given base.

        Raises:
            ValueError: if value is not positive"""
        if value <= 0:
            raise ValueError("Logarithm of non-positive number is not allowed")
        return math.log(value, base)
    

    def natural_log(self, value: float) -> float:
        """Returns the Natural Logarithm (base e) of a value.
        
        Raises: 
            ValueError: if value is not positive"""
        if value <=0:
            raise ValueError("Natural log input must be positive")
        return math.log(value)
    

    def sine(self, degrees: float) -> float:
        """Returns the sine of an angle in degrees."""
        return math.sin(math.radians(degrees))
    

    def cosine(self, degrees: float) -> float:
        """Returns the cosine of an angle in degrees."""
        return math.cos(math.radians(degrees))
    

    def tangent(self, degrees: float) -> float:
        """Returns the tangent of an angle in degrees."""
        return math.tan(math.radians(degrees))
    

    def factorial(self, n: int) -> int:
        """Returns the factorial of a positive integer.
        
        Raises:
            ValueError: if n is negative"""
        if n < 0:
            raise ValueError("Factorial of negative number is not allowed")
        return math.factorial(n)
    

    def absolute(self, value: float) -> float:
        """Returns the absolute value."""
        return abs(value)
    

    def exponential(self, exponent: float) -> float:
        """Returns the exponential of a number (e^exponent)."""
        return math.exp(exponent)
    

    def ceiling(self, value: float) -> int:
        """Returns the smallest integer greater than or equal to value."""
        return math.ceil(value)
    

    def floor(self, value: float) -> int:
        """Returns the largest integer less than or equal to value."""
        return math.floor(value)

"""
basic.py

Defines basic arithmetic operations. 
This module contains no input/output logic.
"""

class BasicOperations:
    """Encapsulates basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b
    
    def substract(self, a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Returns the quotient two numbers.
        
        Raises:
            ValueError: if b is zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    
    def modulo(self, a: float, b: float) -> float:
        """Returns the remainder of a divided by b.

        Raises:
            ValueError: if b is zero."""
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        return a % b
    
    def percentage(self, value: float, percent: float) -> float:
        """Returns the percentage of a value."""
        return (value * percent) / 100


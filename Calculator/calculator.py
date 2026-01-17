"""
calculator.py

defines the calculator engine which composes all operations.
"""

from Calculator.basic import BasicOperations
from Calculator.scientific import ScientificOperations
from typing import List,Tuple

class Calculator:
    """
    Core calculator enigne
    
    this class aggregates basic and scientific operations, 
    and acts like a single access point for the UI layer.
    Includes calculation history tracking."""

    def __init__(self) -> None:
        self.basic = BasicOperations()
        self.scientific = ScientificOperations()
        self._history: List[Tuple[str, float]] = []
        self._max_history = 10


    def add_to_history(self, operation: str, result: float) -> None:
        """ Add a calculation to history.
        
        Args:
            operation (str): String describing the operation.
            result (float): The calculation result."""
        self._history.append((operation, result))
        #Keeps only the last max_history entries 
        if len(self._history)  > self._max_history:
            self._history.pop(0)


    def get_history(self) -> List[Tuple[str, float]]:
        """ Returns the calculation history.
        
        Returns:
            List[Tuple[str, float]]: List of operation descriptions and results."""
        return self._history.copy()
    

    def clear_history(self) -> None:
        """Clears the calculation history."""
        self._history.clear()


    def has_history(self) -> bool: 
        """Checks if there is any calculation history."""
        return len(self._history) > 0
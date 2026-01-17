"""
menu.py

Command line interface for the Scientific Calculator.
"""

from calculator import Calculator

class CalculatorCLI:
    """handles command line interaction for the calculator."""
    def __init__(self) -> None:
        self.calculator = Calculator()


    
    def display_menu(self) -> None:
        """Display the calculator menu."""
        print("\n" + "=" * 50)
        print("           SCIENTIFIC CALCULATOR")
        print("=" * 50)
        print("\nBASIC OPERATIONS:")
        print("  1. Add")
        print("  2. Subtract")
        print("  3. Multiply")
        print("  4. Divide")
        print("  5. Modulo (%)")
        print("  6. Percentage")
        print("\nSCIENTIFIC OPERATIONS:")
        print("  7. Power (x^y)")
        print("  8. Square Root (√x)")
        print("  9. Logarithm (log)")
        print(" 10. Natural Log (ln)")
        print(" 11. Sine (sin)")
        print(" 12. Cosine (cos)")
        print(" 13. Tangent (tan)")
        print(" 14. Factorial (n!)")
        print(" 15. Absolute Value (|x|)")
        print(" 16. Exponential (e^x)")
        print(" 17. Ceiling")
        print(" 18. Floor")
        print("\nUTILITY:")
        print("  h. View History")
        print("  c. Clear History")
        print("  0. Exit")
        print("=" * 50)


    
    def display_history(self) -> None:
        """Display calculation history."""
        if not self.calculator.has_history():
            print("\nNo calculation history yet.")
            return

        print("\n" + "-" * 50)
        print("CALCULATION HISTORY:")
        print("-" * 50)
        for idx, (operation, result) in enumerate(self.calculator.get_history(), 1):
            print(f"{idx}. {operation} = {result}")
        print("-" * 50)

    def run(self) -> None:
        """Run the CLI event loop."""
        while True:
            self.display_menu()
            choice = input("\nChoose an option: ").strip()

            try:
                if choice == "0":
                    print("\n✓ Exiting calculator. Goodbye!")
                    break

                elif choice.lower() == "h":
                    self.display_history()
                    input("\nPress Enter to continue...")
                    continue

                elif choice.lower() == "c":
                    self.calculator.clear_history()
                    print("\n✓ History cleared successfully!")
                    input("\nPress Enter to continue...")
                    continue

                # Basic operations (two numbers)
                elif choice in {"1", "2", "3", "4", "5", "6"}:
                    a, b = self._get_two_numbers()
                    
                    operations = {
                        "1": (self.calculator.basic.add, f"{a} + {b}"),
                        "2": (self.calculator.basic.subtract, f"{a} - {b}"),
                        "3": (self.calculator.basic.multiply, f"{a} × {b}"),
                        "4": (self.calculator.basic.divide, f"{a} ÷ {b}"),
                        "5": (self.calculator.basic.modulo, f"{a} % {b}"),
                        "6": (self.calculator.basic.percentage, f"{b}% of {a}"),
                    }
                    
                    func, operation_str = operations[choice]
                    result = func(a, b)
                    self.calculator.add_to_history(operation_str, result)

                # Power
                elif choice == "7":
                    base = self._get_number("Enter base: ")
                    exp = self._get_number("Enter exponent: ")
                    result = self.calculator.scientific.power(base, exp)
                    self.calculator.add_to_history(f"{base}^{exp}", result)

                # Square root
                elif choice == "8":
                    x = self._get_number()
                    result = self.calculator.scientific.square_root(x)
                    self.calculator.add_to_history(f"√{x}", result)

                # Logarithm
                elif choice == "9":
                    x = self._get_number()
                    base = self._get_number("Enter base (default 10): ", default=10)
                    result = self.calculator.scientific.logarithm(x, base)
                    self.calculator.add_to_history(f"log{base}({x})", result)

                # Natural log
                elif choice == "10":
                    x = self._get_number()
                    result = self.calculator.scientific.natural_log(x)
                    self.calculator.add_to_history(f"ln({x})", result)

                # Trigonometric functions
                elif choice in {"11", "12", "13"}:
                    angle = self._get_number("Enter angle in degrees: ")
                    
                    trig_operations = {
                        "11": (self.calculator.scientific.sine, "sin"),
                        "12": (self.calculator.scientific.cosine, "cos"),
                        "13": (self.calculator.scientific.tangent, "tan"),
                    }
                    
                    func, name = trig_operations[choice]
                    result = func(angle)
                    self.calculator.add_to_history(f"{name}({angle}°)", result)

                # Factorial
                elif choice == "14":
                    n = int(input("Enter an integer: "))
                    result = self.calculator.scientific.factorial(n)
                    self.calculator.add_to_history(f"{n}!", result)

                # Single number operations
                elif choice in {"15", "16", "17", "18"}:
                    x = self._get_number()
                    
                    single_operations = {
                        "15": (self.calculator.scientific.absolute, f"|{x}|"),
                        "16": (self.calculator.scientific.exponential, f"e^{x}"),
                        "17": (self.calculator.scientific.ceiling, f"ceil({x})"),
                        "18": (self.calculator.scientific.floor, f"floor({x})"),
                    }
                    
                    func, operation_str = single_operations[choice]
                    result = func(x)
                    self.calculator.add_to_history(operation_str, result)

                else:
                    print("\n✗ Invalid option. Please try again.")
                    input("\nPress Enter to continue...")
                    continue

                print(f"\n✓ Result: {result}")
                input("\nPress Enter to continue...")

            except ValueError as ve:
                print(f"\n✗ Error: {ve}")
                input("\nPress Enter to continue...")
            except Exception as error:
                print(f"\n✗ Unexpected error: {error}")
                input("\nPress Enter to continue...")

    @staticmethod
    def _get_two_numbers():
        """Prompt user for two float values."""
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b

    @staticmethod
    def _get_number(prompt: str = "Enter number: ", default=None) -> float:
        """Prompt user for a single float value with optional default."""
        user_input = input(prompt).strip()
        if default is not None and user_input == "":
            return default
        return float(user_input)
"""
main.py

Entry point for the Scientific Calculator application.
"""

from Cli.menu import CalculatorCLI


def main() -> None:
    """Start the calculator application."""
    app = CalculatorCLI()
    app.run()


if __name__ == "__main__":
    main()
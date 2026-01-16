# Scientific Calculator

A command-line scientific calculator built with Python and Object-Oriented Programming principles. Features clean architecture that separates calculation logic from the user interface, making it easily extensible.

## ✨ Features

### Basic Operations
- Addition, Subtraction, Multiplication, Division
- Modulo (Remainder)
- Percentage Calculation

### Scientific Operations
- Power (x^y)
- Square Root (√x)
- Logarithm (any base)
- Natural Logarithm (ln)
- Trigonometric Functions (sin, cos, tan)
- Factorial (n!)
- Absolute Value (|x|)
- Exponential (e^x)
- Ceiling & Floor

### Additional Features
- **Calculation History** - Tracks your last 10 calculations
- **Error Handling** - Comprehensive validation for all inputs
- **Clean Architecture** - Separation of concerns (Calculator logic ↔ CLI)

## 🏗️ Project Structure

```
Scientific-Calculator/
├── main.py                 # Application entry point
├── calculator/
│   ├── __init__.py        # Package initialization
│   ├── basic.py           # Basic arithmetic operations
│   ├── scientific.py      # Scientific operations
│   └── calculator.py      # Core engine with history
├── cli/
│   ├── __init__.py        # CLI package initialization
│   └── menu.py            # Command-line interface
├── tests/                 # Unit tests (optional)
├── README.md              # Documentation
└── .gitignore             # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Scientific-Calculator.git
cd Scientific-Calculator
```

2. Run the calculator:
```bash
python main.py
```

## 💻 Usage

### Basic Example
```
Choose an option: 1
Enter first number: 25
Enter second number: 17
✓ Result: 42.0
```

### Scientific Example
```
Choose an option: 11
Enter angle in degrees: 30
✓ Result: 0.5
```

### View History
```
Choose an option: h

CALCULATION HISTORY:
1. 25 + 17 = 42.0
2. sin(30°) = 0.5
3. √16 = 4.0
```

## 🎯 Design Principles

This project demonstrates:

- **Object-Oriented Programming**: Classes, composition, encapsulation
- **Separation of Concerns**: Calculator logic is independent of CLI
- **SOLID Principles**: Single responsibility, open/closed principle
- **Clean Code**: Readable, maintainable, well-documented
- **Error Handling**: Graceful handling of edge cases

## 🧪 Testing

Run unit tests (if implemented):
```bash
python -m pytest tests/
```

## 🔮 Future Enhancements

- [ ] Expression parser (e.g., "2 + 3 * 4")
- [ ] Memory functions (M+, MR, MC)
- [ ] GUI version (Tkinter/PyQt)
- [ ] History export to file
- [ ] Inverse trigonometric functions
- [ ] Statistical operations (mean, median, std dev)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Your Name  
GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Built with Python's `math` module
- Follows PEP 8 style guidelines
- Inspired by scientific calculator design patterns

---

**Note**: This calculator is designed for educational purposes and demonstrates professional Python development practices including OOP, clean architecture, and maintainable code.
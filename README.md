# copilot-test-calculator
Simple Python calculator created with GitHub Copilot

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Graphical User Interface (GUI) using tkinter
- Error handling for division by zero
- Clear (C) and Clear Entry (CE) buttons
- Decimal number support

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

On Linux, if tkinter is not installed:
```bash
sudo apt-get install python3-tk
```

## Usage

### Running the Calculator GUI

```bash
python3 main.py
```

Or directly:
```bash
python3 calculator_gui.py
```

### Using the Calculator Module

You can also import and use the calculator module in your own Python code:

```python
from calculator import add, subtract, multiply, divide

result = add(5, 3)        # Returns 8
result = subtract(10, 4)  # Returns 6
result = multiply(3, 7)   # Returns 21
result = divide(15, 3)    # Returns 5.0
```

## Testing

Run the unit tests:

```bash
python3 test_calculator.py
```

## Project Structure

- `calculator.py` - Core calculator module with arithmetic operations
- `calculator_gui.py` - GUI interface using tkinter
- `main.py` - Main entry point for the application
- `test_calculator.py` - Unit tests for calculator operations

"""
Simple calculator module with basic arithmetic operations.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(num1, operator, num2):
    """
    Perform calculation based on operator.
    
    Args:
        num1: First number
        operator: Operation to perform (+, -, *, /)
        num2: Second number
        
    Returns:
        Result of the calculation
        
    Raises:
        ValueError: If operator is unknown or division by zero
    """
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        raise ValueError(f"Unknown operator '{operator}'. Use +, -, *, or /")


def main():
    """Command-line interface for the calculator."""
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    print()
    
    while True:
        try:
            user_input = input("Enter calculation (e.g., 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Error: Invalid format. Use: number operator number")
                continue
            
            num1_str, operator, num2_str = parts
            
            # Convert to numbers
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                print("Error: Invalid numbers provided")
                continue
            
            # Perform calculation
            result = calculate(num1, operator, num2)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

"""
Calculator GUI using tkinter.
"""
import tkinter as tk
from tkinter import ttk
import calculator


class CalculatorGUI:
    """Simple calculator GUI application."""
    
    def __init__(self, root):
        """Initialize the calculator GUI."""
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Current calculation
        self.current = ""
        self.total = 0
        self.operator = None
        self.reset_display = False
        
        # Create display
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.display.insert(0, "0")
        
        # Configure grid weights
        root.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        """Create a button with the specified text and position."""
        if text == 'C':
            colspan = 2
        else:
            colspan = 1
            
        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            command=lambda t=text: self.on_button_click(t)
        )
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
    
    def on_button_click(self, char):
        """Handle button click events."""
        if char.isdigit() or char == '.':
            self.handle_number(char)
        elif char in ['+', '-', '*', '/']:
            self.handle_operator(char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear_all()
        elif char == 'CE':
            self.clear_entry()
    
    def handle_number(self, char):
        """Handle number and decimal point input."""
        if self.reset_display:
            self.display.delete(0, tk.END)
            self.reset_display = False
        
        current = self.display.get()
        if current == "0" and char != '.':
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, char)
        elif char == '.' and '.' in current:
            pass  # Ignore multiple decimal points
        else:
            self.display.insert(tk.END, char)
    
    def handle_operator(self, op):
        """Handle operator input."""
        try:
            current = float(self.display.get())
        except ValueError:
            return
        
        if self.operator:
            self.calculate()
            
        self.total = float(self.display.get())
        self.operator = op
        self.reset_display = True
    
    def calculate(self):
        """Perform the calculation."""
        if not self.operator:
            return
        
        try:
            current = float(self.display.get())
            
            if self.operator == '+':
                result = calculator.add(self.total, current)
            elif self.operator == '-':
                result = calculator.subtract(self.total, current)
            elif self.operator == '*':
                result = calculator.multiply(self.total, current)
            elif self.operator == '/':
                result = calculator.divide(self.total, current)
            
            # Display result
            self.display.delete(0, tk.END)
            # Format result to remove unnecessary decimals
            if result == int(result):
                self.display.insert(0, str(int(result)))
            else:
                self.display.insert(0, str(result))
            
            self.operator = None
            self.reset_display = True
            
        except ValueError as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.operator = None
            self.reset_display = True
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.operator = None
            self.reset_display = True
    
    def clear_all(self):
        """Clear all (C button)."""
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")
        self.total = 0
        self.operator = None
        self.reset_display = False
    
    def clear_entry(self):
        """Clear entry (CE button)."""
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")


def main():
    """Main entry point for the calculator GUI."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

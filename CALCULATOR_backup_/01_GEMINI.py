import tkinter as tk
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""

        # Display Screen
        self.display_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.display_frame.pack(expand=True, fill="both", padx=15, pady=(15, 5))

        self.display_label = tk.Label(
            self.display_frame,
            text="0",
            anchor="e",
            font=("Helvetica", 28, "bold"),
            bg="#181825",
            fg="#cdd6f4",
            padx=15,
            pady=15
        )
        self.display_label.pack(expand=True, fill="both")

        # Buttons Grid Layout
        self.buttons_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Button Layout Matrix
        buttons = [
            ('C', 1, 0, '#f38ba8'), ('⌫', 1, 1, '#fab387'), ('%', 1, 2, '#89b4fa'), ('/', 1, 3, '#89b4fa'),
            ('7', 2, 0, '#313244'), ('8', 2, 1, '#313244'), ('9', 2, 2, '#313244'), ('*', 2, 3, '#89b4fa'),
            ('4', 3, 0, '#313244'), ('5', 3, 1, '#313244'), ('6', 3, 2, '#313244'), ('-', 3, 3, '#89b4fa'),
            ('1', 4, 0, '#313244'), ('2', 4, 1, '#313244'), ('3', 4, 2, '#313244'), ('+', 4, 3, '#89b4fa'),
            ('√', 5, 0, '#89b4fa'), ('0', 5, 1, '#313244'), ('.', 5, 2, '#313244'), ('=', 5, 3, '#a6e3a1')
        ]

        # Configure Grid Rows and Columns
        for i in range(6):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.buttons_frame.columnconfigure(j, weight=1)

        # Create Buttons
        for (text, row, col, bg_color) in buttons:
            btn = tk.Button(
                self.buttons_frame,
                text=text,
                font=("Helvetica", 16, "bold"),
                bg=bg_color,
                fg="#11111b" if bg_color in ['#f38ba8', '#fab387', '#a6e3a1', '#89b4fa'] else "#cdd6f4",
                activebackground="#45475a",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                command=lambda symbol=text: self.on_button_click(symbol)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

        # Keyboard Bindings
        self.root.bind("<Key>", self.handle_keypress)

    def update_display(self, value):
        # Truncate overly long text for display aesthetics
        if len(value) > 16:
            value = value[-16:]
        self.display_label.config(text=value if value else "0")

    def on_button_click(self, symbol):
        if symbol == 'C':
            self.expression = ""
        elif symbol == '⌫':
            self.expression = self.expression[:-1]
        elif symbol == '=':
            self.evaluate_expression()
            return
        elif symbol == '√':
            try:
                if self.expression:
                    val = float(eval(self.expression))
                    if val < 0:
                        raise ValueError
                    self.expression = str(math.sqrt(val))
            except Exception:
                self.expression = "Error"
        elif symbol == '%':
            try:
                if self.expression:
                    val = float(eval(self.expression))
                    self.expression = str(val / 100)
            except Exception:
                self.expression = "Error"
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += str(symbol)

        self.update_display(self.expression)

    def evaluate_expression(self):
        try:
            # Evaluate standard math expressions
            result = str(eval(self.expression))
            # Format integers cleanly
            if result.endswith(".0"):
                result = result[:-2]
            self.expression = result
        except ZeroDivisionError:
            self.expression = "Cannot divide by 0"
        except Exception:
            self.expression = "Error"
        
        self.update_display(self.expression)

    def handle_keypress(self, event):
        key = event.char
        if key in "0123456789.+-*/":
            self.on_button_click(key)
        elif event.keysym == "Return":
            self.on_button_click("=")
        elif event.keysym == "BackSpace":
            self.on_button_click("⌫")
        elif event.keysym == "Escape":
            self.on_button_click("C")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
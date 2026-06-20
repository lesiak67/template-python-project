import ast
import operator as _op
import tkinter as tk
from typing import Union

# safe operator mapping
_OPERATORS = {
    ast.Add: _op.add,
    ast.Sub: _op.sub,
    ast.Mult: _op.mul,
    ast.Div: _op.truediv,
    ast.Pow: _op.pow,
    ast.Mod: _op.mod,
    ast.FloorDiv: _op.floordiv,
}


def _eval(node: ast.AST) -> Union[int, float]:
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        func = _OPERATORS.get(type(node.op))
        if func is None:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        return func(left, right)
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.UAdd):
            return +_eval(node.operand)
        if isinstance(node.op, ast.USub):
            return -_eval(node.operand)
        raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
    if isinstance(node, ast.Num):  # type: ignore[attr-defined]
        return node.n  # type: ignore[attr-defined]
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
    raise ValueError("Unsupported expression element")


def calculate(expression: str) -> Union[int, float]:
    """
    Safely evaluate a numeric expression (supports + - * / // % ** and parentheses).
    Raises ValueError on invalid expressions.
    """
    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    try:
        parsed = ast.parse(expression, mode="eval")
        return _eval(parsed)
    except (SyntaxError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"Invalid expression: {exc}") from exc


# --- GUI (Tkinter) ---
def _on_eval(entry: tk.Entry, result_label: tk.Label):
    expr = entry.get()
    try:
        res = calculate(expr)
        result_label.config(text=str(res), fg="black")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")


def _make_button(frame, text, cmd, row, col, colspan=1):
    btn = tk.Button(frame, text=text, width=4, command=cmd)
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)
    return btn


def run_gui():
    root = tk.Tk()
    root.title("Calculator")

    entry = tk.Entry(root, width=30)
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
    entry.focus_set()

    result_label = tk.Label(root, text="", anchor="w", width=30)
    result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=(0, 5))

    btn_frame = tk.Frame(root)
    btn_frame.grid(row=2, column=0, columnspan=4)

    buttons = [
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("/", 0, 3),
        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("*", 1, 3),
        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("-", 2, 3),
        ("0", 3, 0),
        (".", 3, 1),
        ("(", 3, 2),
        (")", 3, 3),
        ("C", 4, 0),
        ("%", 4, 1),
        ("**", 4, 2),
        ("+", 4, 3),
    ]
    for txt, r, c in buttons:

        def _append(t=txt):
            if t == "C":
                entry.delete(0, tk.END)
                result_label.config(text="")
            else:
                entry.insert(tk.END, t)

        _make_button(btn_frame, txt, _append, r, c)

    eval_btn = tk.Button(
        root, text="=", width=34, command=lambda: _on_eval(entry, result_label)
    )
    eval_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    entry.bind("<Return>", lambda e: _on_eval(entry, result_label))

    root.mainloop()


if __name__ == "__main__":
    run_gui()

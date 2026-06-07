import argparse
import sys
from main import calculate

def repl():
    print("Calculator REPL. Type 'quit' or 'exit' to leave.")
    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line.lower() in {"quit", "exit"}:
            break
        try:
            print(calculate(line))
        except Exception as e:
            print("Error:", e)

def main(argv=None):
    parser = argparse.ArgumentParser(prog="calculator", description="Evaluate simple numeric expressions.")
    parser.add_argument("expression", nargs="*", help="Expression to evaluate (quote if needed).")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start interactive REPL.")
    args = parser.parse_args(argv)

    if args.interactive or not args.expression:
        repl()
        return 0

    expr = " ".join(args.expression)
    try:
        result = calculate(expr)
        print(result)
        return 0
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
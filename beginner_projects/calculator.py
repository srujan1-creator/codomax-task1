"""
=============================================================================
Project 1: Command-Line Scientific Calculator
Module: 02_beginner_projects / project1_calculator.py
Description: An interactive CLI calculator featuring arithmetic, powers,
             square roots, percentage calculations, error handling,
             and calculation history tracking.
=============================================================================
"""

import math
import sys
from typing import List, Tuple


class Calculator:
    def __init__(self):
        self.history: List[str] = []

    def add(self, a: float, b: float) -> float:
        res = a + b
        self._record(f"{a} + {b} = {res}")
        return res

    def subtract(self, a: float, b: float) -> float:
        res = a - b
        self._record(f"{a} - {b} = {res}")
        return res

    def multiply(self, a: float, b: float) -> float:
        res = a * b
        self._record(f"{a} * {b} = {res}")
        return res

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Math Error: Division by zero is undefined.")
        res = a / b
        self._record(f"{a} / {b} = {res}")
        return res

    def power(self, base: float, exp: float) -> float:
        res = math.pow(base, exp)
        self._record(f"{base} ^ {exp} = {res}")
        return res

    def square_root(self, val: float) -> float:
        if val < 0:
            raise ValueError("Math Error: Square root of a negative number is not a real number.")
        res = math.sqrt(val)
        self._record(f"sqrt({val}) = {res}")
        return res

    def percentage(self, part: float, total: float) -> float:
        if total == 0:
            raise ZeroDivisionError("Total cannot be zero for percentage computation.")
        res = (part / total) * 100
        self._record(f"({part} / {total}) * 100 = {res:.2f}%")
        return res

    def _record(self, entry: str):
        self.history.append(entry)

    def show_history(self):
        if not self.history:
            print("No calculations performed yet.")
            return
        print("\n--- Calculation History ---")
        for i, item in enumerate(self.history, 1):
            print(f"  [{i}] {item}")


def run_demo():
    print("=" * 60)
    print(" RUNNING CALCULATOR AUTOMATED DEMO ")
    print("=" * 60)
    calc = Calculator()

    print("Addition (145 + 78)       :", calc.add(145, 78))
    print("Subtraction (500 - 235)   :", calc.subtract(500, 235))
    print("Multiplication (12.5 * 8) :", calc.multiply(12.5, 8))
    print("Division (144 / 12)       :", calc.divide(144, 12))
    print("Power (2 ^ 10)            :", calc.power(2, 10))
    print("Square Root (sqrt(225))   :", calc.square_root(225))
    print("Percentage (45 out of 60) :", f"{calc.percentage(45, 60):.2f}%")

    # Error handling demonstration
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Handling zero division    : {e}")

    calc.show_history()
    print("\n[Demo Complete] Calculator functions tested successfully.")


def interactive_menu():
    calc = Calculator()
    while True:
        print("\n" + "=" * 40)
        print("    CODOMAX CLI CALCULATOR")
        print("=" * 40)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (sqrt)")
        print("7. Percentage (%)")
        print("8. View History")
        print("9. Exit")
        choice = input("Enter choice (1-9): ").strip()

        if choice == "9":
            print("Thank you for using Codomax Calculator. Goodbye!")
            break
        elif choice == "8":
            calc.show_history()
            continue

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == "1":
                    print("Result:", calc.add(a, b))
                elif choice == "2":
                    print("Result:", calc.subtract(a, b))
                elif choice == "3":
                    print("Result:", calc.multiply(a, b))
                elif choice == "4":
                    print("Result:", calc.divide(a, b))
                elif choice == "5":
                    print("Result:", calc.power(a, b))
            elif choice == "6":
                val = float(input("Enter number: "))
                print("Result:", calc.square_root(val))
            elif choice == "7":
                part = float(input("Enter part: "))
                total = float(input("Enter total: "))
                print(f"Result: {calc.percentage(part, total):.2f}%")
            else:
                print("Invalid choice, please select 1 to 9.")
        except (ValueError, ZeroDivisionError) as err:
            print("Error:", err)


if __name__ == "__main__":
    if "--demo" in sys.argv or not sys.stdin.isatty():
        run_demo()
    else:
        interactive_menu()

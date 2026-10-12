"""
=============================================================================
Module 1: Introduction to AI & Python
File: 02_operators_and_expressions.py
Description: In-depth demonstration of Python arithmetic, relational,
             logical, bitwise, assignment, and identity/membership operators.
=============================================================================
"""

def arithmetic_operators():
    print("=" * 60)
    print(" 1. ARITHMETIC OPERATORS ")
    print("=" * 60)
    a, b = 17, 5
    print(f"Given a = {a}, b = {b}:")
    print(f"  Addition       (a + b)  = {a + b}")
    print(f"  Subtraction    (a - b)  = {a - b}")
    print(f"  Multiplication (a * b)  = {a * b}")
    print(f"  Division       (a / b)  = {a / b:.4f}")
    print(f"  Floor Division (a // b) = {a // b}  (drops decimal portion)")
    print(f"  Modulus        (a % b)  = {a % b}   (remainder)")
    print(f"  Exponentiation (a ** b) = {a ** b}  ({a} raised to power {b})")


def relational_and_logical_operators():
    print("\n" + "=" * 60)
    print(" 2. RELATIONAL & LOGICAL OPERATORS ")
    print("=" * 60)
    x, y = 25, 30
    print(f"Relational (x = {x}, y = {y}):")
    print(f"  x == y : {x == y}")
    print(f"  x != y : {x != y}")
    print(f"  x < y  : {x < y}")
    print(f"  x >= y : {x >= y}")

    has_license = True
    age = 19
    is_sober = True

    can_drive = (age >= 18) and has_license and is_sober
    print(f"\nLogical Expression: can_drive = (age >= 18) and has_license and is_sober => {can_drive}")

    # Short-circuit evaluation demonstration
    print(f"Short-circuit OR : {True or print('Not evaluated')}")
    print(f"Short-circuit AND: {False and print('Not evaluated')}")


def bitwise_and_membership_operators():
    print("\n" + "=" * 60)
    print(" 3. BITWISE, IDENTITY & MEMBERSHIP OPERATORS ")
    print("=" * 60)

    # Bitwise
    m, n = 12, 10  # 12 = 1100, 10 = 1010
    print(f"m = {m} ({bin(m)}), n = {n} ({bin(n)})")
    print(f"  Bitwise AND (m & n): {m & n} ({bin(m & n)})")
    print(f"  Bitwise OR  (m | n): {m | n} ({bin(m | n)})")
    print(f"  Bitwise XOR (m ^ n): {m ^ n} ({bin(m ^ n)})")
    print(f"  Left Shift  (m << 2): {m << 2} ({bin(m << 2)})")

    # Membership
    fruits = ["apple", "banana", "orange", "mango"]
    print(f"\nMembership in {fruits}:")
    print(f"  'apple' in fruits    : {'apple' in fruits}")
    print(f"  'grape' not in fruits: {'grape' not in fruits}")

    # Identity (is vs ==)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    print("\nIdentity vs Equality:")
    print(f"  list1 == list2 : {list1 == list2} (Same content)")
    print(f"  list1 is list2 : {list1 is list2} (Different memory addresses)")
    print(f"  list1 is list3 : {list1 is list3} (Exact same reference)")


if __name__ == "__main__":
    arithmetic_operators()
    relational_and_logical_operators()
    bitwise_and_membership_operators()
    print("\n[Done] Operators and Expressions executed successfully.")

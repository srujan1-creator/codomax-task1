"""
=============================================================================
Module 1: Introduction to AI & Python
File: 01_variables_and_datatypes.py
Description: Comprehensive demonstration of variables, standard data types,
             type conversion, and string formatting in Python 3.
=============================================================================
"""

def demonstrate_variables_and_types():
    print("=" * 60)
    print(" 1. VARIABLES & FUNDAMENTAL DATA TYPES ")
    print("=" * 60)

    # Integer
    age = 21
    # Float
    gpa = 3.85
    # String
    name = "Codomax Intern"
    # Boolean
    is_enrolled = True
    # Complex number
    complex_val = 3 + 4j
    # NoneType
    mentor = None

    print(f"Integer        : age = {age} -> Type: {type(age).__name__}")
    print(f"Float          : gpa = {gpa} -> Type: {type(gpa).__name__}")
    print(f"String         : name = '{name}' -> Type: {type(name).__name__}")
    print(f"Boolean        : is_enrolled = {is_enrolled} -> Type: {type(is_enrolled).__name__}")
    print(f"Complex        : complex_val = {complex_val} -> Type: {type(complex_val).__name__}")
    print(f"NoneType       : mentor = {mentor} -> Type: {type(mentor).__name__}")


def demonstrate_type_casting():
    print("\n" + "=" * 60)
    print(" 2. TYPE CONVERSION (CASTING) ")
    print("=" * 60)

    # String to Int / Float
    str_num = "42"
    converted_int = int(str_num)
    converted_float = float(str_num)
    print(f"Original string '{str_num}' converted to int: {converted_int} (Type: {type(converted_int).__name__})")
    print(f"Original string '{str_num}' converted to float: {converted_float} (Type: {type(converted_float).__name__})")

    # Float to Int (truncation)
    pi_val = 3.14159
    int_pi = int(pi_val)
    print(f"Float {pi_val} cast to int: {int_pi} (truncated, not rounded)")

    # Truthy and Falsy evaluations
    falsy_values = [0, 0.0, "", [], {}, None, False]
    print("\nFalsy Values in Python:")
    for val in falsy_values:
        print(f"  bool({repr(val):<7}) => {bool(val)}")


def demonstrate_string_operations():
    print("\n" + "=" * 60)
    print(" 3. STRING OPERATIONS & FORMATTING ")
    print("=" * 60)

    course = "Artificial Intelligence & Python"
    
    # Slicing: [start:stop:step]
    print(f"Original String: '{course}'")
    print(f"First 10 chars : '{course[:10]}'")
    print(f"Last 6 chars  : '{course[-6:]}'")
    print(f"Reversed string: '{course[::-1]}'")

    # Methods
    print(f"Uppercase      : '{course.upper()}'")
    print(f"Title Case     : '{course.title()}'")
    print(f"Words Count    : {len(course.split())}")

    # Formatting Styles
    student = "Alex"
    score = 94.756
    print("\nFormatting Examples:")
    # f-string (Modern Python 3.6+)
    print(f"  f-string: Student {student} scored {score:.2f}%")
    # str.format()
    print("  format(): Student {} scored {:.2f}%".format(student, score))


if __name__ == "__main__":
    demonstrate_variables_and_types()
    demonstrate_type_casting()
    demonstrate_string_operations()
    print("\n[Done] Variables and Data Types module executed successfully.")

"""
=============================================================================
Module 1: Introduction to AI & Python
File: 03_control_flow.py
Description: Demonstrating decision-making in Python with if-elif-else,
             nested conditions, match-case (Python 3.10+), and ternary expressions.
=============================================================================
"""

def grade_evaluator(score: float) -> str:
    """Classifies student grade based on percentage score."""
    if score < 0 or score > 100:
        return "Invalid Score (Must be 0-100)"
    elif score >= 90:
        return "Grade A+ (Outstanding)"
    elif score >= 80:
        return "Grade A (Excellent)"
    elif score >= 70:
        return "Grade B (Good)"
    elif score >= 60:
        return "Grade C (Satisfactory)"
    elif score >= 50:
        return "Grade D (Pass)"
    else:
        return "Grade F (Needs Improvement)"


def cinema_ticket_pricing(age: int, is_student: bool, is_weekend: bool) -> float:
    """Calculates ticket price using nested conditional logic."""
    base_price = 15.0

    if age < 5:
        # Toddlers enter free
        return 0.0
    elif age < 18:
        # Minors get base discount
        price = 8.0
        if is_student:
            price -= 2.0
    elif age >= 65:
        # Senior citizen discount
        price = 9.0
    else:
        # Standard adult pricing
        price = base_price
        if is_student:
            price -= 3.0

    # Weekend surcharge
    if is_weekend:
        price += 2.50

    return price


def demonstrate_match_case(command: str):
    """Demonstrates structural pattern matching (Python 3.10+)."""
    match command.strip().lower():
        case "start" | "run":
            return "Status: System initialized and running."
        case "stop" | "halt":
            return "Status: System stopped gracefully."
        case "restart":
            return "Status: System rebooting..."
        case "status":
            return "Status: All services operational (100% health)."
        case _:
            return f"Status: Unknown command '{command}'."


if __name__ == "__main__":
    print("=" * 60)
    print(" 1. IF-ELIF-ELSE GRADE EVALUATION ")
    print("=" * 60)
    test_scores = [95, 82, 73, 64, 52, 41, 105]
    for s in test_scores:
        print(f"Score {s:>3} -> {grade_evaluator(s)}")

    print("\n" + "=" * 60)
    print(" 2. NESTED CONDITIONS & REAL-WORLD PRICING ")
    print("=" * 60)
    scenarios = [
        ("Toddler (age 3)", 3, False, False),
        ("High School Student (age 16)", 16, True, False),
        ("College Student Weekend (age 20)", 20, True, True),
        ("Adult Weekend (age 35)", 35, False, True),
        ("Senior Citizen (age 68)", 68, False, False)
    ]
    for desc, age, is_stud, is_wknd in scenarios:
        price = cinema_ticket_pricing(age, is_stud, is_wknd)
        print(f"{desc:<35} : ${price:.2f}")

    print("\n" + "=" * 60)
    print(" 3. PATTERN MATCHING (MATCH-CASE) ")
    print("=" * 60)
    for cmd in ["start", "stop", "status", "reboot"]:
        print(demonstrate_match_case(cmd))

    # Ternary expression demonstration
    user_status = "Active"
    status_label = "Online" if user_status == "Active" else "Offline"
    print(f"\nTernary Operator: user_status='{user_status}' => '{status_label}'")
    print("\n[Done] Control flow demonstrated successfully.")

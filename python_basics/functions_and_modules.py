"""
=============================================================================
Module 1: Introduction to AI & Python
File: 06_functions_and_modules.py
Description: In-depth exploration of Python functions, arguments (*args, **kwargs),
             lambda functions, recursion, higher-order functions, and variable scopes.
=============================================================================
"""

from typing import List, Tuple, Callable


def calculate_statistics(numbers: List[float]) -> Tuple[float, float, float]:
    """
    Computes mean, min, and max for a list of numeric values.

    Args:
        numbers (List[float]): A non-empty list of numeric items.

    Returns:
        Tuple[float, float, float]: (mean, min_value, max_value)
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics for an empty list.")
    total = sum(numbers)
    mean = total / len(numbers)
    return mean, min(numbers), max(numbers)


def flexible_ai_agent_builder(agent_name: str, *capabilities, **hyperparams) -> dict:
    """
    Demonstrates *args (variable positional) and **kwargs (variable keyword arguments).
    """
    agent_profile = {
        "name": agent_name,
        "capabilities": list(capabilities),
        "parameters": hyperparams
    }
    return agent_profile


def factorial_recursive(n: int) -> int:
    """Recursive calculation of n! with base condition check."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def demonstrate_lambdas_and_functional():
    print("=" * 60)
    print(" 1. LAMBDA & HIGHER-ORDER FUNCTIONS (MAP, FILTER) ")
    print("=" * 60)

    raw_scores = [45, 88, 72, 95, 60, 52, 99]
    print(f"Raw Scores: {raw_scores}")

    # Lambda with filter: only passing scores >= 60
    passing = list(filter(lambda s: s >= 60, raw_scores))
    print(f"Passing scores (>= 60) using filter: {passing}")

    # Lambda with map: curve grades by +5 points (max 100)
    curved = list(map(lambda s: min(100, s + 5), raw_scores))
    print(f"Curved scores (+5 points) using map  : {curved}")

    # Lambda with sorted: sort tuples by second element
    pairs = [("AI", 98), ("DevOps", 85), ("Web", 92), ("Data", 95)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    print(f"Sorted courses by score               : {sorted_pairs}")


def demonstrate_scopes_and_closures():
    print("\n" + "=" * 60)
    print(" 2. VARIABLE SCOPES (LEGB) & CLOSURES ")
    print("=" * 60)

    global_counter = 100  # Global scope

    def make_multiplier(factor: float) -> Callable[[float], float]:
        """Closure that remembers factor in its enclosing scope."""
        def multiplier(value: float) -> float:
            return value * factor
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(f"Closure 'double(15)' -> {double(15)}")
    print(f"Closure 'triple(15)' -> {triple(15)}")


if __name__ == "__main__":
    print("=" * 60)
    print(" 3. FUNCTION PARAMETERS, *ARGS, & **KWARGS ")
    print("=" * 60)

    # Calling statistical function
    sample_data = [12.5, 45.0, 68.2, 91.0, 33.4]
    mean, min_v, max_v = calculate_statistics(sample_data)
    print(f"Data: {sample_data}")
    print(f"Stats -> Mean: {mean:.2f}, Min: {min_v}, Max: {max_v}")

    # Calling *args / **kwargs builder
    agent = flexible_ai_agent_builder(
        "CodomaxBot-v1",
        "Natural Language Processing",
        "Code Generation",
        "Math Reasoning",
        temperature=0.7,
        max_tokens=2048,
        model_version="1.5-pro"
    )
    print("\nGenerated Agent Config:")
    print(f"  Name        : {agent['name']}")
    print(f"  Capabilities: {agent['capabilities']}")
    print(f"  Hyperparams : {agent['parameters']}")

    # Recursive test
    print(f"\nFactorial of 6 (recursive) = {factorial_recursive(6)}")

    demonstrate_lambdas_and_functional()
    demonstrate_scopes_and_closures()
    print("\n[Done] Functions and Modules executed successfully.")

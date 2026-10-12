"""
=============================================================================
Module 1: Introduction to AI & Python
File: 04_loops.py
Description: Demonstrating for loops, while loops, loop controls (break,
             continue, pass), nested loops, and loop-else clauses.
=============================================================================
"""

def demonstrate_for_loops():
    print("=" * 60)
    print(" 1. FOR LOOPS & ITERATION HELPERS ")
    print("=" * 60)

    # Basic range
    print("Numbers 1 to 5:")
    for i in range(1, 6):
        print(f"  Item {i}")

    # Enumerate
    frameworks = ["PyTorch", "TensorFlow", "Scikit-Learn", "Hugging Face"]
    print("\nIterating with enumerate():")
    for idx, fw in enumerate(frameworks, start=1):
        print(f"  {idx}. {fw}")

    # Zip iteration
    metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]
    scores = [0.94, 0.91, 0.96, 0.93]
    print("\nIterating two sequences together with zip():")
    for metric, score in zip(metrics, scores):
        print(f"  {metric:<10} : {score:.2%}")


def demonstrate_while_loops():
    print("\n" + "=" * 60)
    print(" 2. WHILE LOOPS & ACCUMULATION ")
    print("=" * 60)

    # Fibonacci sequence generation using while loop
    n_terms = 8
    a, b = 0, 1
    count = 0
    fib_series = []
    while count < n_terms:
        fib_series.append(a)
        a, b = b, a + b
        count += 1
    print(f"First {n_terms} terms of Fibonacci series: {fib_series}")


def demonstrate_loop_controls():
    print("\n" + "=" * 60)
    print(" 3. LOOP CONTROLS (BREAK, CONTINUE, LOOP-ELSE) ")
    print("=" * 60)

    print("Filtering and breaking in a loop:")
    for num in range(1, 15):
        if num % 3 == 0:
            continue  # Skip multiples of 3
        if num > 11:
            print(f"  Reached limit ({num})! Breaking loop.")
            break
        print(f"  Processing number: {num}")

    # Loop-else: Prime Number Checker
    candidate = 29
    is_prime = True
    print(f"\nPrime check for {candidate} using 'for-else':")
    for factor in range(2, int(candidate ** 0.5) + 1):
        if candidate % factor == 0:
            print(f"  {candidate} is not prime (divisible by {factor})")
            is_prime = False
            break
    else:
        # Executes only if loop completes without hitting 'break'
        print(f"  {candidate} is a PRIME NUMBER! (Verified via loop-else)")


def demonstrate_nested_loops():
    print("\n" + "=" * 60)
    print(" 4. NESTED LOOPS: MULTIPLICATION TABLE GRID ")
    print("=" * 60)
    print("    ", end="")
    for col in range(1, 6):
        print(f"{col:>4}", end="")
    print("\n    " + "-" * 20)

    for row in range(1, 6):
        print(f"{row:>2} |", end="")
        for col in range(1, 6):
            print(f"{row * col:>4}", end="")
        print()


if __name__ == "__main__":
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_controls()
    demonstrate_nested_loops()
    print("\n[Done] Loops and iterations demonstrated successfully.")

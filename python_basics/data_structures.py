"""
=============================================================================
Module 1: Introduction to AI & Python
File: 05_data_structures.py
Description: Exhaustive guide to Python's core data structures: Lists,
             Tuples, Dictionaries, Sets, and Comprehensions.
=============================================================================
"""

def demonstrate_lists():
    print("=" * 60)
    print(" 1. LISTS (MUTABLE, ORDERED SEQUENCES) ")
    print("=" * 60)

    languages = ["Python", "JavaScript", "C++", "Java"]
    print(f"Initial list   : {languages}")

    # Modifications
    languages.append("Rust")
    languages.insert(1, "Go")
    print(f"After insertion: {languages}")

    # Removal
    removed = languages.pop()
    print(f"Popped item    : '{removed}' -> Remaining: {languages}")

    # Slicing and Sorting
    languages.sort()
    print(f"Sorted list    : {languages}")
    print(f"Slice [1:3]    : {languages[1:3]}")


def demonstrate_tuples():
    print("\n" + "=" * 60)
    print(" 2. TUPLES (IMMUTABLE, ORDERED SEQUENCES) ")
    print("=" * 60)

    # Tuple creation & packing
    coordinates = (37.7749, -122.4194)  # San Francisco (lat, long)
    print(f"Coordinates tuple : {coordinates}")

    # Tuple Unpacking
    latitude, longitude = coordinates
    print(f"Unpacked          : Latitude={latitude}, Longitude={longitude}")

    # Tuples as dictionary keys (due to immutability/hashability)
    grid_map = {(0, 0): "Start", (1, 2): "Checkpoint", (3, 3): "Goal"}
    print(f"Grid map key (1, 2): '{grid_map[(1, 2)]}'")


def demonstrate_dictionaries():
    print("\n" + "=" * 60)
    print(" 3. DICTIONARIES (KEY-VALUE HASH MAPS) ")
    print("=" * 60)

    model_config = {
        "model_name": "RandomForestClassifier",
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42,
        "is_trained": False
    }

    print("Model Configuration:")
    for key, value in model_config.items():
        print(f"  {key:<15} : {value}")

    # Updating and Safe Access
    model_config["learning_rate"] = 0.01
    learning_rate = model_config.get("learning_rate", "N/A")
    missing_key = model_config.get("batch_size", 32)  # Returns default 32
    print(f"\nAccess existing key : {learning_rate}")
    print(f"Access with default : {missing_key}")


def demonstrate_sets():
    print("\n" + "=" * 60)
    print(" 4. SETS (UNORDERED, UNIQUE COLLECTIONS) ")
    print("=" * 60)

    dataset_a = {"Python", "NumPy", "Pandas", "Scikit-Learn"}
    dataset_b = {"Pandas", "PyTorch", "TensorFlow", "Python"}

    print(f"Set A: {dataset_a}")
    print(f"Set B: {dataset_b}")

    print(f"  Union (A | B)        : {dataset_a | dataset_b}")
    print(f"  Intersection (A & B) : {dataset_a & dataset_b}")
    print(f"  Difference (A - B)   : {dataset_a - dataset_b}")
    print(f"  Symmetric Diff (A ^ B): {dataset_a ^ dataset_b}")


def demonstrate_comprehensions():
    print("\n" + "=" * 60)
    print(" 5. COMPREHENSIONS (ELEGANT PYTHONIC SYNTAX) ")
    print("=" * 60)

    # List comprehension (squares of even numbers)
    evens_squared = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    print(f"List comprehension (evens squared) : {evens_squared}")

    # Dictionary comprehension (word lengths)
    words = ["Artificial", "Intelligence", "Machine", "Learning", "Python"]
    word_lengths = {word: len(word) for word in words}
    print(f"Dictionary comprehension (lengths) : {word_lengths}")

    # Set comprehension (unique vowel count)
    text = "Codomax Internship Module One"
    vowels_found = {ch.lower() for ch in text if ch.lower() in "aeiou"}
    print(f"Set comprehension (vowels found)   : {vowels_found}")


if __name__ == "__main__":
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    demonstrate_comprehensions()
    print("\n[Done] Data Structures demonstration completed successfully.")

# Codomax Internship — Task 1: Introduction to AI & Python

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests Passing](https://img.shields.io/badge/Tests-10%2F10%20Passed-brightgreen.svg)]()
[![Curriculum](https://img.shields.io/badge/Curriculum-Codomax%20Module%201-orange.svg)]()

> **Submission Deliverables for Module 1 (Day 1 – Day 4 · High Priority)**  
> **Topic:** Introduction to AI & Python  
> **GitHub Repository:** [https://github.com/srujan1-creator/codomax-task1](https://github.com/srujan1-creator/codomax-task1)  
> **Learning Notes:** Available in [`LEARNING_NOTES.md`](./LEARNING_NOTES.md) (formatted for Google Docs / Notion export)

---

## 📌 Table of Contents
1. [Overview & Deliverables](#-overview--deliverables)
2. [Curriculum Coverage](#-curriculum-coverage)
3. [Repository Directory Structure](#-repository-directory-structure)
4. [Getting Started & Installation](#-getting-started--installation)
5. [Running the Python Code](#-running-the-python-code)
   - [Part 1: Core Python Fundamentals](#part-1-core-python-fundamentals)
   - [Part 2: Beginner-Friendly Python Projects](#part-2-beginner-friendly-python-projects)
   - [Part 3: AI & Machine Learning Foundations](#part-3-ai--machine-learning-foundations)
6. [Automated Unit Testing](#-automated-unit-testing)
7. [Learning Notes Summary](#-learning-notes-summary)
8. [Submission Links](#-submission-links)

---

## 🚀 Overview & Deliverables

This repository contains the complete implementation, project source code, unit test suite, and academic learning documentation for **Module 1: Introduction to AI & Python** of the Codomax Internship Program.

### What Was Accomplished:
- ✅ Mastered the core tenets of **Artificial Intelligence (AI)** and **Machine Learning (ML)**.
- ✅ Explored and implemented practical comparisons clarifying **AI vs ML vs Deep Learning (DL)**.
- ✅ Analyzed and implemented real-world AI applications across **Healthcare, Finance, NLP, E-Commerce, and Computer Vision**.
- ✅ Mastered Python programming fundamentals: variables, data types, type casting, operators, control flow, loops, data structures, and functions.
- ✅ Engineered **5 modular, beginner-friendly Python applications** featuring interactive CLI menus and automated demo/testing modes.
- ✅ Implemented an **end-to-end Machine Learning pipeline from scratch in pure Python** (Feature Scaling, Train-Test Split, Logistic Regression via Gradient Descent, Evaluation Metrics).
- ✅ Built an automated **unit test suite (10/10 tests passing)** using Python's `unittest` framework.
- ✅ Documented an exhaustive **Day 1 to Day 4 Learning Journal** in [`LEARNING_NOTES.md`](./LEARNING_NOTES.md).

---

## 📚 Curriculum Coverage

| Day | Modules Covered | Implemented Code Files | Key Concepts |
| :---: | :--- | :--- | :--- |
| **Day 1** | Python Environment & Basics | `python_basics/variables_and_datatypes.py`<br>`python_basics/operators_and_expressions.py` | Variables, primitive types, type casting, strings, arithmetic, logical, bitwise & membership operators |
| **Day 2** | Decision Making & Data Structures | `python_basics/control_flow.py`<br>`python_basics/loops.py`<br>`python_basics/data_structures.py` | `if-elif-else`, pattern matching, `for` & `while` loops, loop-else, lists, tuples, sets, dictionaries, comprehensions |
| **Day 3** | Functions & Beginner Projects | `python_basics/functions_and_modules.py`<br>`beginner_projects/calculator.py`<br>`beginner_projects/number_guessing.py`<br>`beginner_projects/student_tracker.py`<br>`beginner_projects/todo_manager.py` | Positional/keyword arguments, `*args`, `**kwargs`, lambda, scope, recursion, CLI tools, JSON persistence |
| **Day 4** | AI/ML Foundations & Analytics | `beginner_projects/text_analyzer.py`<br>`ai_ml_foundations/ai_vs_ml_vs_dl_demo.py`<br>`ai_ml_foundations/real_world_ai_applications.py`<br>`ai_ml_foundations/simple_ml_model.py` | Rule-based AI vs ML vs DL, NLP spam filter, recommendation engine, health risk estimator, edge detection, pure Python ML pipeline |

---

## 📂 Repository Directory Structure

```
codomax-task1/
├── README.md                          # Main project documentation and overview
├── LEARNING_NOTES.md                  # Comprehensive Day 1 - Day 4 study notes
├── requirements.txt                   # Optional dependencies
├── .gitignore                         # Standard Python gitignore
│
├── python_basics/                     # Part 1: Core Python Programming Fundamentals
│   ├── __init__.py
│   ├── variables_and_datatypes.py     # Primitive types, type casting, string slicing & formatting
│   ├── operators_and_expressions.py   # Arithmetic, relational, logical, bitwise & membership operators
│   ├── control_flow.py                # If-elif-else, nested conditions, pattern matching, ternary ops
│   ├── loops.py                       # For/while loops, enumerate, zip, break/continue, loop-else
│   ├── data_structures.py             # Lists, tuples, dictionaries, sets & comprehensions
│   └── functions_and_modules.py       # *args, **kwargs, recursion, lambda, closures, scopes
│
├── beginner_projects/                 # Part 2: Practical Beginner-Friendly Python Projects
│   ├── __init__.py
│   ├── calculator.py                  # CLI Scientific Calculator with calculation history
│   ├── number_guessing.py             # Number Guessing Game with difficulty levels & hints
│   ├── student_tracker.py             # Academic Performance Tracker with GPA & class analytics
│   ├── todo_manager.py                # To-Do Task Manager with JSON persistence
│   └── text_analyzer.py               # Text & Sentiment Lexicon Analyzer (TTR, word frequencies)
│
├── ai_ml_foundations/                 # Part 3: AI, ML & Deep Learning Foundations
│   ├── __init__.py
│   ├── ai_vs_ml_vs_dl_demo.py         # Practical code demonstrating Rule-Based AI vs ML vs DL
│   ├── real_world_ai_applications.py  # Simulations of NLP Spam Filter, Recommender, Health Risk, CV
│   └── simple_ml_model.py             # End-to-end ML pipeline from scratch (Logistic Regression)
│
└── tests/                             # Part 4: Automated Verification Test Suite
    ├── __init__.py
    └── test_basics.py                 # 10 automated unit tests covering all modules
```

---

## ⚙️ Getting Started & Installation

### Prerequisites
- Python 3.10, 3.11, or 3.12 installed on your machine.
- Git installed.

### Clone the Repository
```bash
git clone https://github.com/srujan1-creator/codomax-task1.git
cd codomax-task1
```

*(Optional) Install testing and formatting libraries:*
```bash
pip install -r requirements.txt
```
> **Note:** All core scripts in this repository are written in pure Python 3 using standard library modules—no external third-party packages are strictly required!

---

## 💻 Running the Python Code

### Part 1: Core Python Fundamentals
Run any of the fundamental concepts scripts directly:
```bash
python python_basics/variables_and_datatypes.py
python python_basics/operators_and_expressions.py
python python_basics/control_flow.py
python python_basics/loops.py
python python_basics/data_structures.py
python python_basics/functions_and_modules.py
```

---

### Part 2: Beginner-Friendly Python Projects
Every project supports both an interactive mode and an automated demo mode (`--demo`):

1. **Scientific CLI Calculator:**
   ```bash
   python beginner_projects/calculator.py --demo      # Automated demonstration
   python beginner_projects/calculator.py             # Interactive menu
   ```

2. **Smart Number Guessing Game:**
   ```bash
   python beginner_projects/number_guessing.py --demo # Binary search bot simulation
   python beginner_projects/number_guessing.py        # Interactive game play
   ```

3. **Student Grade & Performance Tracker:**
   ```bash
   python beginner_projects/student_tracker.py
   ```

4. **Task & To-Do List Manager (JSON Persistence):**
   ```bash
   python beginner_projects/todo_manager.py --demo    # Automated demo
   python beginner_projects/todo_manager.py           # Interactive task manager
   ```

5. **Text & Sentiment Lexicon Analyzer:**
   ```bash
   python beginner_projects/text_analyzer.py --demo
   ```

---

### Part 3: AI & Machine Learning Foundations

1. **AI vs ML vs DL Comparison:**
   ```bash
   python ai_ml_foundations/ai_vs_ml_vs_dl_demo.py
   ```
   *Demonstrates: (1) Rule-based Loan Approval AI, (2) Statistical Linear Regression ML, and (3) Multi-Layer Neural Network forward pass.*

2. **Real-World AI Applications:**
   ```bash
   python ai_ml_foundations/real_world_ai_applications.py
   ```
   *Simulates: NLP Spam Detection, Collaborative Recommender, Cardiovascular Health Risk, and Computer Vision Edge Detection.*

3. **End-to-End Machine Learning Pipeline (From Scratch):**
   ```bash
   python ai_ml_foundations/simple_ml_model.py
   ```
   *Executes: Synthetic dataset creation, Standard feature scaling, Train/Test split, Logistic Regression trained via Gradient Descent, Confusion Matrix, and Evaluation Metrics (Accuracy: ~96.7%, Precision: 100%, Recall: 93.8%, F1: 96.8%).*

---

## 🧪 Automated Unit Testing

To verify all components across the repository, execute the unit test suite:

```bash
python -m unittest tests/test_basics.py
```

**Output:**
```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

---

## 📖 Learning Notes Summary

The accompanying [`LEARNING_NOTES.md`](./LEARNING_NOTES.md) document contains 10 extensive sections formatted for easy reading or direct export into **Google Docs** or **Notion**:
1. **Executive Summary**
2. **Foundations of Artificial Intelligence (AI)** (Definitions, ANI vs AGI vs ASI, History)
3. **Machine Learning (ML) Fundamentals** (Supervised, Unsupervised, Reinforcement, ML Lifecycle)
4. **Deep Learning (DL) & Neural Networks** (Neurons, Activations, Backprop, Optimizers)
5. **The Hierarchy: AI vs ML vs DL** (Architectural Venn diagram & Comparison Matrix)
6. **Real-World Applications of AI** (Healthcare, Autonomous Vehicles, Finance, NLP, E-Commerce)
7. **Python Programming Foundations** (Variables, Operators, Control Flow, Loops, Data Structures, Functions)
8. **Practical Beginner Projects Overview** (Design & architecture of the 5 projects)
9. **Day-by-Day Learning Log** (Detailed daily diary for Days 1 through 4)
10. **Key Takeaways & Reflections**

---

## 📬 Submission Links

- **GitHub Repository Link:** [https://github.com/srujan1-creator/codomax-task1](https://github.com/srujan1-creator/codomax-task1)
- **Learning Notes Document:** Located in the repository at [`LEARNING_NOTES.md`](./LEARNING_NOTES.md)

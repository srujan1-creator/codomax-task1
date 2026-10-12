"""
=============================================================================
Module 1: Introduction to AI & Python
File: 01_ai_vs_ml_vs_dl_demo.py
Description: Practical code demonstrations illustrating the paradigm shifts
             between Rule-Based Artificial Intelligence (AI), Statistical
             Machine Learning (ML), and Multi-Layer Deep Learning (DL).
=============================================================================
"""

import math
import random
from typing import List, Tuple


# =============================================================================
# 1. CLASSICAL / RULE-BASED AI (Symbolic Expert System)
# Paradigm: Humans hand-craft the rules and logic. No learning occurs.
# =============================================================================
class RuleBasedLoanAI:
    @staticmethod
    def evaluate_loan(credit_score: int, annual_income: float, debt_to_income: float) -> Tuple[str, str]:
        """
        Expert rules hardcoded by domain specialists.
        """
        if credit_score < 580:
            return "REJECTED", "Credit score too low (high default risk)."
        if debt_to_income > 0.45:
            return "REJECTED", "Debt-to-income ratio exceeds 45% threshold."
        if annual_income < 30000:
            return "REJECTED", "Annual income below minimum baseline."
        if credit_score >= 750 and debt_to_income < 0.30:
            return "APPROVED_PREMIUM", "Excellent profile qualifying for lowest interest rate."
        return "APPROVED_STANDARD", "Standard profile meeting all safety criteria."


# =============================================================================
# 2. MACHINE LEARNING (Statistical Model)
# Paradigm: The computer learns mathematical weights (W) and bias (b) from data.
# Algorithm: Simple Linear Regression via Gradient Descent (from scratch).
# =============================================================================
class LinearRegressionML:
    def __init__(self):
        self.weight: float = 0.0
        self.bias: float = 0.0

    def fit(self, X: List[float], y: List[float]):
        """Learns relationship y ~ weight * X + bias using Ordinary Least Squares regression."""
        n = len(X)
        mean_x = sum(X) / n
        mean_y = sum(y) / n

        numerator = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(X, y))
        denominator = sum((x_i - mean_x) ** 2 for x_i in X)

        self.weight = numerator / denominator if denominator != 0 else 0.0
        self.bias = mean_y - (self.weight * mean_x)

    def predict(self, x: float) -> float:
        return self.weight * x + self.bias


# =============================================================================
# 3. DEEP LEARNING (Multi-Layer Perceptron / Neural Network)
# Paradigm: Multiple stacked layers with non-linear activations learn
#            hierarchical representations directly from complex inputs.
# =============================================================================
class SimpleNeuralNetworkDL:
    def __init__(self):
        # 2 inputs -> 2 hidden neurons -> 1 output neuron
        # Pre-initialized weights demonstrating forward-pass representation
        self.W1 = [[0.8, -0.5], [0.4, 0.9]]  # Shape: 2x2
        self.b1 = [0.1, -0.2]
        self.W2 = [1.2, -0.7]                # Shape: 2x1
        self.b2 = 0.05

    @staticmethod
    def relu(x: float) -> float:
        """Rectified Linear Unit activation."""
        return max(0.0, x)

    @staticmethod
    def sigmoid(x: float) -> float:
        """Sigmoid activation for probability mapping [0, 1]."""
        return 1.0 / (1.0 + math.exp(-max(-50.0, min(50.0, x))))

    def forward(self, x1: float, x2: float) -> float:
        # Hidden Layer with non-linear ReLU activation
        h1 = self.relu(x1 * self.W1[0][0] + x2 * self.W1[1][0] + self.b1[0])
        h2 = self.relu(x1 * self.W1[0][1] + x2 * self.W1[1][1] + self.b1[1])

        # Output Layer with Sigmoid activation
        z_out = h1 * self.W2[0] + h2 * self.W2[1] + self.b2
        return self.sigmoid(z_out)


def run_comparative_demo():
    print("=" * 70)
    print("      PARADIGM 1: RULE-BASED ARTIFICIAL INTELLIGENCE (AI)")
    print("=" * 70)
    applicants = [
        ("Applicant A", 780, 85000, 0.20),
        ("Applicant B", 620, 45000, 0.40),
        ("Applicant C", 540, 60000, 0.25),
    ]
    for name, score, income, dti in applicants:
        decision, reason = RuleBasedLoanAI.evaluate_loan(score, income, dti)
        print(f"{name:<12} (Credit: {score}, Inc: ${income}, DTI: {dti:.2f})")
        print(f"  Decision  : {decision}")
        print(f"  Rationale : {reason}\n")

    print("=" * 70)
    print("      PARADIGM 2: STATISTICAL MACHINE LEARNING (ML)")
    print("=" * 70)
    # Predicting house price ($k) based on size (sqft in hundreds: 10 = 1000sqft)
    # Ground truth approximately: Price = 25 * Size + 50
    X_train = [10.0, 12.0, 15.0, 18.0, 20.0, 24.0]
    y_train = [300.0, 350.0, 425.0, 500.0, 550.0, 650.0]

    ml_model = LinearRegressionML()
    ml_model.fit(X_train, y_train)

    print(f"Learned Formula: House Price ~ {ml_model.weight:.2f} * (Area/100) + {ml_model.bias:.2f}")
    test_sizes = [14.0, 22.0, 28.0]
    for size in test_sizes:
        sqft = int(size * 100)
        pred = ml_model.predict(size)
        print(f"  House Size: {sqft} sq ft -> Predicted Price: ${pred:.2f}k")

    print("\n" + "=" * 70)
    print("      PARADIGM 3: DEEP LEARNING (DL - NEURAL NETWORK)")
    print("=" * 70)
    dl_model = SimpleNeuralNetworkDL()
    print("Multi-layer neural network forward inference:")
    sample_inputs = [(1.5, 0.5), (0.2, 2.1), (-1.0, 0.8)]
    for idx, (x1, x2) in enumerate(sample_inputs, 1):
        prob = dl_model.forward(x1, x2)
        print(f"  Sample {idx}: Inputs ({x1}, {x2}) -> Output Activation: {prob:.4f} (Prob: {prob*100:.1f}%)")

    print("\n" + "=" * 70)
    print("                      SUMMARY COMPARISON")
    print("=" * 70)
    print("1. Rule-Based AI : Relies on human-programmed logic & heuristics.")
    print("2. Machine Learn : Discovers patterns/parameters automatically from data.")
    print("3. Deep Learning : Uses deep artificial neural networks to learn representations")
    print("                   from raw data without manual feature extraction.")
    print("=" * 70)


if __name__ == "__main__":
    run_comparative_demo()

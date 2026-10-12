"""
=============================================================================
Module 1: Introduction to AI & Python
File: 03_simple_ml_model.py
Description: End-to-end implementation of a Machine Learning workflow from
             scratch in pure Python (Data Preparation, Feature Scaling,
             Train/Test Split, Logistic Regression via Gradient Descent,
             Confusion Matrix, and Evaluation Metrics).
=============================================================================
"""

import math
import random
from typing import List, Tuple, Dict


class SimpleScaler:
    """Standardizes features to zero mean and unit variance."""
    def __init__(self):
        self.means: List[float] = []
        self.stds: List[float] = []

    def fit_transform(self, X: List[List[float]]) -> List[List[float]]:
        n_samples = len(X)
        n_features = len(X[0])
        self.means = [sum(X[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
        self.stds = [
            math.sqrt(sum((X[i][j] - self.means[j]) ** 2 for i in range(n_samples)) / n_samples) or 1.0
            for j in range(n_features)
        ]
        return self.transform(X)

    def transform(self, X: List[List[float]]) -> List[List[float]]:
        return [[(row[j] - self.means[j]) / self.stds[j] for j in range(len(row))] for row in X]


class LogisticRegressionScratch:
    def __init__(self, learning_rate: float = 0.1, epochs: int = 400):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights: List[float] = []
        self.bias: float = 0.0

    @staticmethod
    def _sigmoid(z: float) -> float:
        # Clamp z to avoid overflow
        z = max(-50.0, min(50.0, z))
        return 1.0 / (1.0 + math.exp(-z))

    def fit(self, X: List[List[float]], y: List[int]):
        n_samples = len(X)
        n_features = len(X[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            for i in range(n_samples):
                # Linear combination
                linear = sum(X[i][j] * self.weights[j] for j in range(n_features)) + self.bias
                y_pred = self._sigmoid(linear)

                # Gradient descent step per sample
                error = y_pred - y[i]
                for j in range(n_features):
                    self.weights[j] -= self.lr * error * X[i][j]
                self.bias -= self.lr * error

    def predict_proba(self, X: List[List[float]]) -> List[float]:
        n_features = len(self.weights)
        probas = []
        for row in X:
            linear = sum(row[j] * self.weights[j] for j in range(n_features)) + self.bias
            probas.append(self._sigmoid(linear))
        return probas

    def predict(self, X: List[List[float]], threshold: float = 0.5) -> List[int]:
        return [1 if p >= threshold else 0 for p in self.predict_proba(X)]


def generate_synthetic_data(seed: int = 42) -> Tuple[List[List[float]], List[int]]:
    """
    Generates synthetic student performance data:
    Features: [Study Hours per Week (0-30), Attendance % (40-100)]
    Label   : 1 (Passed Course), 0 (Failed Course)
    """
    random.seed(seed)
    X: List[List[float]] = []
    y: List[int] = []

    for _ in range(120):
        study_hours = random.uniform(2.0, 28.0)
        attendance = random.uniform(45.0, 98.0)
        # Latent pass probability depends strongly on both
        logit = (study_hours * 0.25) + (attendance * 0.08) - 9.0
        prob = 1.0 / (1.0 + math.exp(-logit))
        label = 1 if prob >= 0.5 else 0

        X.append([round(study_hours, 1), round(attendance, 1)])
        y.append(label)

    return X, y


def train_test_split_custom(X: List[List[float]], y: List[int], test_ratio: float = 0.25):
    n_total = len(X)
    n_test = int(n_total * test_ratio)
    indices = list(range(n_total))
    random.seed(42)
    random.shuffle(indices)

    test_idx = indices[:n_test]
    train_idx = indices[n_test:]

    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]

    return X_train, X_test, y_train, y_test


def evaluate_model(y_true: List[int], y_pred: List[int]) -> Dict[str, float]:
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    tn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)

    accuracy = (tp + tn) / len(y_true) if len(y_true) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": tp, "tn": tn, "fp": fp, "fn": fn
    }


def main():
    print("=" * 70)
    print("      MACHINE LEARNING PIPELINE IMPLEMENTATION (FROM SCRATCH)")
    print("=" * 70)

    # 1. Dataset Generation
    X, y = generate_synthetic_data()
    print(f"Generated Dataset : {len(X)} records")
    print(f"Features          : [Weekly Study Hours, Attendance %]")
    print(f"Class Balance     : {y.count(1)} Passed ({y.count(1)/len(y):.1%}), {y.count(0)} Failed")

    # 2. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split_custom(X, y, test_ratio=0.25)
    print(f"Train Set Size    : {len(X_train)} samples")
    print(f"Test Set Size     : {len(X_test)} samples")

    # 3. Feature Scaling
    scaler = SimpleScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Model Training
    model = LogisticRegressionScratch(learning_rate=0.08, epochs=500)
    model.fit(X_train_scaled, y_train)
    print(f"\nTrained Logistic Regression Weights:")
    print(f"  Study Hours Weight : {model.weights[0]:.4f}")
    print(f"  Attendance Weight  : {model.weights[1]:.4f}")
    print(f"  Bias (Intercept)   : {model.bias:.4f}")

    # 5. Model Evaluation
    y_pred = model.predict(X_test_scaled)
    metrics = evaluate_model(y_test, y_pred)

    print("\n" + "=" * 70)
    print("                      EVALUATION RESULTS")
    print("=" * 70)
    print(f"Accuracy        : {metrics['accuracy']:.2%}")
    print(f"Precision       : {metrics['precision']:.2%}")
    print(f"Recall          : {metrics['recall']:.2%}")
    print(f"F1-Score        : {metrics['f1']:.2%}")

    print("\nConfusion Matrix:")
    print(f"  [TN={metrics['tn']:>2}]  [FP={metrics['fp']:>2}]")
    print(f"  [FN={metrics['fn']:>2}]  [TP={metrics['tp']:>2}]")

    # 6. Prediction on Unseen Scenarios
    print("\n" + "=" * 70)
    print("             PREDICTION ON NEW UNSEEN STUDENTS")
    print("=" * 70)
    new_students = [
        ("Student Alpha", [24.0, 92.0]),  # Dedicated: high study, high attendance
        ("Student Beta",  [5.0, 52.0]),   # Low study, low attendance
        ("Student Gamma", [15.0, 75.0]),  # Moderate
    ]
    new_scaled = scaler.transform([s[1] for s in new_students])
    probas = model.predict_proba(new_scaled)

    for (name, raw), p in zip(new_students, probas):
        status = "PASSED" if p >= 0.5 else "FAILED"
        print(f"{name:<15} (Study: {raw[0]}h/wk, Attend: {raw[1]}%)")
        print(f"  Predicted Probability of Passing: {p:.2%} -> Outcome: {status}\n")

    print("[Done] Complete Machine Learning Pipeline executed successfully.")


if __name__ == "__main__":
    main()

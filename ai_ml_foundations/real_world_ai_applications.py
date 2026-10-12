"""
=============================================================================
Module 1: Introduction to AI & Python
File: 02_real_world_ai_applications.py
Description: Practical Python implementations simulating 4 major real-world AI
             applications: NLP Email Spam Filter, Product Recommendation System,
             Healthcare Risk Scoring, and Computer Vision Edge Detection.
=============================================================================
"""

import math
from typing import List, Dict, Tuple


# =============================================================================
# APPLICATION 1: NATURAL LANGUAGE PROCESSING (SPAM EMAIL FILTER)
# Technique: Naive Bayes probability scoring using word likelihoods
# =============================================================================
class SpamFilterNLP:
    def __init__(self):
        # Sample training probabilities for tokens given spam vs ham
        self.spam_words = {"lottery": 0.85, "win": 0.80, "cash": 0.90, "urgent": 0.75, "free": 0.88, "claim": 0.82}
        self.ham_words = {"meeting": 0.05, "project": 0.04, "internship": 0.02, "review": 0.05, "schedule": 0.03}
        self.prior_spam = 0.30  # Baseline 30% spam rate

    def predict_spam_score(self, text: str) -> Tuple[float, str]:
        words = text.lower().split()
        score = self.prior_spam
        reasons = []

        for w in words:
            if w in self.spam_words:
                score += self.spam_words[w] * 0.4
                reasons.append(f"+'{w}' (spam indicator)")
            elif w in self.ham_words:
                score -= 0.3
                reasons.append(f"-'{w}' (legitimate indicator)")

        # Sigmoid squash
        prob = 1.0 / (1.0 + math.exp(-score))
        classification = "SPAM" if prob >= 0.65 else "NOT SPAM (HAM)"
        return prob, classification


# =============================================================================
# APPLICATION 2: RECOMMENDATION SYSTEM (E-COMMERCE / STREAMING)
# Technique: Cosine Similarity between user preference vectors
# =============================================================================
class RecommenderSystem:
    @staticmethod
    def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = math.sqrt(sum(a * a for a in vec_a))
        mag_b = math.sqrt(sum(b * b for b in vec_b))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot_product / (mag_a * mag_b)

    @classmethod
    def recommend(cls, target_user: str, user_profiles: Dict[str, List[float]]) -> List[Tuple[str, float]]:
        if target_user not in user_profiles:
            return []
        target_vec = user_profiles[target_user]
        scores = []
        for other_user, other_vec in user_profiles.items():
            if other_user == target_user:
                continue
            sim = cls.cosine_similarity(target_vec, other_vec)
            scores.append((other_user, sim))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores


# =============================================================================
# APPLICATION 3: HEALTHCARE DIAGNOSTICS & RISK TRIAGE
# Technique: Multi-factorial weighted risk score for cardiovascular health
# =============================================================================
class HealthRiskEstimator:
    @staticmethod
    def calculate_cardio_risk(age: int, systolic_bp: int, cholesterol: int, smoker: bool) -> Dict:
        points = 0
        # Age
        if age >= 60: points += 4
        elif age >= 45: points += 2

        # Blood pressure
        if systolic_bp >= 140: points += 3
        elif systolic_bp >= 120: points += 1

        # Cholesterol
        if cholesterol >= 240: points += 3
        elif cholesterol >= 200: points += 1

        # Smoker
        if smoker: points += 3

        if points >= 8:
            level = "HIGH RISK (Consult Physician Promptly)"
        elif points >= 4:
            level = "MODERATE RISK (Lifestyle Changes Recommended)"
        else:
            level = "LOW RISK (Healthy Baseline)"

        return {"risk_points": points, "risk_category": level}


# =============================================================================
# APPLICATION 4: COMPUTER VISION (EDGE DETECTION FILTER)
# Technique: 2D Convolution with a Sobel horizontal edge kernel
# =============================================================================
def simulate_edge_detection():
    # 4x4 Synthetic greyscale image (showing a horizontal brightness border)
    image_patch = [
        [10, 10, 10, 10],
        [10, 10, 10, 10],
        [90, 90, 90, 90],
        [90, 90, 90, 90]
    ]

    # 3x3 Horizontal Sobel kernel
    kernel = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]

    # Perform 2D convolution for the valid 2x2 output region
    feature_map = [[0, 0], [0, 0]]
    for r in range(2):
        for c in range(2):
            acc = 0
            for kr in range(3):
                for kc in range(3):
                    acc += image_patch[r + kr][c + kc] * kernel[kr][kc]
            feature_map[r][c] = acc

    return feature_map


def main():
    print("=" * 70)
    print("   1. NLP APPLICATION: SPAM DETECTION ")
    print("=" * 70)
    nlp = SpamFilterNLP()
    test_emails = [
        "URGENT: Win free cash lottery prize now! Claim immediately.",
        "Reminder: Codomax internship project review meeting tomorrow."
    ]
    for em in test_emails:
        prob, label = nlp.predict_spam_score(em)
        print(f"Email Content : \"{em}\"")
        print(f"Probability   : {prob:.2%} -> Classified as: {label}\n")

    print("=" * 70)
    print("   2. E-COMMERCE / STREAMING: COLLABORATIVE RECOMMENDATIONS ")
    print("=" * 70)
    # Features: [Action, Sci-Fi, Comedy, Romance, Documentary] (Ratings 1-5)
    movie_ratings = {
        "User_Srujan": [5, 5, 2, 1, 4],
        "User_Alice":  [5, 4, 1, 2, 5],
        "User_Bob":    [1, 1, 5, 5, 1],
        "User_Charlie":[4, 5, 3, 2, 3]
    }
    recs = RecommenderSystem.recommend("User_Srujan", movie_ratings)
    print("Recommendations for User_Srujan based on taste similarity:")
    for user, sim in recs:
        print(f"  Similarity with {user:<12} : {sim:.4f} ({sim*100:.1f}% match)")

    print("\n" + "=" * 70)
    print("   3. HEALTHCARE: CARDIOVASCULAR RISK ESTIMATOR ")
    print("=" * 70)
    patient = HealthRiskEstimator.calculate_cardio_risk(age=55, systolic_bp=145, cholesterol=220, smoker=True)
    print("Patient: 55yo, BP: 145, Cholesterol: 220, Smoker: Yes")
    print(f"Assessment: {patient['risk_category']} (Score: {patient['risk_points']} points)")

    print("\n" + "=" * 70)
    print("   4. COMPUTER VISION: 2D CONVOLUTION (EDGE DETECTION) ")
    print("=" * 70)
    edge_map = simulate_edge_detection()
    print("Output feature map highlighting horizontal border (Sharp response):")
    for row in edge_map:
        print(f"  {row}")

    print("\n[Done] All real-world AI application demonstrations executed successfully.")


if __name__ == "__main__":
    main()

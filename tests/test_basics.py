"""
=============================================================================
Module 1: Test Suite
File: tests/test_basics.py
Description: Automated unit tests verifying python basics, beginner projects,
             and AI/ML logic across Module 1.
=============================================================================
"""

import unittest
import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from python_basics.control_flow import grade_evaluator, cinema_ticket_pricing
from python_basics.functions_and_modules import calculate_statistics, factorial_recursive
from beginner_projects.calculator import Calculator
from beginner_projects.number_guessing import NumberGuessingGame
from beginner_projects.student_tracker import Student, ClassroomTracker
from beginner_projects.todo_manager import TaskManager
from beginner_projects.text_analyzer import TextAnalyzer
from ai_ml_foundations.ai_vs_ml_vs_dl_demo import RuleBasedLoanAI, LinearRegressionML, SimpleNeuralNetworkDL
from ai_ml_foundations.real_world_ai_applications import RecommenderSystem, SpamFilterNLP
from ai_ml_foundations.simple_ml_model import LogisticRegressionScratch, evaluate_model


class TestModule1(unittest.TestCase):

    def test_grade_evaluator(self):
        self.assertIn("A+", grade_evaluator(95))
        self.assertIn("B", grade_evaluator(75))
        self.assertIn("F", grade_evaluator(35))
        self.assertIn("Invalid", grade_evaluator(105))

    def test_ticket_pricing(self):
        self.assertEqual(cinema_ticket_pricing(3, False, False), 0.0)
        self.assertEqual(cinema_ticket_pricing(16, True, False), 6.0)

    def test_math_and_stats(self):
        mean, min_v, max_v = calculate_statistics([10, 20, 30])
        self.assertEqual(mean, 20)
        self.assertEqual(min_v, 10)
        self.assertEqual(max_v, 30)
        self.assertEqual(factorial_recursive(5), 120)

    def test_calculator(self):
        calc = Calculator()
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.square_root(16), 4)

    def test_number_guessing(self):
        game = NumberGuessingGame("2")
        self.assertEqual(game.max_attempts, 7)
        self.assertEqual(game.max_range, 100)
        game.secret_number = 42
        feedback = game.evaluate_guess(42)
        self.assertEqual(feedback, "CORRECT")
        self.assertTrue(game.has_won)

    def test_student_tracker(self):
        student = Student("S1", "Test Student")
        student.add_score("Python", 90)
        student.add_score("Math", 80)
        self.assertEqual(student.calculate_average(), 85.0)
        self.assertEqual(student.get_letter_grade(), "A")
        self.assertTrue(student.is_passed())

    def test_todo_manager(self):
        test_file = "test_temp_tasks.json"
        if os.path.exists(test_file):
            os.remove(test_file)
        mgr = TaskManager(test_file)
        t = mgr.add_task("Test Task", priority="High")
        self.assertEqual(len(mgr.tasks), 1)
        self.assertTrue(mgr.mark_complete(t["id"]))
        self.assertTrue(mgr.tasks[0]["completed"])
        mgr.delete_task(t["id"])
        self.assertEqual(len(mgr.tasks), 0)
        if os.path.exists(test_file):
            os.remove(test_file)

    def test_text_analyzer(self):
        text = "Artificial Intelligence is innovative and fantastic."
        analyzer = TextAnalyzer(text)
        self.assertEqual(analyzer.word_count(), 6)
        senti = analyzer.analyze_sentiment()
        self.assertEqual(senti["sentiment"], "Positive")

    def test_ai_foundations(self):
        dec, _ = RuleBasedLoanAI.evaluate_loan(780, 90000, 0.20)
        self.assertEqual(dec, "APPROVED_PREMIUM")

        reg = LinearRegressionML()
        reg.fit([1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 6.0, 8.0])
        self.assertAlmostEqual(reg.predict(5.0), 10.0, places=2)

        dl = SimpleNeuralNetworkDL()
        out = dl.forward(1.0, 1.0)
        self.assertTrue(0.0 <= out <= 1.0)

    def test_recommender_and_spam(self):
        sim = RecommenderSystem.cosine_similarity([1, 0, 0], [1, 0, 0])
        self.assertAlmostEqual(sim, 1.0, places=3)
        sim_ortho = RecommenderSystem.cosine_similarity([1, 0], [0, 1])
        self.assertAlmostEqual(sim_ortho, 0.0, places=3)

        spam = SpamFilterNLP()
        prob, label = spam.predict_spam_score("win free lottery cash now")
        self.assertEqual(label, "SPAM")


if __name__ == "__main__":
    unittest.main()

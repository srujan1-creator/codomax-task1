"""
=============================================================================
Project 3: Student Grade & Performance Tracker
Module: 02_beginner_projects / project3_student_tracker.py
Description: A comprehensive academic tracking system managing student
             marks across multiple subjects, calculating GPA, assigning
             letter grades, generating class analytics and summary reports.
=============================================================================
"""

import sys
from typing import Dict, List, Optional


class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.scores: Dict[str, float] = {}

    def add_score(self, subject: str, score: float):
        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} must be between 0 and 100.")
        self.scores[subject] = score

    def calculate_average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def get_letter_grade(self) -> str:
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def is_passed(self, passing_threshold: float = 50.0) -> bool:
        if not self.scores:
            return False
        # Student passes if average >= threshold and no individual subject < 40
        return self.calculate_average() >= passing_threshold and all(s >= 40.0 for s in self.scores.values())


class ClassroomTracker:
    def __init__(self, course_name: str):
        self.course_name = course_name
        self.students: Dict[str, Student] = {}

    def register_student(self, student: Student):
        self.students[student.student_id] = student

    def class_average(self) -> float:
        if not self.students:
            return 0.0
        totals = [s.calculate_average() for s in self.students.values()]
        return sum(totals) / len(totals)

    def top_performer(self) -> Optional[Student]:
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.calculate_average())

    def print_performance_report(self):
        print("\n" + "=" * 70)
        print(f"       CODOMAX ACADEMIC PERFORMANCE REPORT - {self.course_name.upper()}")
        print("=" * 70)
        print(f"{'ID':<8} {'Student Name':<20} {'Average':<10} {'Grade':<8} {'Status':<10}")
        print("-" * 70)

        for s in self.students.values():
            avg = s.calculate_average()
            grade = s.get_letter_grade()
            status = "PASS" if s.is_passed() else "FAIL"
            print(f"{s.student_id:<8} {s.name:<20} {avg:<10.2f} {grade:<8} {status:<10}")

        print("-" * 70)
        print(f"Total Enrolled  : {len(self.students)}")
        print(f"Class Average   : {self.class_average():.2f}%")
        top = self.top_performer()
        if top:
            print(f"Top Performer   : {top.name} (Avg: {top.calculate_average():.2f}%, Grade: {top.get_letter_grade()})")
        print("=" * 70)


def run_demo():
    print("=" * 60)
    print(" RUNNING STUDENT GRADE TRACKER DEMO ")
    print("=" * 60)

    tracker = ClassroomTracker("AI & Machine Learning 101")

    # Seed data
    s1 = Student("STU001", "Aarav Sharma")
    s1.add_score("Python", 92)
    s1.add_score("Math", 88)
    s1.add_score("AI Concepts", 95)

    s2 = Student("STU002", "Priya Patel")
    s2.add_score("Python", 78)
    s2.add_score("Math", 82)
    s2.add_score("AI Concepts", 80)

    s3 = Student("STU003", "Rohan Verma")
    s3.add_score("Python", 64)
    s3.add_score("Math", 58)
    s3.add_score("AI Concepts", 62)

    s4 = Student("STU004", "Ananya Reddy")
    s4.add_score("Python", 98)
    s4.add_score("Math", 96)
    s4.add_score("AI Concepts", 99)

    s5 = Student("STU005", "Vikram Singh")
    s5.add_score("Python", 45)
    s5.add_score("Math", 38)  # Fail in single subject
    s5.add_score("AI Concepts", 52)

    for st in [s1, s2, s3, s4, s5]:
        tracker.register_student(st)

    tracker.print_performance_report()


if __name__ == "__main__":
    run_demo()

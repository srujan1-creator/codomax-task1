"""
=============================================================================
Project 4: Task & To-Do List Manager
Module: 02_beginner_projects / project4_todo_manager.py
Description: A robust task management application featuring task creation,
             completion tracking, priority tagging, filtering, and JSON
             file persistence.
=============================================================================
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional


class TaskManager:
    def __init__(self, storage_file: str = "tasks_sample.json"):
        self.storage_file = storage_file
        self.tasks: List[Dict] = []
        self.load_tasks()

    def add_task(self, title: str, priority: str = "Medium", category: str = "General") -> Dict:
        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "priority": priority.capitalize(),
            "category": category.capitalize(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def mark_complete(self, task_id: int) -> bool:
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        original_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < original_len:
            # Re-index remaining tasks
            for idx, t in enumerate(self.tasks, 1):
                t["id"] = idx
            self.save_tasks()
            return True
        return False

    def list_tasks(self, filter_status: Optional[bool] = None) -> List[Dict]:
        if filter_status is None:
            return self.tasks
        return [t for t in self.tasks if t["completed"] == filter_status]

    def save_tasks(self):
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except (IOError, json.JSONDecodeError):
                self.tasks = []
        else:
            self.tasks = []

    def display(self, filtered_tasks: Optional[List[Dict]] = None):
        items = filtered_tasks if filtered_tasks is not None else self.tasks
        if not items:
            print("\nNo tasks to display.")
            return

        print("\n" + "=" * 75)
        print(f"{'ID':<4} {'Status':<10} {'Priority':<10} {'Category':<12} {'Title'}")
        print("-" * 75)
        for t in items:
            status = "[DONE]" if t["completed"] else "[TODO]"
            print(f"{t['id']:<4} {status:<10} {t['priority']:<10} {t['category']:<12} {t['title']}")
        print("=" * 75)


def run_demo():
    print("=" * 60)
    print(" RUNNING TASK & TO-DO MANAGER DEMO ")
    print("=" * 60)

    # Use a temporary sample file for the demo
    demo_file = "demo_tasks.json"
    if os.path.exists(demo_file):
        os.remove(demo_file)

    manager = TaskManager(storage_file=demo_file)

    # Add tasks
    print("Adding sample internship tasks...")
    manager.add_task("Complete Module 1 Python Basics exercises", priority="High", category="Codomax")
    manager.add_task("Review differences between AI, ML, and Deep Learning", priority="High", category="Study")
    manager.add_task("Write comprehensive learning notes in Notion", priority="Medium", category="Codomax")
    manager.add_task("Setup GitHub repository and push source files", priority="High", category="Dev")
    manager.add_task("Read research paper on Neural Networks", priority="Low", category="Reading")

    manager.display()

    # Mark some as completed
    print("\nMarking task #1 and #4 as completed...")
    manager.mark_complete(1)
    manager.mark_complete(4)
    manager.display()

    print("\nFiltering: Showing Pending Tasks only:")
    pending = manager.list_tasks(filter_status=False)
    manager.display(pending)

    # Clean up demo file
    if os.path.exists(demo_file):
        os.remove(demo_file)
    print("\n[Done] Task Manager demo completed successfully.")


if __name__ == "__main__":
    if "--demo" in sys.argv or not sys.stdin.isatty():
        run_demo()
    else:
        mgr = TaskManager()
        while True:
            print("\n=== TO-DO LIST MENU ===")
            print("1. View All Tasks")
            print("2. Add Task")
            print("3. Mark Task as Done")
            print("4. Delete Task")
            print("5. View Pending Tasks")
            print("6. Exit")
            opt = input("Select option (1-6): ").strip()

            if opt == "1":
                mgr.display()
            elif opt == "2":
                t_title = input("Task title: ").strip()
                t_prio = input("Priority (Low/Medium/High) [Medium]: ").strip() or "Medium"
                t_cat = input("Category [General]: ").strip() or "General"
                mgr.add_task(t_title, t_prio, t_cat)
                print("Task added successfully!")
            elif opt == "3":
                mgr.display()
                t_id = int(input("Enter task ID to mark done: "))
                if mgr.mark_complete(t_id):
                    print("Task updated!")
                else:
                    print("Task ID not found.")
            elif opt == "4":
                mgr.display()
                t_id = int(input("Enter task ID to delete: "))
                if mgr.delete_task(t_id):
                    print("Task deleted!")
                else:
                    print("Task ID not found.")
            elif opt == "5":
                mgr.display(mgr.list_tasks(filter_status=False))
            elif opt == "6":
                print("Exiting To-Do Manager.")
                break

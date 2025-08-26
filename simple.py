
import json
from pathlib import Path

DATA_FILE = Path("todo.json")

def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except json.JSONDecodeError:
            pass
    return []

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))

def show(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t['title']}")
    print()

def main():
    tasks = load_tasks()
    print("=== Simple To-Do List ===")
    while True:
        print("Commands: add  remove  done  view  clear  save  quit")
        cmd = input("> ").strip().lower()

        if cmd == "add":
            title = input("Task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                print("Added.")
            else:
                print("Title cannot be empty.")

        elif cmd == "remove":
            show(tasks)
            try:
                idx = int(input("Task number to remove: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Removed: {removed['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

        elif cmd == "done":
            show(tasks)
            try:
                idx = int(input("Task number completed: "))
                if 1 <= idx <= len(tasks):
                    tasks[idx - 1]["done"] = True
                    print("Marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

        elif cmd == "view":
            show(tasks)

        elif cmd == "clear":
            confirm = input("Delete ALL tasks? (y/n): ").strip().lower()
            if confirm == "y":
                tasks.clear()
                print("All tasks cleared.")

        elif cmd == "save":
            save_tasks(tasks)
            print(f"Saved to {DATA_FILE.resolve()}")

        elif cmd in ("quit", "exit", "q"):
            save_tasks(tasks)
            print("Saved and exiting. Bye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

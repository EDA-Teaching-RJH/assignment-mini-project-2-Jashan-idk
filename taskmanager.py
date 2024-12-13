import re
import csv
from task_object import Task

tasks = []

def main():
    tasks = load_tasks_from_file()
    
    print("welcome to the task manager")

    for day in ["Today", "Tomorrow"]:
        print(f" what are your tasks for {day} and when done entering tasks type done")
        while True:
            task_description = input(f"Task for {day}:")
            if task_description.lower() == "done":
                break
            elif task_description == "":
                raise ValueError
            add_task(tasks, Task(task_description, day))
    
    print("\nthese are your tasks")
    for i, task in enumerate(tasks):
        print(f"[{i}] {task}")

    save_tasks_to_file(tasks)
    

def add_task(tasks, task):
    tasks.append(task)

def save_tasks_to_file(tasks, filename="tasks.csv"):
    with open (filename, "w" , newline="") as file:
        writer = csv.writer(file) 
        writer.writerow(["description", "day"])
        for task in tasks:
            writer.writerow([task.description, task.day])
    
def load_tasks_from_file(filename="tasks.csv"):
    tasks = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                description, day = row
                task = Task(description, day)
                tasks.append(task)
    except FileNotFoundError:
        print("No previous tasks found.")
    return tasks
if __name__ == "__main__":
        main()
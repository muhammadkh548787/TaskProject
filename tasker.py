from prowild import Add
import pathlib
import os
from pathlib import Path


print("1. User registration and login")
print("2. Add task")
print("3. Show all tasks")
print("4. Todays tasks")
print("5. Delete task")



cwd=pathlib.Path.cwd()
file_manager=Add(cwd)

run = True
while run:
    x = input("Choose your choice: ")

    if x == "1":
        file_manager.reg()
    elif x == "2":
        file_manager.add_task()
    elif x == "3":
        file_manager.show_tasks()
    elif x == "4":
        file_manager.todays_task()
    elif x == "5":
        file_manager.delete_task()
    elif x == "exit":
        run = False
    




    
        




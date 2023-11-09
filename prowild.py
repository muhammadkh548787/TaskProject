import ast
import pickle
from datetime import date
import pathlib
import os
from pathlib import Path
import shutil
import hashlib
import datetime
from datetime import datetime
date_string = datetime.today()
day = "%d"
month = "%m"
year = "20%y"
day_now = int(datetime.strftime(date_string,day))
month_now = int(datetime.strftime(date_string,month))
year_now = int(datetime.strftime(date_string, year))


class Add:
    def __init__(self, cwd):
        self.cwd = cwd
    def reg(self):
        user = input("User: ")
        password = input("Password: ")
        file_name = 'userp.txt'
        with open(file_name, 'a') as f:
            f.write((user)+ '\n')
        hash_object = hashlib.sha256()
        hashed_password = hash_object.update(password.encode())
        hashed_password_hex = hash_object.hexdigest()
        with open(file_name, 'a') as f:
            f.write((hashed_password_hex)+ '\n')
    def add_task(self):
        task_number = input("Number of your task: ")
        task_name = input("Name of your task: ")
        task_description = input("Describe your task: ")
        task_priority = input("Priority of your task: ")
        task_dedline = input("Dedline of your task: ")
        task_status = input("Status of your task: ")
        task = f"number: {task_number} | name: {task_name} | description: {task_description} | priority: {task_priority} | dedline: {task_dedline} | status: {task_status}"
        
        with open("tasks.txt", 'a') as f:
            f.write(task + "\n")

    def show_tasks(self):
        qw = Path('tasks.txt')
        file_content = qw.read_text()
        print(file_content)
    def delete_task(self):
        ad = Add.show_tasks()
        index = int(input("Which task you want to delete: ")) - 1
        if 0 <= index < len(ad):
            task = ad[index]
            ad.remove_task(task)
            print("The task has been deleted")
    def todays_task(self):
        with open("tasks.txt","r") as file:
            for line in file.read().splitlines():
                line_split = line.split("|")
                line_split_1 = str(line_split[4])
                line_split_1_1 = line_split_1.split(":")
                line_split_1_1_1 = line_split_1_1[1]
                line_splited_to_str_nums = line_split_1_1_1.split("-")
                line_splited_to_str_nums_day = int(line_splited_to_str_nums[0])
                line_splited_to_str_nums_month = int(line_splited_to_str_nums[1])
                line_splited_to_str_nums_year = int(line_splited_to_str_nums[2])
                if line_splited_to_str_nums_day == day_now and line_splited_to_str_nums_month == month_now and line_splited_to_str_nums_year == year_now:
                    print(line)





 

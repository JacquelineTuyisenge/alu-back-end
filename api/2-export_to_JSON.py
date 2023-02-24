#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        extract username
    """
    username = user.get("username")

    """
        request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status(completed) in boolean format
    """
    tasks = {}
    """
        convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    task_list = []
    for k, v in tasks.items():
        task_list.append({
            "task": k,
            "completed": v,
            "username": username
        })

    json_to_dump = {argv[1]: task_list}
    """
        export to JSON
    """
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)

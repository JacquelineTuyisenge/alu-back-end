#!/usr/bin/python3
""""Python script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    employee_username = user_info["username"]

    todos_info_sorted = [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], employee_username]))
        for task in todos_info]

    user_dict = {str(employee_id): todos_info_sorted}
    with open(str(employee_id) + '.json', "w") as file:
        file.write(json.dumps(user_dict))

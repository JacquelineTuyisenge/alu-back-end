#!/usr/bin/python3
""" get data from csv """

import csv
import json
import requests
import sys
if __name__ == "__main__":
    def getTodos(id):
        link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        res = requests.get(link)
        return json.loads(res.text)
    link = "https://jsonplaceholder.typicode.com/users/"
    res = requests.get(link)
    users = json.loads(res.text)
    data = {}
    for i in users:
        todos = getTodos(i["id"])
        data[i["id"]] = [{"task": j["title"], "completed": j["completed"],
                          "username": i["username"]} for j in todos]
    with open("todo_all_employees.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))

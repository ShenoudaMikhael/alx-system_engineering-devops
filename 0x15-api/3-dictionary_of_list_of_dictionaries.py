#!/usr/bin/python3
"""Gather Data Module"""
import json
import urllib.request
import urllib.response


if __name__ == "__main__":

    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos/"
    ) as response:

        data = json.loads(response.read())

        with urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users/"
        ) as resp:

            users = json.loads(resp.read())
        gn = {}
        for user in users:
            q = [i for i in data if i["userId"] == int(user["id"])]
            js = {
                "{}".format(user["id"]): [
                    {
                        "username": user["username"],
                        "task": i["title"],
                        "completed": i["completed"],
                    }
                    for i in q
                ]
            }
            gn.update(js)
        with open("todo_all_employees.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(gn))

#!/usr/bin/python3
"""Gather Data Module"""
import json
from sys import argv
import urllib.request
import urllib.response


if __name__ == "__main__":
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
                                ) as resp:
        user = json.loads(resp.read())

    with urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos/"
                                ) as response:
        data = json.loads(response.read())
        q = [i for i in data if i["userId"] == int(argv[1])]
        js = {"{}".format(argv[1]): [
            {
                "task": i["title"],
                "completed": i["completed"],
                "username": user["username"]
                } for i in q]}
        with open("{}.json".format(argv[1]), "w") as f:
            f.write(json.dumps(js))

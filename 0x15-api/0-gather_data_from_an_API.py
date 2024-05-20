#!/usr/bin/python3
"""Gather Data Module"""
from sys import argv
import urllib.request
import urllib.response
import json

with urllib.request.urlopen(
    "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
                            ) as resp:
    user = json.loads(resp.read())

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos/"
                            ) as response:
    data = json.loads(response.read())
    q = [i for i in data if i["userId"] == int(argv[1])]
    completed = [i for i in q if i["completed"] is True]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"],
            len(completed), len(q)
        )
    )
    for i in completed:
        print("\t {}".format(i["title"]))

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
        # completed = [i for i in q if i["completed"] is True]
        
        with open("{}.csv".format(argv[1]), "w") as f:
            for i in q:
                f.write(
                    '"{}","{}","{}","{}"\n'.format(
                        argv[1],
                        user["name"],
                        i["completed"],
                        i["title"],
                        )
                        )

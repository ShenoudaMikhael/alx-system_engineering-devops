#!/usr/bin/python3
"""Top Ten Module"""


def top_ten(subreddit):
    """Top Ten"""
    import requests

    with requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "ALX"},
        allow_redirects=False,
        timeout=30,
    ) as r:
        if r.status_code >= 300:
            print("None")
        else:
            for child in r.json().get("data").get("children"):
                print(child.get("data").get("title"))

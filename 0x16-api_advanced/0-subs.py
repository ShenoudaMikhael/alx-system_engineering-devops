#!/usr/bin/python3
"""# subs module"""
import requests


def number_of_subscribers(subreddit):
    """numbeer of subs"""
    headers = {"User-Agent": "user_agent"}
    with requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        timeout=30,
        headers=headers,
    ) as r:
        if r.status_code == 200:

            return r.json()["data"]["subscribers"]
        else:
            return 0

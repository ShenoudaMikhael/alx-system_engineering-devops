#!/usr/bin/python3
"""# subs module"""
import requests


def number_of_subscribers(subreddit):
    """numbeer of subs"""
    try:
        headers = {"User-Agent": "/u/ALX"}
        with requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            timeout=30,
            headers=headers,
            allow_redirects=False,
        ) as r:
            if r.status_code == 200:

                return r.json().get("data").get("subscribers")
            else:
                return 0
    except requests.RequestException:
        return 0

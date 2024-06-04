#!/usr/bin/python3
"""Recurse it Module"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Recurse"""
    import requests

    with requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        params={"count": count, "after": after},
        headers={"User-Agent": "ALX"},
        allow_redirects=False,
        timeout=30,
    ) as r:
        if r.status_code >= 400:
            return None

        hot_l = hot_list + [
            child.get("data").get("title")
            for child in r.json().get("data").get("children")
        ]

        info = r.json()
        if not info.get("data").get("after"):
            return hot_l

        return recurse(
            subreddit,
            hot_l,
            info.get("data").get("count"),
            info.get("data").get("after"),
        )

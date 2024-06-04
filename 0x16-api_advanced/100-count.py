#!/usr/bin/python3
"""Count Module"""

import requests


def count_words(subreddit, word_list, after="", count=[]):
    """count all words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    with requests.get(
        url,
        params={"after": after},
        allow_redirects=False,
        headers={"user-agent": "bhalut"},
        timeout=30,
    ) as r:

        if r.status_code == 200:
            data = r.json()

            for t in data["data"]["children"]:
                for w in t["data"]["title"].split():
                    for i in range(len(word_list)):
                        if word_list[i].lower() == w.lower():
                            count[i] += 1

            after = data["data"]["after"]
            if after is None:
                save = []
                for i in range(len(word_list)):
                    for j in range(i + 1, len(word_list)):
                        if word_list[i].lower() == word_list[j].lower():
                            save.append(j)
                            count[i] += count[j]

                for i in range(len(word_list)):
                    for j in range(i, len(word_list)):
                        if count[j] > count[i] or (
                            word_list[i] > word_list[j]
                            and count[j] == count[i]
                        ):
                            nc = count[i]
                            count[i] = count[j]
                            count[j] = nc
                            nc = word_list[i]
                            word_list[i] = word_list[j]
                            word_list[j] = nc

                for i in range(len(word_list)):
                    if (count[i] > 0) and i not in save:
                        print("{}: {}".format(word_list[i].lower(), count[i]))
            else:
                count_words(subreddit, word_list, after, count)

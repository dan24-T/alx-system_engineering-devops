#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, w_list=[], after="", i=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    p = {
        "after": after,
        "count": i,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=p,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    i += res.get("dist")
    for c in res.get("children"):
        w_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, w_list, after, i)
    return w_list

#!/usr/bin/python3
"""
number_of_subscribers task - api Adavanced
"""

import requests


def number_of_subscribers(subreddit):
    """Query that returns number of subscribers of a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    req = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'My-User-Agent'},allow_redirects=False).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs

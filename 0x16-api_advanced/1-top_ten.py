#!/usr/bin/python3
""" We can print top ten hot posts with the function blow"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    B_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"}
    p = {
        "limit": 10
    }
    response = requests.get(B_url, headers=headers, params=p,
                            allow_redirects=False)
    if response.status_code >= 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]

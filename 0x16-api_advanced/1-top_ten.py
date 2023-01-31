#!/usr/bin/python3
"""
queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import pprint
import requests


def top_ten(subreddit):
    headers = {'User-agent': 'dani random'}
    URL = 'https://www.reddit.com/r/{}/hot.json'
    get_sub = requests.get(URL.format(subreddit),
                           params={"limit": 10, "g": "GLOBAL"},
                           headers={"User-Agent": "Dani random"},
                           allow_redirects=False)
    data = get_sub.json().get('data', {}).get('children', {})
    if get_sub.status_code != 200 or not data:
        return print("None")
    for post in data:
        print(post.get('data', {}).get('title'))

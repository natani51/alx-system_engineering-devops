#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import pprint
import requests


URL = 'https://www.reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-agent': 'dani random'}
    params = {"g": "GLOBAL"}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    get_sub = requests.get(URL.format(subreddit),
                           headers=headers,
                           params=params,
                           allow_redirects=False)
    if get_sub.status_code != 200:
        return None
    data = get_sub.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)

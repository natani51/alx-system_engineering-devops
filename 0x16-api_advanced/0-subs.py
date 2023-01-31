#!/usr/bin/python3
"""
Queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-agent': 'dani random'}
    URL = 'https://www.reddit.com/r/{}/about.json'
    get_sudreddit = requests.get(URL.format(subreddit),
                                 headers=headers, allow_redirects=False)
    if get_sudreddit.status_code != 200:
        return 0
    return get_sudreddit.json().get('data', {}).get('subscribers')

#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays 
the body of the response.
"""

from sys import argv
import requests


if __name__ == '__main__':

    url = argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)

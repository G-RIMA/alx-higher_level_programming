#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))

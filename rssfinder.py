#!/usr/bin/env python3

import requests
import sys

rsslist=[
        'rss',
        'atom',
        'atom.xml',
        'rss.xml',
        'feed',
        'index.rdf',
        'index.xml'
        ]
def usage():
    print(f"./{sys.argv[0]} [top.url]")


def main():
    url=sys.argv[1]
    if not url.endswith('/'):
        url+='/'

    for p in rsslist:
        resp=requests.get(url+p)
        if resp.status_code==200:
            print(f"   Find!! {url+p}")
        else:
            print(f"Not Found {url+p}")


if __name__ == '__main__':
    if len(sys.argv)<2:
        usage()
        exit()
    main()

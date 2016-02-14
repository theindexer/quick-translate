#! /usr/bin/env python
import argparse
import urllib
import json

def read(url):
    return json.loads(urllib.urlopen(url).read())

def translate(args):
    key = "YOUR_KEY_HERE"
    query = args.query
    target = args.target
    source = args.source
    result = read("https://www.googleapis.com/language/translate/v2?key=" + key + "&source=" + source + "&target=" + target + "&q=" + query + "&format=text")
    print result["data"]["translations"][0]["translatedText"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="target language", default="ja")
    parser.add_argument("--source", help="source language", default="en")
    parser.add_argument("query", help="text to translate")
    translate(parser.parse_args())





#!/usr/bin/env python
"""
web.py - Web Facilities
Copyright sfan5, 2014
"""

import re
import urllib
import urllib.request
import urllib.parse
import requests
import json as jsonlib
from html.entities import html5 as name2codepoint

user_agent = "Mozilla/5.0 (compatible; Phenny; +https://github.com/asl97/phenny)"

def get(uri, amount=-1):
	global user_agent
	r = requests.get(uri, headers={"User-Agent": user_agent})
	return r.content, r.status_code

def head(uri):
	global user_agent
	r = requests.head(uri, headers={"User-Agent": user_agent})
	return r.headers, f.status_code


def post(uri, query):
	global user_agent
	r = requests.post(uri, data=query, headers={"User-Agent": user_agent})
	return r.content, f.status_code

def entity(match):
	value = match.group(1).lower()
	if value.startswith('#x'):
		return chr(int(value[2:], 16))
	elif value.startswith('#'):
		return chr(int(value[1:]))
	elif (value + ';') in name2codepoint:
		return name2codepoint[value + ';']
	return '[' + value + ']'

r_entity = re.compile(r'&([^;\s]+);')

def decode(html):
	return r_entity.sub(entity, html)

def json(text):
	return jsonlib.loads(text)

def urlencode(text):
	return urllib.parse.quote_plus(text)


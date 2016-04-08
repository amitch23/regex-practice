# from http://www.python-course.eu/re.php
import re

sent1 = "Hello, you."
sent2 = "Customer number: 232454, Date: February 12, 2011."

phone = "510 364-5555"
url = "/articles/1234/22/99999"
xml = "<composer>Wolfgang Amadeus Mozart</composer>"
html = "<ul><li>list item 1</li></ul>"

def matching_basics(sent1, phone):
	match_search = re.search(r"y", sent1)
	match_search1 = re.search(r"o..", sent1)
	# Match from beginning of str, 3 or more characters that are digits
	# i.e. does this string start with an area code?
	match_search2 = re.search(r"^[0-9]{3,}", phone)

	result1 = "Result of matching 'y' for '%s': '%s'" % (sent1, match_search.group())
	result2 = "Result of matching 'o..' for '%s': '%s'" % (sent1, match_search1.group())
	result3 = "Result of using carets and quantifiers for '%s': '%s'" % (phone, match_search2.group())

	return "%s \n%s\n%s" % (result1, result2, result3)

def match_using_groups(sent2):
	# Capture in a group any sequence of consecutive digits, then any character after
	# for 0 or more, colon, space, second group of any character set of any length
	match_object = re.search(r"([0-9]+).*: (.*)", sent2)
	
	result = "Result of using groups for '%s'. \nGroup 1: '%s' \nGroup 2:'%s'" % (sent2, match_object.group(1), match_object.group(2))
	return "%s" % (result)

def match_url(url):
	result = re.search(r"^/articles/([0-9]{4})/([0-9]{2})/([0-9]+)$", url)
	return "Result of matching url a la django url conf: %s" % result.group()

def find_and_fix(xml, html):

	"""Change xml line to: "composer: Wolfgang Amadeus Mozart"""
	"""Change html line to: "List item 1"""

	# Capture in first group any letter sequence of length 1 or more
	# Second group: sequence of any characters of any length 
	
	result1 = re.search(r"^<([a-z]+)>(.*)</\1>", xml)
	result2 = re.search(r"^<([a-z]+)><([a-z]+)>(.*)</\2></\1>", html)

	return "xml: %s\nhtml: %s \n" % ((result1.group(1) + ": " + result1.group(2)), (result2.group(3)))

# def find_things(text1):

# 	txt = open(text1)
# 	   for line in txt:
# 	# 	do stuff

if __name__ == "__main__":
	print matching_basics(sent1, phone)
	print match_using_groups(sent2)
	print match_url(url)
	print find_and_fix(xml, html)
	# find_things("the-little-man-Galsworthy.txt")


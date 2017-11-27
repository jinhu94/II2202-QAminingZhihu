# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    content = ""
    def handle_data(self, data):
        self.content += data


def content_analyze(str1):
	"""
	Receive a HTML string
	Return a tuple (content, length of content, # of images, # of links)
	"""
	count_img = str1.count("<img")
	count_link = str1.count("<a href")

	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser() 
	parser.feed(str1)
	content = parser.content.strip("\n")
	length = len(content)
	return (content, length, count_img, count_link)


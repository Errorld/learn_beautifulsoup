#coding: utf-8

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
def decorator(f):
	def fn(thing):
		print('fuck')
		return f(thing)
	return fn
@decorator
def printer(thing):
	print(thing)

string='god'
printer(string)

soup = BeautifulSoup(html_doc, 'html.parser')
# soup_name = [ k for k,v in locals().iteritems() if v is soup][0]
# won't work with dict
# I just can't get the name of a variable.
# Therefore, the following is:
input('press to print soup.title')
print(soup.title)
input('press to print soup.title.name')
print(soup.title.name)
input('press to print soup.title.string')
print(soup.title.string)
input('press to print soup.p')
print(soup.p)
input('press to print soup.a')
print(soup.a)
input('press to print soup.find_all("a")')
print(soup.find_all('a'))
input('press to print soup.find(id="link3")')
print(soup.find(id='link3'))
input('press to print soup.get_text()')
print(soup.get_text())

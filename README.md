#learn_beautifulsoup

##begin to learn
2015-09-22 16:37:40

- add readme.md
- add soup1.py
 - enumerate some usages of BeautifulSoup

###encountered a problem when I want to derive the *name of a variable* from a *variable*

find a answer on Zhihu,which is:

> **no** method to do so


- [original answer](http://www.zhihu.com/question/20403362/answer/15050144)
'cause Python holds no such a useful function and implement no pre-processing.*I guse*
also got something:
 - global() gives a dict which contains{variableName, value}

but can't get the variableName with no clue


- [form Stack Overflow](http://stackoverflow.com/questions/2553354/how-to-get-a-variable-name-as-a-string-in-python)
on Stack Overflow, I got a piece of useful but dangrous code:
```
blah = 1
blah_name = [ k for k,v in locals().iteritems() if v is blah][0]
```
not perfect, but may *work*.

> This is not possible in Python, which really doesn't have "variables". Python has names, and there can be more than one name for the same object.

###personal problem solved by eval()
```
def decorator(f):	#prictice decoration
	def fn(thing):
		input("press to print("+thing+")")
		return f(thing)
	return fn
	
@decorator
def printer(string):
	print(eval(string))

L = ['soup.title', 'soup.title.name', 'soup.title.string',\
 'soup.p', 'soup.a', 'soup.find_all("a")', \	#add strings here
 'soup.find(id="link3")', 'soup.get_text()']	#be ware of the 'and"
soup = BeautifulSoup(html_doc, 'html.parser')

for i in L:
	printer(i)
```
**I must be a genius**
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-22/22355254.jpg)
*************
##something wrong here
2015-09-22 19:38:19

- add dict.py
    - get translation from iciba in comman mode
    - uses like:![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-22/29069834.jpg)
    - actually this is the begining of my learning about BeautifulSoup

> Somehow I figured out that this is not what a readme should be like
I need a blog maybe

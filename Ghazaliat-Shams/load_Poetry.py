import urllib
from lxml import html
import xml.etree.cElementTree as ET


url = 'http://ganjoor.net/moulavi/shams/ghazalsh/sh'
#page = html.fromstring(urllib.urlopen(url).read())

a = []
def dfs(p,a):
	#print p.tag
	#print p.get('class')
	if p.tag == 'div' and (p.get('class')=='m1' or p.get('class')=='m2'):
		for child in p:
			a.append(child.text)
		#print 'what the boor?'
	for child in p:
		dfs(child,a)
def extract_poem(page):
	a = []
	dfs(page,a)
	return a

root = ET.Element('root')
poems = []
for i in range(1,26):
	#print extract_poem(page)
	poems.append(ET.SubElement(root,'Poem',name=str(i)))
for i in range(25):
	page = html.fromstring(urllib.urlopen(url+str(i+1)).read())
	this_poem = extract_poem(page)
	for j in range(len(this_poem)):
		ET.SubElement(poems[i],'Beit',name=str(j)).text = this_poem[j]

tree = ET.ElementTree(root)
tree.write('Poem.xml',encoding='utf-8')

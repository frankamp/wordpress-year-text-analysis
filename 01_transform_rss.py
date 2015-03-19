import os
import codecs
import xml.dom.minidom
from xml.dom.minidom import Node
import re
import datetime
import html2text
html2text.BODY_WIDTH = 0

start_ordinal = 735233

def parse_poem(item):
    poem = item.getElementsByTagName('content:encoded')[0].childNodes[0].nodeValue
    title = item.getElementsByTagName('title')[0].childNodes[0].nodeValue
    matches = re.search(r"\d+", title)
    if matches:
        number = matches.group()
    else:
        print "couldn't find a number in ", title
        raise Exception("BOOM")
    pub_date = item.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
    pub_date = datetime.datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S +0000")
    poem = html2text.html2text(poem)
    return number, title, poem, pub_date


for f in os.listdir('rss'):
    if f.endswith('.xml'):
        print "parsing", f
        dom = xml.dom.minidom.parse('rss/' + f)
        items = dom.getElementsByTagName('item')
        for item in items:
            number, title, poem, pub_date = parse_poem(item)
            number = "%03d" % int(number)
            ordinal_of_year = pub_date.date().toordinal() - start_ordinal
            ordinal_of_year = "%03d" % int(ordinal_of_year)
            with codecs.open('poems/' + ordinal_of_year + "_" + number + ".txt", 'w', 'utf-8') as w:
                w.write(poem)

            
            
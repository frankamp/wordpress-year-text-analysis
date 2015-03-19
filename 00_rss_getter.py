import requests
import codecs
start_page = 1
end_page = 38

def get_article_rss(n):
    u = "http://grahammurtaugh.com/?feed=rss2&paged=" + str(n)
    return requests.get(u).text

print "doing stuff!"
for i in range(start_page, end_page+1):
    print "getting", i
    resp = get_article_rss(i)
    print "ok"
    padded = "%02d" % int(i)
    with codecs.open("rss/%s.xml" % padded, 'w', 'utf-8') as w:
         w.write(resp)
print "done"
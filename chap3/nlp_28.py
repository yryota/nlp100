# -*- coding: utf-8 -*-
from collections import Counter
import re
with open('English.txt','r') as f:
    s = ''.join(f.readlines())
    a = re.search(u'基礎情報.*\n\|',s)
    b = re.search(r'[}]+\n',s[a.start():])
    l = re.split(u'\n[\|]+',s[a.end():a.start()+b.start()-1])
    d = {}
    for word in l:
        c = re.search(r'(.*?)(?=\s=)',word)
        e = re.search(r'(?<=\s=\s)(.*)',word)
        d.update({word[:c.end()]:word[e.start():]})
for k in d:
    v = re.sub(r'\'{2,5}',r'',d[k])
    v = re.sub(r'(.*?\[\[)(.+?)(\]\].*?)',r'\2',v)
    d.update({k:v})
for k in d:
    v = re.sub(r'<.*?>',r'',d[k])
    d.update({k:v})
    v = re.sub(r'\[.*?\]',r'',d[k])
    d.update({k:v})
print(d)

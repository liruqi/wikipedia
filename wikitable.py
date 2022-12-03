# -*- coding: utf-8 -*-
# wikitable: fix wikitable syntax on wikipedia
# Copyright © 2022, Ruqi Li <liruqi@gmail.com>
 
import pywikibot
import json
import os
import re
import sys

LANG='zh'
if len(sys.argv) == 1:
    site = pywikibot.Site('zh', 'wikipedia')  # The site we want to run our bot on
    page = pywikibot.Page(site, '镇江南站')
    print (page.text)
    page.text = page.text.replace('{|table ', '{| ')
    page.save('Fix wikitable syntax')  # Saves the page
    exit(1)

LANG=sys.argv[1]
site = pywikibot.Site(LANG, 'wikipedia') 
BASEDIR="../../wikipedia." + LANG
ERRORDIR=os.path.join(BASEDIR, "Errors")
names = [f for f in os.listdir(ERRORDIR)]
cnt=0
action='beginning'
debug=False
if len(sys.argv)>2:
    action=sys.argv[2].lower()

WT_BEGIN_PATTERN=r'{\|(\s*)table'
WT_BEGIN_TEXT='{|'

WT_SOURCE_PATTERN=r'{\|(\s*)class\=wikitable(\s*)sortable(\s*)(\w+)='
WT_SOURCE_TEXT=r'{| class="wikitable sortable" \4='

S_PATTERN=WT_BEGIN_PATTERN
R_TEXT=WT_BEGIN_TEXT
if action=='style': #TODO: This mode is buggy now
    S_PATTERN=r'{\|(.*)style=([^=|\!]*)'
    R_TEXT=None
    debug=True
elif action[0]=='s':
    S_PATTERN=WT_SOURCE_PATTERN
    R_TEXT=WT_SOURCE_TEXT

def rebuildStyle(t):
    if action != 'style':
        return None
    q=[]
    for mo in re.finditer(S_PATTERN,t):
        s = mo.start()
        e = mo.end()
        if mo.group(0).count('"') == 2:
            continue
        q.append(mo)
        print ('String match "%s" at %d:%d' % (t[s:e], s, e))
    if len(q)==0:
        return None
     
    def fixStyle(s):
        frags=s.replace('"',' ').replace(';',' ').split()
        attribs=[]
        st=0
        name=""
        for f in frags:
            if len(f)==0:
                continue
            if st==2: #value
                if len(name)==0:
                    exit(5)
                attribs.append(name+":"+f)
                st=0
                continue 
            nv=f.split(':')
            if st==1:
                if f==':':
                    st+=1
                elif len(nv)>1:
                    attribs.append(name+":"+nv[1])
                continue
                    
            if len(nv)==1:
                name=nv[0]
                st=1
            elif nv[1]=='':
                name=nv[0]
                st=2
            else:
                attribs.append(f)
        return "; ".join(attribs) 
    
    print('debug:',len(q))
    while q:
        mo = q.pop()
        ss=fixStyle(mo.group(2))
        print(mo.group(2),'->',ss)
        others=mo.group(1).strip().strip(";")
        rep='{| '+others+' style="'+ss+'"' + "\n" 
        t=t[:mo.start()] + rep + t[mo.end():]
    return t
 
for name in names:
    if name[-8:] == ".err.log":
        cnt+=1
        d=0
        with open (os.path.join(ERRORDIR, name)) as f:
            err=f.read()
            mo=re.search(S_PATTERN,err)
            if mo == None:
                continue
            print(mo.group(0))
            print(cnt, "Found:", name[:-8], "->", err)
            page = pywikibot.Page(site, name[:-8])
            ptext=page.text
            if action=='style':
                ntext=rebuildStyle(ptext)
                if ntext==None:
                    continue
            else:
                ntext=re.sub(S_PATTERN, R_TEXT, ptext)
            if ptext == ntext:
                print("wikitable error not found.")
                os.remove(os.path.join(ERRORDIR, name))
                continue
            page.text=ntext
            if debug:
                print (ntext)
            else:
                page.save('Fix wikitable ' + action + ' syntax, src: https://github.com/liruqi/wikipedia/blob/master/wikitable.py')
            wt=os.path.join(ERRORDIR, name[:-8]+".wikitext")
            if os.path.isfile(wt) and LANG=="zh":
                with open(wt,"w") as wtf:
                    wtf.write(ntext)
            d=1
            
        if d==1:
            os.remove(os.path.join(ERRORDIR, name))
            if LANG!="zh":
                wt=os.path.join(ERRORDIR, name[:-8]+".wikitext")
                if os.path.isfile(wt):
                    os.remove(wt)


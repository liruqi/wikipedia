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
    os.exit(1)

LANG=sys.argv[1]
site = pywikibot.Site(LANG, 'wikipedia') 
BASEDIR="../../wikipedia." + LANG
ERRORDIR=os.path.join(BASEDIR, "Errors")
WT_PATTERN=r'{\|(\s*)table'
names = [f for f in os.listdir(ERRORDIR)]
cnt=0
for name in names:
    if name[-8:] == ".err.log":
        cnt+=1
        d=0
        with open (os.path.join(ERRORDIR, name)) as f:
            err=f.read()
            mo=re.search(WT_PATTERN,err)
            if mo == None:
                continue
            print(mo.group(0))
            print(cnt, "Found:", name[:-8], "->", err)
            page = pywikibot.Page(site, name[:-8])
            ptext=page.text
            ntext=re.sub(WT_PATTERN, '{|', ptext)
            if ptext == ntext:
                print("wikitable error not found.")
                os.remove(os.path.join(ERRORDIR, name))
                continue
            page.text=ntext
            page.save('Fix wikitable beginning syntax')  # Saves the page
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


# -*- coding: utf-8 -*-
# wikitable: fix wikitable syntax on wikipedia
# Copyright © 2022, Ruqi Li <liruqi@gmail.com>
 
import pywikibot
import json
import os
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
names = [f for f in os.listdir(ERRORDIR)]
cnt=0
for name in names:
    if name[-8:] == ".err.log":
        cnt+=1
        d=0
        with open (os.path.join(ERRORDIR, name)) as f:
            err=f.read()
            if err.find('{|table ') == -1:
                continue
            print(cnt, "Found:", name[:-8], "->", err)
            page = pywikibot.Page(site, name[:-8])
            ptext=page.text
            ntext=ptext.replace('{|table ', '{| ')
            if ptext == ntext:
                print("wikitable error not found.")
                os.remove(os.path.join(ERRORDIR, name))
                continue
            page.text=ntext
            page.save('Fix wikitable syntax')  # Saves the page
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


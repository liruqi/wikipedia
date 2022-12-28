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
if action=='style':
    S_PATTERN=r'{\|(.*)style=([^|\!]*)'
    R_TEXT=None
    debug=False
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
        if mo.group(0).count('{{') > 0:
            continue
        if q and s<q[-1].end()+6: #probably got more 1 style=xxx in a line 
            q.pop()
        q.append(mo)
        print ('String match "%s" at %d:%d' % (t[s:e], s, e))
    if len(q)==0:
        return None
     
    def fixStyle(s):
        frags=s.replace('"',';').replace('\'',';').split(';')
        print("frags:", frags)
        attribs=[]
        st=0
        attrName=""
        tableAttr={}

        def updateStyle(f,st,attribs,tableAttr):
            TableAttrNames=["cellspacing", "cellpadding", "class", "align", "bgcolor", "nowrap"]
            global attrName
            print('updateStyle:',f,st,attribs,tableAttr)
            if len(f)==0:
                return (st,attribs,tableAttr)
            if st==2: #value
                if len(attrName)==0:
                    exit(5)
                if attrName in TableAttrNames:
                    tableAttr[attrName]=f
                elif attrName!="style":
                    attribs.append(attrName+":"+f)
                st=0
                return (st,attribs,tableAttr)
 
            nv=f.split(':')
            if len(nv)==1:
                nv=f.split('=')
            if st==1:
                if f==':' or f=='=':
                    st+=1
                elif len(nv)>1:
                    attribs.append(attrName+":"+nv[1])
                    attrName=''
                return (st,attribs,tableAttr)
                    
            if len(nv)==1:
                if re.fullmatch('\w+', nv[0]):
                    attrName=nv[0].lower()
                    st=1
            elif nv[1]=='':
                if re.fullmatch('\w+', nv[0]):
                    attrName=nv[0].lower()
                    st=2
            else:
                attrName=nv[0].lower().strip()
                attrValue=nv[1].lower().strip()
                #print("nv:",nv)
                if attrName in TableAttrNames:
                    if attrName!="align" and (attrValue not in TableAttrNames):
                        tableAttr[nv[0]]=nv[1]
                elif attrName=='':
                    return (st,attribs,tableAttr)
                elif attrName=='style':
                    return updateStyle(attrValue,st,attribs,tableAttr)
                elif attrName in ['color']:
                    v=nv[1].strip()
                    idx=v.find(" ")
                    if idx==-1: 
                        attribs.append(attrName+":"+v)
                    else:
                        attribs.append(attrName+":"+v[:idx])
                        return updateStyle(v[idx:],st,attribs,tableAttr)
                else:
                    attribs.append(attrName+":"+nv[1])
            return (st,attribs,tableAttr)
        for f in frags:
            f=f.strip()
            st,attribs,tableAttr = updateStyle(f,st,attribs,tableAttr)
        
        return ["; ".join(attribs), tableAttr]
    
    print('debug:',len(q))
    while q:
        mo = q.pop()
        ss,tableAttr=fixStyle(mo.group(2))
        print(mo.group(2),'==>',ss,str(tableAttr))
        others=mo.group(1).strip().strip(";").strip("|")
        rep='{| '+others
        if tableAttr:
            rep=rep+' '+ " ".join([ k+'="'+tableAttr[k]+'"' for k in tableAttr])
        if len(ss):
            rep=rep+' style="'+ss+'"' 
        rep=rep+"\n" 
        print(mo.group(0),'->',rep)
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
                print ("---DEBUG:", name, "---")
            else:
                page.save('Fix ' + LANG + ' wikitable ' + action + ' syntax, [[User:Liruqi/wikitable]]', minor=True)
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


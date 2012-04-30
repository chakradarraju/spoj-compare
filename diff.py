#! /usr/bin/env python
from pyquery import PyQuery as pyq
from urllib2 import HTTPError as httperror
import sets, sys, re
try: CONFIG = open("config.dat","r")
except Exception, e: raise
try: configtext = CONFIG.read()
except Exception, e: raise
pattern = re.compile("\\n([\w_]+)[\t ]*([\w: \\\/~.-]+)")
config = dict((x[0],x[1]) for x in re.findall(pattern,configtext))
tocompare = []
if(len(sys.argv)==1): tocompare.append(raw_input())
else:
    for args in sys.argv[1:]:
        if(args!="!"): tocompare.append(args)
done = False
for args in sys.argv[1:]:
    if(args=="!"):
        try: FILE = open("mysolved.dat","r")
        except Exception, e: raise
        try: probtext = FILE.read()
        except Exception, e: raise
        problist = probtext.split()
        FILE.close()
        done = True
if(done==False):
    print "Fetching your solved problems..."
    try: me = pyq(url='http://www.spoj.pl/users/'+config['myhandle']+'/')
    except httperror, e: raise
    try: FILE = open("mysolved.dat","w")
    except Exception, e: raise
    probtext = me('.content').find('table').eq(2).text()
    try: FILE.write(probtext)
    except Exception, e: raise
    FILE.close()
    problist = probtext.split()
solved = sets.Set(problist)
for handle in tocompare:
    print "Fetching "+handle+"'s solved problems..."
    try: other = pyq(url='http://www.spoj.pl/users/'+handle+'/')
    except httperror: print "User "+handle+" Not Found"
    else:
        if(other('.content').find('table').eq(0).text().split()[1]==handle):
            print handle+":"
            for prob in other('.content').find('table').eq(2).text().split():
                if(prob not in solved): print prob
        else: print "User "+handle+" not found"

#! /usr/bin/env python
myhandle = "chakradarraju"
from pyquery import PyQuery as pyq
import sets
import sys
problist = []
done = False
for args in sys.argv[1:]:
    if(args=="!"):
        FILE = open("mysolved.dat","r")
        problist = FILE.read().split()
        done = True
if(done==False):
    print "Fetching your solved problems..."
    me = pyq(url='http://www.spoj.pl/users/'+myhandle+'/')
    FILE = open("mysolved.dat","w")
    probtext = me('.content').find('table').eq(2).text()
    FILE.write(probtext)
    problist = probtext.split()
solved = sets.Set(problist)
tocompare = []
if(len(sys.argv)==1):
    tocompare.append(raw_input())
else:
    for args in sys.argv[1:]:
        if(args!="!"):
            tocompare.append(args)
for handle in tocompare:
    print "Fetching "+handle+"'s solved problems..."
    try:
        other = pyq(url='http://www.spoj.pl/users/'+handle+'/')
        if(other('.content').find('table').eq(0).text().split()[1]==handle):
            print handle+":"
            for prob in other('.content').find('table').eq(2).text().split():
                if(prob not in solved):
                    print prob
        else:
             print "User "+handle+" not found"
    except urllib2.HTTPError:
        print "User "+handle+" Not Found"

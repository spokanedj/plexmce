#this is my file

mypath = "c:\\users\\public\\recorded tv"

from datetime import datetime, date, time

import win32com.client
sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)

from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) & f.endswith(".wtv") ]
print (onlyfiles)

ns = sh.NameSpace(mypath)

targetcols = ['Title', 'Genre', 'Rating', 'Length', 'Subtitle', 'Parental rating', 'Episode name', 'Broadcast date', 'Program description', 'Station call sign']
colnames = []
colnumbs = []

for colnum in range(0,1024):
    colname=ns.GetDetailsOf(None, colnum)
    if colname:
        for t in targetcols:
            if t == colname:
                colnames.append(colname)
                colnumbs.append(colnum)

##for counter, colnum in enumerate(colnames):
##    print (counter, colnum)

for item in ns.Items():
    if isfile(item.Path)& item.Path.endswith(".wtv"):
        print (item.Path)
        for colnum in range(len(targetcols)):
            colval=ns.GetDetailsOf(item, colnumbs[colnum])
            if colval:
                print('\t', colnumbs[colnum], colnames[colnum], ":", colval)


struct_time = datetime.strptime("10/9/2014 16:30 AM", "%m/%d/%Y %H:%M %p")

print ("returned tuple:", struct_time)

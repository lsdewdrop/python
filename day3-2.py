__author__ = 'user'

import allview
import sinchung
import delete
import listveiw

while 2:

    print "1. all view  2. sinchung  3. delete  4. your list view  5. close"
    n=input()
    if n==1:
        moklok={}
        allview.all_view(moklok)
    elif n==2:
        sinchung.sinchung()
    elif n==3:
        delete.delete()
    elif n==4:
        listveiw.listveiw()
    else:
        break

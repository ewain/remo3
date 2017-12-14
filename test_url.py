# coding: utf-8
import urllib.request
import re
import urllib.request
req = urllib.request.Request(
    'http://www.sport247.live/it/home', 
    data=None, 
    headers={
        'User-Agent': 'Mozilla'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

response = urllib.request.urlopen('http://www.sport247.live/it/home')
leggo = response.read()
print ('#HTML#', leggo)
#print ('#FineHTML#')
header= response.getheaders()
#print ('header: ',header)
status= response.status
#print ('status: ',status)

diretta = re.finditer("Diretta", str(leggo))
if diretta:
    print('qui')
    for istanza_m in diretta:
        print('posizione',istanza_m.start())
        print('istanza_m.group',istanza_m.group())
        print ('istanze: ', istanza_m) 
else:
    print('non trovato')

#print (diretta)
print('---fine diretta---')

match = re.search(' [0-9][0-9][0-9][0-9] ', str(leggo))
print (match)


match2 = re.finditer(' [0-9][0-9][0-9][0-9] ', str(leggo))
#print (match2)
i=0
for anno in match2:
    i+=1
    print(anno.span())
    #print ('match n°',i,':', anno.group(0),sep='')

print('------------')
match3 = re.finditer('NewsHeadline', str(leggo))
#print (match3)

#print ('list3: ',list3)
i=0
for news in match3:
    i+=1
    print (news.span())
    #print ('distro n°',i,':', anno.group(0),sep='')

print('------------seconda versione-----------------')
match4 = re.finditer(' [0-9][0-9][0-9][0-9] ', str(leggo))
#print (match4)
list1=list(match4)
print('------------')
match5 = re.finditer('NewsHeadline', str(leggo))
#print (match5)
list2=list(match5)
#print ('list3: ',list3)
listAll=list1+list2
print ('lsitAll: ',listAll)
print ('----FINE----')
       
       
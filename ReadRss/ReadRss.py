#import library to do http requests:
import urllib2
import urllib

#import MySQLdb
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
 #.....
 
 
 # if you want to open file in a directory
 # file = open('rss.xml')
 #  print file.read()

 
#download the file:
file = urllib2.urlopen('http://www.somedomain.com/somexmlfile.xml')

# or

urlLink = "http://feeds.bbci.co.uk/news/rss.xml"
file = urllib2.urlopen(urlLink)


#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()

#parse the xml you downloaded
dom = parseString(data)

    #-------------- 
from xml.dom import minidom

 # file = urllib2.urlopen('http://feeds.bbci.co.uk/news/world/rss.xml')

xmldoc = minidom.parse(urllib2.urlopen(urlLink))

itemlist = xmldoc.getElementsByTagName('item') 

numOfINews = len(itemlist)
print " numOfINews :",numOfINews



#------------------ Using numOfINews+1 coz of the page title so, by sing +1 will be ignored
for i in range (0,numOfINews+1):


    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name title:
    xmlTagTitle = dom.getElementsByTagName('title')[i+1].toxml()
    #strip off the tag (<title>data</title>  --->   data) 
    xmlDataTitle = xmlTagTitle.replace('<title>','').replace('</title>','').encode('utf-8').strip()
    
    
    xmlTagDescription = dom.getElementsByTagName('description')[i].toxml()
    #strip off the tag (<tag>data</tag>  --->   data):
   
#
# xmlDataDescription = xmlTagDescription.replace('<description>','').replace('</description>','')
 #   """
   
    # ---- To Solve    #--------  UnicodeEncodeError: 'ascii' codec can't encode character u'\xa3'

    xmlDataDescription = xmlTagDescription.replace('<description>','').replace('</description>','').encode('utf-8').strip()

    
    xmlTagLink = dom.getElementsByTagName('link')[i+1].toxml()
    #strip off the tag (<tag>data</tag>  --->   data):
    xmlDataLink = xmlTagLink.replace('<link>','').replace('</link>','').encode('utf-8').strip()
    
    if i == 0:
            print "-----------------------------------------------------------------------------------------------"
            #just print the data
            print "------------------------------------ [", xmlDataTitle,"] -------------------------------------"
            print "-----------------------------------------------------------------------------------------------"
    
    else:    
        #print out the xml tag and data in this format: <tag>data</tag>
        print "Tiltel :", i, xmlDataTitle
        
         #print out the xml tag and data in this format: <tag>data</tag>
        print "Description :", xmlDataDescription
             #print out the xml Link and data in this format: <tag>data</tag>
        print "Link :", xmlDataLink,"\n"





# --------



"""
url = 'http://10.0.2.2/android_connect/create_calls.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }




data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()


"""


"""
from xml.dom import minidom


xmldoc = minidom.parse('rss.xml')
itemlist = xmldoc.getElementsByTagName('item') 
print len(itemlist)
print itemlist[0].attributes['title'].value
for s in itemlist :
    print s.attributes['title'].value
"""
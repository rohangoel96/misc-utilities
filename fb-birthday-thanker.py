import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

token='-----------' #facebook user access token here with extented permissions to post 
facebook=fb.graph.api(token)
graph = GraphAPI(token)
since_date = "1391212800" #unix time stamp

def getMessage(id):
    query2=id+'?fields=message,from'
    r2 = graph.get(query2)
    name = r2['from']['name']
    text = 'Thank You '+name+' :)'

    print "\nMessage : " + r2['message'].split('\n')[0]
    print "Comment : " + text 
    return text


def thank():

    query="me/posts?fields=id&limit=500&since="+since_date
    r=graph.get(query)
    
    
    
    idlist=[x['id'] for x in r['data']]
    idlist.reverse()
    print("There are "+ str(len(idlist)) +" posts since "+since_date)
    
    char1=raw_input("Are you sure you want to comment? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of posts to be commented ")
        # mess=raw_input("Enter the message to be commented: ")
        if nos<=len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
              mess = getMessage(indid)
                     
              facebook.publish(cat="comments",id=indid,message=mess) #Comments on each post
              facebook.publish(cat="likes",id=indid)                 #Likes each post
              count=count+1
              print("Notification number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
        else: 
              print("Not that many posts available")
    else :
      print("No commenting then.")

thank()

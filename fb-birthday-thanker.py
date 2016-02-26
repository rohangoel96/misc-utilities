import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

#facebook user access token here with extented permissions to post | https://developers.facebook.com/tools/explorer
token='------' 
facebook=fb.graph.api(token)
graph = GraphAPI(token)
since_date = "1391212800" #unix time stamp

def getComment(id):

    query = id+'?fields=message,from'
    result = graph.get(query)
    commentor_name = result['from']['name']
    comment = 'Thank You ' + commentor_name +' :)'

    print "\nPost : " + result['message'].split('\n')[0] #prints only the first line of post
    print "Comment : " + comment 
    return comment


def ThankAndLike():

    query="me/posts?fields=id&limit=500&since="+since_date
    result=graph.get(query)
    
    idlist=[x['id'] for x in result['data']] #post id's of all the posts in the time-frame
    idlist.reverse() #order it from recent to old
    print("There are "+ str(len(idlist)) +" posts since "+since_date)
    
    char1=raw_input("Are you sure you want to comment? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of posts to be commented ")
        
        if nos<=len(idlist):
           for p_id in (idlist[(len(idlist)-nos):]):
              mess = getComment (p_id)
              print p_id
              print mess
              facebook.publish(cat="comments",id=p_id,message=mess) #Comments on each post
              facebook.publish(cat="likes",id=p_id)                 #Likes each post
              count=count+1
              print("Notification number:"+str(count)+" on www.facebook.com/"+str(p_id).split('_')[0]+"/posts/"+str(p_id).split('_')[1])
        else: 
              print("Not that many posts available")
    else :
      print("No commenting then.")

ThankAndLike()

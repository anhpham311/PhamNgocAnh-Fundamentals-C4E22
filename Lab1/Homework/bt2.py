from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
import datetime

#Connect to database
client = MongoClient(uri)
db = client.get_default_database()

#Collection 
posts = db['posts']  #insert_one (C), find (R)

#Create a document
post = {
    "title": "Cam nghi ve C4E22 ",
    "content": 'Coding that la kho. Nhung thay Huy giang rat de hieu. Toi can phai co gang hon trong hoc tap va lam bai tap cham chi hon',
    "author": 'Annie',
    "date": datetime.datetime.now(),
}

#Insert created document 
posts.insert_one(post)
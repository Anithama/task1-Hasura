from flask import Flask,jsonify,render_template
import requests

import json

app = Flask(__name__)

@app.route("/author")
def home():
    uri = "https://jsonplaceholder.typicode.com/users"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

  

    return render_template('author.html',authors=data)
@app.route("/post")
def home1():
    uri = "https://jsonplaceholder.typicode.com/posts"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

  

    return render_template('post.html',posts=data)
@app.route("/count")
def home2():
   uri1 = "https://jsonplaceholder.typicode.com/users"
   uri2 = "https://jsonplaceholder.typicode.com/posts"
   try:
       uResponse1 = requests.get(uri1)
       uResponse2 = requests.get(uri2)
   except requests.ConnectionError:
      return "Connection Error"  
   Jresponse1 = uResponse1.text
   Jresponse2 = uResponse2.text
   data1 = json.loads(Jresponse1)
   data2 = json.loads(Jresponse2)
   carr=[]
   for a in data1:
      ct=0
      d={}
      for p in data2:
         if a['id']==p['userId']:
            ct=ct+1	
      d['Name']=a['name']
      d['count']=ct
      carr.append(d)
   return render_template('count.html',res=carr)    
  

    
if __name__ == "__main__":
    app.run(debug = True)
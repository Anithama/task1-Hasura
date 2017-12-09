from flask import Flask, redirect, url_for, request,render_template,make_response
app = Flask(__name__)

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   age2 = request.cookies.get('Age')
   return '<h1> Stored key values:'+name+'with age '+age2+'</h1>'



if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask, redirect, url_for, request,render_template,make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      age1 = request.form['age']
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   resp.set_cookie('Age', age1)
   return resp   




if __name__ == '__main__':
   app.run(debug = True)
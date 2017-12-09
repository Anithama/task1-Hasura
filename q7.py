from flask import Flask, redirect, url_for, request,render_template,make_response
app = Flask(__name__)

@app.route('/input')
def index():
   return render_template('q7.html')

@app.route('/result', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      
   print(user)
   return user 




if __name__ == '__main__':
   app.run(debug = True)
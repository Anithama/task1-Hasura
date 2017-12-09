from flask import Flask, redirect, url_for, request,render_template,make_response,abort
app = Flask(__name__)



@app.route('/html')
def index():
   return render_template('index.html')
@app.route('/image')
def login():
    return redirect('https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2016/03/1458289957powerful-images3.jpg')

if __name__ == '__main__':
   app.run(debug = True)
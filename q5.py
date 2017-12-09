from flask import Flask, redirect, url_for, request,render_template,make_response,abort
app = Flask(__name__)



@app.route('/robots1.txt')
def login1():
    abort(403)	
@app.route('/robots.txt')
def login():
    return redirect('http://httpbin.org/deny')

if __name__ == '__main__':
   app.run(debug = True)
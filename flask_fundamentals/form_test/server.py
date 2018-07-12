from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/user/<username>/<idn>')
def show_user_profile(username, idn):
    print username
    print idn
    return render_template("redirect.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   # redirects back to the '/' route
   #return render_template('redirect.html')
   return redirect('/show')
'''
@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])
  '''

@app.route('/show')
def show_user():
  return render_template('user.html')

app.run(debug=True) # run our server

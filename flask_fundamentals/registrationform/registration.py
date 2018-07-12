from flask import Flask, render_template, request, redirect,flash,session
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_REGEX = re.compile(r'^[a-zA-Z]+$')
UPPERDIGIT_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z]).+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/result',methods=['POST'])
def result():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    if len(first_name) < 1:
        flash("First Name CANNOT be left blank!")
        return redirect('/')
    elif name_REGEX.match(first_name):
        flash("Invalid First Name")
        return redirect('/')

    elif len(last_name) < 1:
        flash("Last Name CANNOT be left blank!")
        return redirect('/')
    elif name_REGEX.match(last_name):
        flash("Invalid Last Name")
        return redirect('/')

    elif len(email) < 1:
        flash("Email CANNOT be left blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email")
        return redirect('/')   

    elif len(password) < 1:
        flash("Password CANNOT be left blank!")
        return redirect('/')
    elif len(password) < 8:
        flash("Password must be longer than 8 characters!")
        return redirect('/')
    elif not UPPERDIGIT_REGEX.match(password):
        flash("Password must contain at least one upper case letter and one digit")
        return redirect('/')

    elif len(confirm_password) < 1:
        flash("Please confirm password")
        return redirect('/')

    elif password != confirm_password:
        flash("Passwords don't match!")
        return redirect('/')
    else:
        return render_template('result.html')

    return redirect('/')

@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)




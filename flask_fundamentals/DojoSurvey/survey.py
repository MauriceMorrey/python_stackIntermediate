from flask import Flask, render_template, request, redirect,flash,session
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("survey.html")

@app.route('/results', methods=['GET','POST'])
def results():
   print "Got Post Info"
   #return "here"
   if len(request.form['name']) < 1:
     flash("Name cannot be empty!")
   else:
      flash("Success! Your name is {}".format(request.form['name']))

   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment =  request.form['comment']
   if len(request.form['comment']) <1:
      flash('You also need to add a comment')
      return redirect('/')
   elif len(request.form['comment']) >=121:
      flash('Comment is larger than 120 characters')
      return redirect('/')
   return render_template('results.html', name = name, location = location, language = language, comment = comment)
   #return redirect('/')
    
app.run(debug=True) 
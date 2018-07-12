from flask import Flask , render_template, request, redirect, session, flash
import random

app=Flask(__name__)
app.secret_key='ala_gong_zhu'

@app.route('/')
def index():
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    print "You chose number:", session['number']
    return render_template('greatN.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess_num = int(request.form['number'])
    your_guess = ""
    
    if guess_num == session['number']:
        your_guess= 'Right on!'
    
    elif guess_num < session['number']:
        your_guess = 'Too low!'
        
    elif guess_num > session['number']:
        your_guess = 'Too high!'

	return redirect('/')

app.run(debug = True)
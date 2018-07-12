from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "SecretKey"
import random
import time
messages = []

@app.route('/')
def index():
	if session.get('goldcount'):
		pass
	else:
		session['goldcount'] = 0
	return render_template('gold.html', messages=messages)

@app.route('/process_gold', methods=['POST'])
def gold():
	if request.form['action'] == 'farm':
		value = random.randrange(9, 21)
		session['goldcount'] += value
		messages.insert(0,("Earned " + str(value) + " gold from the farm! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	
	elif request.form['action'] == 'cave':
		value = random.randrange(4, 11)
		session['goldcount'] += value
		messages.insert(0,("Earned " + str(value) + " gold from the farm! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	
	elif request.form['action'] == 'house':
		value = random.randrange(2, 6)
		session['goldcount'] += value
		messages.insert(0,("Earned " + str(value) + " gold from the farm! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	
	elif request.form['action'] == 'casino':
		value = random.randrange(-50,51)
		session['goldcount'] += value
		if value > 0:
			messages.insert(0,("Earned " + str(value) + " gold from the farm! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
		else:
			messages.insert(0,("Entered a casino and lost " + str(value) + "gold...Ouch.." + str(time.strftime("%d/%m/%Y %I:%M %p"))))

	return redirect('/')

@app.route('/reset')
def reset():
	session.pop('goldcount')

	for i in range(0, len(messages)):
		messages.pop()

	return redirect('/')

app.run(debug=True)
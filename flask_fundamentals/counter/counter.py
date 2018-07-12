from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "count_alan_gongzhu"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] =0
    counter = session["counter"]
    return render_template('counter.html', counter = counter)

@app.route( '/ninjaL2', methods = ['POST'] )
def ninja_level2():
    session['counter'] += 1
    return redirect( '/' )

@app.route( '/reset', methods = ['POST'] )
def reset():
    session['counter'] = 1
    return redirect( '/' )

app.run( debug = True )

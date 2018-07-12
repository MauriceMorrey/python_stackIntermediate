from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("turtles.html")

@app.route('/ninja/<color>')
def one_ninja(color):
    return render_template("turtle.html", color = color)

app.run(debug=True) 
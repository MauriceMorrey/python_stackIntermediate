from flask import Flask, render_template  

app = Flask(__name__)                     

@app.route('/') 
def welcome():
    return render_template('portfolio.html',name="Maurice",phrase="hello", times=5) 

@app.route('/projects')
def my_projects():
  return render_template('projects.html')

@app.route('/about')
def about_me():
  return render_template('about.html')
                                             
app.run(debug=True)                       
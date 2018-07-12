from flask import Flask, render_template  

app = Flask(__name__)                     

@app.route('/')   

@app.route('/world')
def world():
  return render_template('world.html')
                                             
app.run(debug=True)                       
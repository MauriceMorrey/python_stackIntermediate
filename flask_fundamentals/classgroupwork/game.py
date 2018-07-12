from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.config['SECRET_KEY']='blormp'

@app.route("/")

def home():
    return render_template("index.html")
    
@app.route("/fail/<id>")

def fail(id):
    if 'num' in session:
        session['num']+=1
    else:
        session['num'] = 0
    num = session['num']
    if id == "2":
        failure_message = "Pat's smile vanishes into thin air. 'Dogs?  You like DOGS? I can't stand them, and I can't stand you.  You aren't fit to date me.  Let me take you somewhere where you'll feel more at home.' Within less than a second, a bag is thrown over your head.  The insides smell like raw steak and hot dogs.  You are dragged for what feels like hours and left on the ground, struggling to escape. 'Have fun with your friends,' you hear, alongside the pitter-patter of hungry feet and ravenous growls.  Looks like you made a bad first impression."
    elif id == "3":
        failure_message = "Pat's face stretches to its extremities.  'PIE??? You... absolute scoundrel!  And to think I was just starting to like you.  Well, if you simply must have your pie, I'm happy to oblige.' You nervously sip your water glass and realize your vision is starting to go blurry.  The next thing you know, you're inside an oven covered with cherries, apples, and rhubarb.  Looks like someone got a little indecisive with their ironic murder. 'Now's your chance to impress me,' you hear over the faint sound of dials turning.  Your hot date is about to get a little hotter."
    else:
        failure_message = "Pat simply blinks, slowly and menacingly. You didn't think a blink could be menacing, but you've learned a lot tonight. 'Tea.  Had to be tea.  Such a waste.  Well, if you're set in your ways, I suppose I won't stand between you and your happiness.  Let's have some tea.' Just then, a plane crashes into the restaurant and kills you.  OOOOOOPS!!!"
    return render_template("fail.html", failure_message=failure_message, num=num)

@app.route("/success/<id>" )

def success(id):
    if id == "1" :
        question = "This is the worst date of your life, and possibly your last.  Pat stares across the dinner table at you, eyes twitching, with a smile that holds no joy.  'So tell me about yourself,' Pat says.  'Are you a cat person or a dog person?'"
        answer1 = 'Cat person'
        answer2 = 'Dog person'
    elif id == "2" :
        question = "'Good.  I can't stand dogs, and I can't tolerate people who like dogs.  I think we'll get along nicely.' You sigh with relief, but it doesn't last long. Pat's brief smirk fades back into the same empty smile from before.  'What do you want for dessert?  Cake or pie?'"
        answer1 = 'Cake'
        answer2 = 'Pie'
    elif id == "3" :
        question = "'That's a good choice.  Pie is quite bad for you, especially if I catch you eating it.'  Looks like you dodged another bullet, blade, or whatever else you shudder to think might be in Pat's pockets.  But Pat doesn't seem fully satisfied as the unsuspecting waiter cluelessly delivers your cake. 'I need a little pick-me-up before we leave.  I get angry when I get tired.  Should we get some coffee or tea?'"
        answer1 = 'Coffee'
        answer2 = 'Tea'
    else:
        return render_template("victory.html")
    next_id = int(id)+1
    next_id = str(next_id)
    return render_template("success.html", question=question, id=next_id, answer1=answer1, answer2=answer2)


@app.route("/reset")

def reset():
    session['num'] = 0
    return redirect("/")

app.run(debug=True)

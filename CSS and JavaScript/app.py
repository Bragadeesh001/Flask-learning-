#import required libraries
from flask import Flask,render_template,url_for,redirect
from flask import Flask, request

#create the opbject
app=Flask(__name__)

#index page
@app.route('/')
def index():
    return render_template('index.html')

#Action form
@app.route('/submit',methods=["POST","GET"])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])
        computer=float(request.form['computer science'])
        total_score=(science+maths+english+computer)/4
    
    return redirect(url_for('result',score=total_score))

#result url
@app.route('/result/<int:score>')
def result(score):
    if score>=50:
        res='pass'
    else:
        res='fail'
    dic={'score':score,'result':res}
    return render_template('result.html',results=dic)

#to run
if __name__=='__main__':
    app.run(debug=True)
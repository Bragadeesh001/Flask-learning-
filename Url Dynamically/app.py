#import the libraries
from flask import Flask,redirect,url_for

#creating object
app=Flask(__name__)

#index page
@app.route('/')
def index():
    return 'Program to show the person is pass or fail'

#pass url
@app.route('/passed/<int:score>')
def passed(score):
    return 'The Student passed with the score: '+str(score)   

#fail url 
@app.route('/failed/<int:score>')
def failed(score):
    return 'The Student has failed with the score: '+str(score)

#url dynamic
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks>50:
        result="passed"
    else:
        result="failed"
    return redirect(url_for(result,score=marks))


#to run
if __name__=='__main__':
    app.run(debug=True)
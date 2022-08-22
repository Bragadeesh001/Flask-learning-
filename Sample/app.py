#import the libraries
from flask import Flask

#create an object
app=Flask(__name__)

#create web pages
@app.route('/')
def index():
    return "Hello Bragadeesh"

@app.route('/Bragadeesh')
def Bragadeesh():
    return "hey bragadeesh, this is a sample flask program"

if __name__=="__main__":
    app.run(debug=True)
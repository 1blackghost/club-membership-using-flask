'''
This is the main file of vehicle billing
'''
#imports
from flask import *

#Creation of flask app
app=Flask(__name__)
app.secret_key="FORADDONCOURSE"

#Main Entry Point Here.
@app.route("/")
def home():
    return render_template("index.html")

with app.app_context():
    #importing views from different files
    from simple_view import *

if __name__=="__main__":
    app.run(debug=True)
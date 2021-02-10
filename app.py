from process import insta
from flask import Flask,request,render_template
import requests




app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        user = request.form.get("kadi")
        passwd = request.form.get("pass")
        return  render_template("index.html",info=insta(user,passwd))
    else:
        return  render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)
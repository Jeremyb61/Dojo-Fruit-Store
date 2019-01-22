from flask import Flask,render_template, render_template, redirect, request
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def store():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print("suck it", request.form)

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M")
    
    return render_template("index2.html", x=date_time)

@app.route('/fruits',methods=['GET'])
def fruits():
    print("Apples are my favorite sport")
    return render_template("fruits.html")


if __name__=="__main__":
    app.run(debug=True)

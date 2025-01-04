from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/analyze", methods=['POST'])
def analyze():
    user_input = float(request.form['user_input'])

    if user_input > 0:
        return "True"
    
    else:
        return "false"

@app.route("/analyze2", methods=['POST'])
def analyze2():
    user_input = float(request.form['user_input'])

    if user_input % 2 == 0:
        return "True"
    
    else:
        return "false"



if __name__ == '__main__':
    app.run(debug=True)

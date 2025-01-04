from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 052f9df3aacaf461db78eb10fa9b12afe3b24b74

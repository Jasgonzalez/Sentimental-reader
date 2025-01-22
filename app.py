from flask import Flask, render_template,request
from transformers import pipeline
import torch


app = Flask(__name__)

device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/analyze", methods=['POST'])
def analyze(): 

    user_input = request.form.get('user_input', '')  # Safely get user input
    if not user_input.strip():
        return render_template('home.html', analysis="Please provide valid input text.")
    
    try:

        # perform the classification
        analysis = classifier(user_input)
        
        # find the highest rated classification
        highest_emotion = max(analysis[0], key = lambda x: x ['score'])
        
        # Prepare the result message
        result_message = f"Emotion: {highest_emotion['label']}"

        return render_template('home.html', analysis=result_message)
    except Exception as e:
        return render_template('home.html', analysis=f"Error during analysis: {str(e)}")


    
'''
@app.route("/analyze2", methods=['POST'])
def analyze2():
    user_input = float(request.form['user_input'])

    if user_input % 2 == 0:
        result = "True"
    
    else:
        result =  "false"

    return render_template('home.html', result = result)
'''

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from ai_engine import get_ai_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    personality = request.form['personality']
    response = get_ai_response(user_message, personality)
    return jsonify({'response': response})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

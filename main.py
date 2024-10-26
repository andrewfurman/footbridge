from flask import Flask, render_template, request, jsonify
from generate_conversation import generate_conversation

app = Flask(__name__)

@app.route('/')
def create_conversation():
    return render_template('create_conversation.html')

@app.route('/create', methods=['POST'])
def create():
    prompt = request.form.get('prompt')
    conversation = generate_conversation(prompt)
    return jsonify(conversation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, request

app = Flask(__name__)


responses = {
    'hello': 'Helloo, how can I assist you?',
    'hi': 'Helloo, how can I assist you?',
    'hey': 'Helloo, how can I assist you?',
    'what is your name?': 'I am your virtual bot using Flask.',
    'how are you?': 'I am doing great, thank you! How can I help you?',
    'quit': 'Goodbye! Have a nice day!'
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    return 'I did not understand that. Please try again.'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['GET'])
def bot_response():
    user_input = request.args.get("msg")
    return chatbot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)

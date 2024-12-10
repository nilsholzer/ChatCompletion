from flask import Flask, render_template, url_for, request, jsonify
from openai import OpenAI

app = Flask(__name__)

#Gets the Open API key from the file API_KEY
API_KEY = open("API_KEY", "r").read()

client = OpenAI(api_key=API_KEY)

#Renders the index.html file
@app.route('/')
def index():
    return render_template('index.html')

#Chat route that takes in a POST request with a JSON object containing the message
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    data = request.get_json()
    message = data.get("message")

    #Generates the response from the AI
    def generate():
        stream = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "The following is a conversation with an AI assistant."},
                {"role": "user", "content": message}
            ],
            stream=True
        )

        #Yields every partial response from the AI until the final response is reached
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield(chunk.choices[0].delta.content)

    
    return generate(), {"Content-Type": "text/plain"}


if(__name__ == '__main__'):
    app.run(debug=True)
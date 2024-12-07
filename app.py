from flask import Flask, render_template, url_for, request, jsonify
import openai

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])

def chat():
    """
    
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"message": "Message is required"}), 400
    
    try:
        response = openai.Completion.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "The following is a conversation with an AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return jsonify({"message": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"message": str(e)}), 500
        """
    return render_template('index.html')

if(__name__ == '__main__'):
    app.run(debug=True)
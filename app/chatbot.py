from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json

        if not data or "messages" not in data:
            return jsonify({"error": "Messages are required"}), 400

        messages = data["messages"]

        # Send message to OpenAI API
        response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                store=True,
                stream=True
        )

        def generate():
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        return app.response_class(generate(), content_type="text/plain")

    except Exception as e:
        print("ERROR: ", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

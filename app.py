import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_ai(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    reply = ask_ai(user_input)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
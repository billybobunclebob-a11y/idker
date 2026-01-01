from flask import Flask, request, jsonify, render_template
from optimus import optimus_groq_generate

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    print("Received from frontend:", user_message)

    reply = optimus_groq_generate(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request
from send_whatsapp import send

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("extend.html")


@app.route("/send", methods=["POST"])
def members():
    data = request.form.to_dict(flat=True)
    send(**data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=28311)  # watch

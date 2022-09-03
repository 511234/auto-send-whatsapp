from flask import Flask, render_template, request
from send_whatsapp import send

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("extend.html")


@app.route("/send", methods=["POST"])
def members():
    data = request.form.to_dict(flat=True)
    send(**data)
    return "Nice!"


if __name__ == "__main__":
    app.run()

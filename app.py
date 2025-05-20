from flask import Flask, render_template
from flask_talisman import Talisman
from dotenv import load_dotenv
import os


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

Talisman(app, content_security_policy=None)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/prices")
def prices():
    return render_template("prices.html")

if __name__ == "__main__":
    app.run()

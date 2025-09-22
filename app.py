from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(24)
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
entries = []


@dataclass
class Entry:
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    happiness: str = ""  # Neues Feld für Happiness


@app.route("/")
def index():
    return render_template("index.html", entries=entries)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_password = request.form.get("password")
        if user_password == PASSWORD:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect password. Please try again.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        flash("You must be logged in to add an entry.", "error")
        return redirect(url_for("login"))
    content = request.form.get("content")
    happiness = request.form.get("happiness", "")
    if content:
        entry = Entry(content=content, happiness=happiness)
        entries.append(entry)
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

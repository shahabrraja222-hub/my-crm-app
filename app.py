from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Home page → login
@app.route("/")
def home():
    return render_template("login.html")

# Login POST route
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Simple check (admin credentials)
    if username == "admin" and password == "admin123":
        return "Admin logged in!"  # future: redirect to admin dashboard
    else:
        return "Invalid credentials! Try again."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


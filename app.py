from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Dummy clients data (temporary)
clients = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com"},
    {"id": 2, "name": "Ahmed", "email": "ahmed@gmail.com"}
]

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Admin login
    if username == "admin" and password == "admin123":
        return render_template("admin_dashboard.html", clients=clients)

    # Client login
    for client in clients:
        if username == client["name"] and password == "123":
            return render_template("client_dashboard.html", client=client)

    return "Invalid credentials"

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_client(id):
    for client in clients:
        if client["id"] == id:
            if request.method == "POST":
                client["name"] = request.form.get("name")
                client["email"] = request.form.get("email")
                return redirect(url_for("home"))
            return render_template("edit_client.html", client=client)

    return "Client not found"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


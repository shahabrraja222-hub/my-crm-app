from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

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

    if username == "admin" and password == "admin123":
        return render_template("admin_dashboard.html", clients=clients)

    for client in clients:
        if username == client["name"] and password == "123":
            return render_template("client_dashboard.html", client=client)

    return "Invalid login"


@app.route("/add", methods=["POST"])
def add_client():
    name = request.form.get("name")
    email = request.form.get("email")

    new_id = len(clients) + 1
    clients.append({"id": new_id, "name": name, "email": email})

    return redirect(url_for("home"))


@app.route("/delete/<int:id>")
def delete_client(id):
    global clients
    clients = [c for c in clients if c["id"] != id]
    return redirect(url_for("home"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_client(id):
    for client in clients:
        if client["id"] == id:
            if request.method == "POST":
                client["name"] = request.form.get("name")
                client["email"] = request.form.get("email")
                return redirect(url_for("home"))
            return render_template("edit_client.html", client=client)

    return "Not found"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



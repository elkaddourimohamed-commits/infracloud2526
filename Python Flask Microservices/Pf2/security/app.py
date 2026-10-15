from flask import render_template

@app.route("/signup-form")
def signup_form():
    return render_template("signup_form.html")

@app.route("/login-form")
def login_form():
    return render_template("login_form.html")

from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    if Email.validate(request.form):
        Email.save(request.form)
        return redirect("/success")
    else:
        return redirect("/")

@app.route('/unique', methods=["POST"])
def unique():
    data = {
        "email":request.form["email"],
    }
    email_in_db = Email.get_by_email(data)
    if not email_in_db:
        flash("Unique email confirmed!")
    else:
        flash("Invalid, email exists!")
    return redirect("/")

@app.route('/success')
def success():
    email = Email.get_all()
    return render_template("success.html", email=email)

@app.route("/delete/<int:id>")
def delete_email(id):
    data = {
        "id":id
    }
    Email.delete_email(data)
    flash("Success! email was deleted. Bye Bye.")
    return redirect("/")



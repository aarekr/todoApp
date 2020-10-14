from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # validations

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


# creating new user
@app.route("/auth/register")
def user_registration():
    return render_template("auth/newuserform.html", form=NewUserForm())


@app.route("/auth/newuser")
def create_new_user():
    print ("uuden userin luonti")
    form = NewUserForm(request.form)
    username = request.form.get("username")
    password = request.form.get("password")

    u = User(username, username, password)
    db.session().add(u)
    db.session().commit()

    #return redirect(url_for("account_created"))
    return redirect(url_for("index"))

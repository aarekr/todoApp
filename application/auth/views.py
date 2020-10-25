from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm

@app.route("/auth/allusers")
def all_users():
    return render_template("auth/allusers.html", all_users=User.all_users())

@app.route("/auth/myprofile")
def my_profile():
    return render_template("auth/myprofile.html", my_tasks=User.my_tasks())

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


# creating new users
@app.route("/auth/register")
def user_registration():
    return render_template("auth/newuserform.html", form=NewUserForm())

@app.route("/auth/newuser", methods=["POST"])
def create_new_user():
    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/newuserform.html", form=form)
    username = request.form.get("username")
    password = request.form.get("password")

    u = User(username, username, password)
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("account_created"))

@app.route("/auth/accountcreated")
def account_created():
    return render_template("auth/accountcreated.html")

# deleting user accounts
@app.route("/auth/deleteuser/<user_id>/", methods=["POST"])
@login_required
def delete_user(user_id):
    deleted_user = User.query.get(user_id)
    db.session().delete(deleted_user)
    db.session().commit()
    return redirect(url_for("account_deleted"))

@app.route("/auth/accountdeleted")
def account_deleted():
    return render_template("auth/accountdeleted.html")

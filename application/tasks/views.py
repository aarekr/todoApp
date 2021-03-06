from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.tasks_and_users(), total_number_of_tasks=Task.total_number_of_tasks())

@app.route("/tasks/", methods=["POST"])
@login_required #(role="ADMIN")
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    t = Task(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):
    t = Task.query.get(task_id)
    if t.done == True:
        t.done = False
    else:
        t.done = True

    db.session().commit()
    return redirect(url_for("tasks_index"))

@app.route("/changetaskowner/<user_id>/", methods=["POST"])
@login_required
def tasks_take_ownership(user_id):
#    print("*****Task: " + task2_id)
    print("*****User: " + user_id)

    return redirect(url_for("tasks_index"))

from flask import Flask, render_template, request, redirect, url_for, app
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@application.before_first_request  # It creates the database and all the necessary tables if does not exist
def create_tables():
    db.create_all()


@application.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@application.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if len(title) > 0:
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for("home"))


@application.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@application.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    application.run(host="0.0.0.0")

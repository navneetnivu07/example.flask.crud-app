import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hum = db.Column(db.String(10), unique=False)
    # co = db.Float(db.Float, nullable=True, unique=False)
    # tvoc = db.Float(db.Float, nullable=True, unique=False)
    # vib = db.Float(db.Float, nullable=True, unique=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    

    def __repr__(self):
        return '<Id %r>' % self.id

    def to_json(self):
        return {
            'id': self.id,
            'hum': self.hum,
            'time': self.time,
        }

@app.route("/sensor", methods=["GET", "POST"])
def sensor():
    sensor_val = None
    if request.form:
        try:
            sen = Sensor(hum=float(request.form.get("hum")))
            print("%%%%%%%%")
            print(request.form.get("hum"))
            db.session.add(sen)
            db.session.commit()
        except Exception as e:
            print("Failed to add sensor value")
            print(e)
        return "success"
    else:
        sensor_val = Sensor.query.all()
        return jsonify(values=list(s.to_json() for s in sensor_val))
        #return render_template("sensor.html", books=sensor_val)
 

@app.route("/", methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    return render_template("sensor.html")


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)


# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Urls(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     long = db.Column(db.String())
#     short = db.Column(db.String(3))

#     def __init__(self, long, short):
#         self.long = long
#         self.short = short

# # This function will be executed once before the first request to the application.
# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route('/', methods=["POST", "GET"])
# def home():
#     if request.method == "POST":
#         url_received = request.form["nm"]
#         # Add code here to store the received URL in the database
#         # For example:
#         # url_entry = Urls(long=url_received, short='XYZ')
#         # db.session.add(url_entry)
#         # db.session.commit()
#         return "URL received: " + url_received
#     else:
#         return render_template("home.html")

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


# -------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key = True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(3))

    def __init__(self, long, short):
        self.long = long
        self.short = short
    
with app.app_context():
    db.create_all()

@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        url_received = request.form["nm"]
        return url_received
    else:
        return render_template("home.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
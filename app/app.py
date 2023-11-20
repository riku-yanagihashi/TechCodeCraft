import os

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}".format(
    user=os.environ.get("POSTGRES_USER"),
    passwd=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    port=os.environ.get("POSTGRES_PORT"),
    db=os.environ.get("POSTGRES_DB"),
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create")
def create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

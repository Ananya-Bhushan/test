from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql
from views.movie import movie_api

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.register_blueprint(movie_api)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin1234@127.0.0.1/API?ssl_disabled=true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()

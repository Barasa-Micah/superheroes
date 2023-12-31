from flask import Flask
from models import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#  We initialize the SQLAlchemy database

db.init_app(app)


if __name__ == '__main__':
    # Creating the database tables if they don't exits that is
    with app.app_context():
     db.create_all()

    app.run(debug=True)
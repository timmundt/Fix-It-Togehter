from flask import Flask
from routes import main
from database import db, insert_skills


app = Flask(__name__)
app.register_blueprint(main)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datastorage.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_skills()
    app.run(debug=True)

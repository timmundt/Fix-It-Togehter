from flask import Flask
from blueprints.staticpage_routes import staticpages_r
from blueprints.auth_routes import auth_r
from blueprints.customer_routes import customer_r
from database import db, insert_skills


app = Flask(__name__)
app.register_blueprint(staticpages_r)
app.register_blueprint(auth_r)
app.register_blueprint(customer_r)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datastorage.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_skills()
    app.run(debug=True)

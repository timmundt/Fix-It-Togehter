from flask import Flask
from flask_login import LoginManager
from blueprints.staticpage_routes import staticpages_r
from blueprints.auth_routes import auth_r
from blueprints.chat_routes import chat_r
from blueprints.customer_routes import customer_r
from blueprints.repairer_routes import repairer_r
from blueprints.review_routes import review_r
from database import User, db, insert_dummy_data, insert_skills


app = Flask(__name__)
app.config['SECRET_KEY']='1234567890'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datastorage.db'
db.init_app(app)

login_manger=LoginManager()
login_manger.init_app(app)
login_manger.login_view='auth.login'

#Quelle ChatGPT

app.register_blueprint(staticpages_r)
app.register_blueprint(auth_r)
app.register_blueprint(chat_r)
app.register_blueprint(customer_r)
app.register_blueprint(repairer_r)
app.register_blueprint(review_r)


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Quelle ChatGPT


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_skills()
        insert_dummy_data()
    app.run(debug=True)

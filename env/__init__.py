from flask import Flask


def Create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ayomitan'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prifix='/')
    app.register_blueprint(auth, url_prifix='/')

    return app

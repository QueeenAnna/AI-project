from dotenv import load_dotenv
from flask import Flask
# from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)
    # _app.config.from_pyfile('settings.py')
    #
    # from app.persistence.db import init_db
    # init_db(_app)

    # login_manager = LoginManager()
    # login_manager.init_app(_app)

    # @login_manager.user_loader
    # def load_user(user_email):
    #     from app.controllers.user_controller import get_user_by_email
    #     return get_user_by_email(user_email)

    from app.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    # from app.blueprints.user import bp_user
    # _app.register_blueprint(bp_user, url_prefix='/user')

    return _app


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run()


from dotenv import load_dotenv
from flask import Flask
# from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)

    from app.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    # from app.blueprints.user import bp_user
    # _app.register_blueprint(bp_user, url_prefix='/user')

    return _app


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run(host='0.0.0.0', port=int('5000'))


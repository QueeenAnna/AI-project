from dotenv import load_dotenv
from flask import Flask


def create_app():
    _app = Flask(__name__)

    from app.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    return _app


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run(host='0.0.0.0', port=int('5000'))

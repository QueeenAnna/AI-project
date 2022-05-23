from flask import Blueprint, render_template

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('index.html')


@bp_open.get('/categories')
def categories():
    return render_template('categories.html')


@bp_open.get('/recipes')
def recipes():
    return render_template('recipes.html')


def main():
    pass


if __name__ == '__main__':
    main()

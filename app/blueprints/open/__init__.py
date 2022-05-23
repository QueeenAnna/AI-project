from flask import Blueprint, render_template, request

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('index.html')


@bp_open.get('/categories')
def categories_get():

    categories = ['30-minutes-or-less', 'desserts', 'inexpensive', 'fish', 'meat', 'vegetarian']

    return render_template('categories.html', categories=categories)

@bp_open.post('/categories')
def categories_post():
    categories = ['30-minutes-or-less', 'desserts', 'inexpensive', 'fish', 'meat', 'vegetarian']

    chosen = []
    for category in request.form:
        if category in categories:
            chosen.append(category)



@bp_open.get('/recipes')
def recipes():
    return render_template('recipes.html')


def main():
    pass


if __name__ == '__main__':
    main()


import webbrowser
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
from app.controllers import recipe_controller as rc
from app.controllers.camera import Video
from app.controllers.camera import Video, FoodDetection
import cv2

bp_open = Blueprint('bp_open', __name__)

# video_stream = FoodDetection(capture_index=1, model_name='trained_model\model_150_epoches.pt')
# detector = FoodDetection(capture_index=1, model_name='trained_model\model_150_epoches.pt')
# video_stream()

detector = FoodDetection(capture_index=1, model_name='./controllers/trained_model/model_150_epoches.pt')
detector()


@bp_open.get('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@bp_open.get('/video')
def video():
    return Response(gen(detector()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@bp_open.get('/categories')
def categories_get():
    # Manage problem with naming that is inconsistent with database!!!
    categories = ['30 Minutes Or Less', 'Desserts', 'Inexpensive', 'Fish', 'Meat', 'Vegetarian']


    return render_template('categories.html', categories=categories)


@bp_open.post('/categories')
def categories_post():
    # Labels and c from index_post()
    labels = []
    c = 'above 10 frames'
    recipes, ingredients = rc.get_recipes(labels, c)  # Skip ingredients?

    # Manage problem with naming that is inconsistent with database!!!
    categories = ['30-minutes-or-less', 'desserts', 'inexpensive', 'fish', 'meat', 'vegetarian']

    chosen = []
    for category in request.form:
        if category in categories:
            chosen.append(category)

    sorted_recipes = rc.sort_by_category(recipes, chosen)
    return redirect(url_for('bp_open.recipes_get', sorted_recipes=sorted_recipes))

@bp_open.get('/recipes')
def recipes_get():
    return render_template('recipes.html')


def main():
    # Code for getting recipe image with url
    r = requests.get("https://www.food.com/recipe/red-lobster-cheddar-bay-biscuits-89684")
    print(r.text)

    soup = BeautifulSoup(r.text, "html.parser").find_all('div', attrs={
        'class': 'recipe-default-image recipe-hero__item theme-gradient svelte-jlgald'})
    image = soup[0].contents[1].attrs['src']
    webbrowser.open(image)
    print()


if __name__ == '__main__':
    main()

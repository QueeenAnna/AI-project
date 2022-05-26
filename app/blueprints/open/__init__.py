from flask import Blueprint, render_template, request, Response
from app.controllers.camera import Video
from app.controllers.camera import Video, FoodDetection
import cv2

bp_open = Blueprint('bp_open', __name__)

# video_stream = FoodDetection(capture_index=1, model_name='trained_model\model_150_epoches.pt')
# detector = FoodDetection(capture_index=1, model_name='trained_model\model_150_epoches.pt')
# video_stream()

detector = FoodDetection(capture_index=1, model_name='model_150_epoches.pt')
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

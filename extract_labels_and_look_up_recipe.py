import os
import csv
import webbrowser
from collections import Counter
import re


def get_labels():
    directory = 'yolov5.0/runs/detect/exp7/labels'  # Change to /exp/labels
    rows = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(directory + '/' + filename, 'r') as f:
                rows += f.readlines()

    count_all = Counter([int(row.split()[0]) for row in rows])
    count_above_10 = Counter({k: c for k, c in count_all.items() if c >= 10})
    return count_above_10


def get_recipes(labels, c):
    ingredients = [label for label in labels if labels.index(label) in c.keys()]
    recipes = []

    with open('RAW_recipes.csv', 'r', encoding='utf-8') as infile:
        read = csv.reader(infile)
        for row in read:
            recipe = {'name': '',
                      'id': 0,
                      'description': '',
                      'ingredients': []}
            for i in ingredients:
                if i in row[10]:
                    recipe['name'] = row[0]
                    recipe['id'] = row[1]
                    recipe['description'] = row[9]
                    recipe['ingredients'].append(i)

            recipes.append(recipe)

    # Removes empty dicts in list
    recipes = [i for i in recipes if i]
    recipes = sorted(recipes, key=lambda d: len(d['ingredients']), reverse=True)
    return recipes


def convert_to_url(name, _id):
    base = 'https://www.food.com/recipe/'
    name = re.sub('[^A-Za-z0-9\-\s]+', '', name)
    name = '-'.join(name.split())

    url = f'{base}{name}-{_id}'
    webbrowser.open(url)



def main():
    # os.system("python detect.py --source 1 --weights ./trained_model/best.pt --save-txt")
    # python detect.py --source 1 --weights ./train_models/model_85_epochs.pt --
    labels = ['asparagus', 'banana', 'beans', 'bell pepper', 'broccoli', 'carrot', 'cheese', 'chicken', 'chili',  # 0-8
              'cucumber', 'egg', 'eggplant', 'garlic', 'ginger', 'lemon', 'lentils', 'milk', 'minced_meat',  # 9-17
              'olive_label', 'olives', 'onion', 'potato', 'red_onion', 'rhubarb', 'rice', 'salmon', 'spaghetti',  # 18-26
              'spinach', 'sun-dried_tomatoes', 'sun-dried_tomatoes_label', 'tomato_sauce', 'tomato', 'whipping_cream']
    c = get_labels()
    recipes = get_recipes(labels, c)

    convert_to_url(recipes[0]['name'], recipes[0]['id'])





    # print(recipes)

    # print(f'\nFound {len(recipes)} recipes out of 180000 recipes')


if __name__ == '__main__':
    main()

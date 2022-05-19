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

    with open('datasets/RAW_recipes.csv', 'r', encoding='utf-8') as infile:
        read = csv.reader(infile)
        for row in read:
            recipe = {'name': '',
                      'id': 0,
                      'description': '',
                      'ingredients': [],
                      'category': []}
            for i in ingredients:
                if i in row[10]:
                    recipe['name'] = row[0]
                    recipe['id'] = row[1]
                    recipe['description'] = row[9]
                    recipe['ingredients'].append(i)
            if len(recipe['ingredients']) > 0:
                if '30-minutes-or-less' in row[5]:
                    recipe['category'].append('30-minutes-or-less')
                if 'desserts' in row[5]:
                    recipe['category'].append('desserts')
                if 'inexpensive' in row[5]:
                    recipe['category'].append('inexpensive')
                if 'fish' in row[5]:
                    recipe['category'].append('fish')
                if 'meat' in row[5]:
                    recipe['category'].append('meat')
                if 'vegetarian' in row[5]:
                    recipe['category'].append('vegetarian')



            recipes.append(recipe)

    # Removes empty dicts in list and those without chosen categories (remove if wanted!)
    recipes = [i for i in recipes if i and len(i['category']) > 0]
    recipes = sorted(recipes, key=lambda d: len(d['ingredients']), reverse=True)

    return recipes, ingredients


def sort_by_category(recipes):
    choice = list(input('Which categories are you interested in? Choose on or more alternatives:\n'
                        '1. 30 minutes or less\n'
                        '2. Desserts\n'
                        '3. Inexpensive\n'
                        '4. Fish\n'
                        '5. Meat\n'
                        '6. Vegetarian'))
    choice = [int(i) for i in choice]
    categories = []
    for c in choice:
        if c == 1:
            categories.append('30-minutes-or-less')
        elif c == 2:
            categories.append('desserts')
        elif c == 3:
            categories.append('inexpensive')
        elif c == 4:
            categories.append('fish')
        elif c == 5:
            categories.append('meat')
        elif c == 6:
            categories.append('vegetarian')
    print()

    sorted_recipes = []
    for recipe in recipes:
        # Checking if the recipe contains all the chosen categories made by the user
        if all(item in recipe['category'] for item in categories):
            sorted_recipes.append(recipe)
    return sorted_recipes


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
    recipes, ingredients = get_recipes(labels, c)
    sorted_recipes = sort_by_category(recipes)
    convert_to_url(recipes[0]['name'], recipes[0]['id'])





    # print(recipes)

    # print(f'\nFound {len(recipes)} recipes out of 180000 recipes')


if __name__ == '__main__':
    main()

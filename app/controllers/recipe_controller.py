import datetime
import os
import csv
import pathlib
import webbrowser
import re


# Used to run model from terminal
def grade_or_update_recipe(name):
    grade = int(input(f'Please grade the recipe {name}, 1-5:\n'
                      '> '))
    graded_recipes = []
    grade_dict = {'name': name,
                  'grade:': grade,
                  'last_cooked': datetime.datetime.now()}
    graded_recipes.append(grade_dict)


def get_labels():
    path = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(path, 'exp/labels')
    directory = path
    rows = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(directory + '/' + filename, 'r') as f:
                rows += f.readlines()

    empty_list = []
    for row in rows:
        test = row.replace('\n', '')
        empty_list.append(test)
    mylist = list(set(empty_list))
    labels_list = [int(x) for x in mylist]

    return labels_list


def get_recipes(labels, c):
    ingredients = [label for label in labels if labels.index(label) in c]

    recipes = []
    path = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(path, 'RAW_recipes.csv')
    with open(path, 'r', encoding='utf-8') as infile:
        read = csv.reader(infile)
        for row in read:
            recipe = {'name': '',
                      'id': 0,
                      'description': '',
                      'ingredients': [],
                      'submitted': datetime.date,
                      'minutes': 0,
                      'category': []}
            for i in ingredients:
                if i in row[10]:
                    recipe['name'] = row[0]
                    recipe['id'] = row[1]
                    recipe['description'] = row[9]
                    recipe['ingredients'].append(i.strip())
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

    recipes = [i for i in recipes if i and len(i['category']) > 0]
    recipes = sorted(recipes, key=lambda d: len(d['ingredients']), reverse=True)

    return recipes, ingredients


def sort_by_category(recipes, categories):
    sorted_recipes = []
    for recipe in recipes:
        if all(item in recipe['category'] for item in categories):
            sorted_recipes.append(recipe)

    return sorted_recipes


def show_url(sorted_recipes):
    url_list_name = []
    url_list_id = []
    final_url_list = []

    for i in range(10):
        url_list_name.append(sorted_recipes[i]['name'])
        url_list_id.append(sorted_recipes[i]['id'])

    for i in range(10):
        base = 'https://www.food.com/recipe/'
        name = re.sub('[^A-Za-z0-9\-\s]+', '', url_list_name[i])
        name = '-'.join(name.split())
        _id = url_list_id[i]

        new_url = f'{base}{name}-{_id}'
        final_url_list.append(new_url)

    return final_url_list


# Used to run model from terminal
def show_top_recipes(sorted_recipes):
    print('These are the top five recipes for you:')
    for i in range(5):
        print(f'{i + 1}. {sorted_recipes[i]["name"].title()}\n'
              f'In this recipe you will use: {", ".join(sorted_recipes[i]["ingredients"])}\n')

    choice = int(input('Which recipe would you like to be directed to? '))

    convert_to_url(sorted_recipes[choice - 1]['name'], sorted_recipes[choice - 1]['id'])


def convert_to_url(self, name, _id):
    base = 'https://www.food.com/recipe/'
    name = re.sub('[^A-Za-z0-9\-\s]+', '', name)
    name = '-'.join(name.split())

    url = f'{base}{name}-{_id}'
    webbrowser.open(url)


def main():
    # Terminal commands:
    # os.system("python detect.py --source 1 --weights ./trained_model/best.pt --save-txt")
    # python detect.py --source 1 --weights ./train_models/model_85_epochs.pt --save-txt

    labels = ['wrong', 'asparagus', 'banana', 'beans', 'bell pepper', 'broccoli', 'carrot', 'cheese', 'chicken',
              'chili', 'cucumber', 'egg', 'eggplant', 'garlic', 'ginger', 'lemon', 'lentils', 'minced_meat',
              'not_food', 'olive_label', 'olives', 'onion', 'potato', 'red_onion', 'rhubarb', 'rice', 'salmon',
              'spaghetti', 'spinach', 'sun-dried tomatoes', 'sun-dried_tomatoes', 'sun-dried_tomatoes_label',
              'tomato sauce', 'tomato_sauce', 'tomato', 'whipping_cream']

    c = get_labels()

    recipes, ingredients = get_recipes(labels, c)
    sorted_recipes = sort_by_category(recipes)
    show_top_recipes(sorted_recipes)


if __name__ == '__main__':
    main()

import datetime
import glob
import os
import csv
import webbrowser
from collections import Counter
import re


class User:
    def __init__(self):
        self.grades = []  # List of dicts

    def grade_or_update_recipe(self, name):
        grade = int(input(f'Please grade the recipe {name}, 1-5:\n'
                          '> '))
        grade_dict = {'name': name,
                      'grade:': grade,
                      'last_cooked': datetime.datetime.now()}
        self.grades.append(grade_dict)

    def get_labels(self):
        # Count number of exp folders in run
        n_exp_folders = str(len(glob.glob('yolov5.0/runs/detect/exp*')))
        # If 1 folder is just named exp
        if n_exp_folders == '1':
            n_exp_folders == ''
        # Get latest exp folder
        directory = f'yolov5.0/runs/detect/exp' + n_exp_folders + '/labels'
        rows = []
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(directory + '/' + filename, 'r') as f:
                    rows += f.readlines()

        count_all = Counter([int(row.split()[0]) for row in rows])
        count_above_10 = Counter({k: c for k, c in count_all.items() if c >= 10})
        return count_above_10

    def get_recipes(self, labels, c):
        ingredients = [label for label in labels if labels.index(label) in c.keys()]
        recipes = []

        with open('datasets/RAW_recipes.csv', 'r', encoding='utf-8') as infile:
            read = csv.reader(infile)
            for row in read:
                recipe = {'name': '',
                          'id': 0,
                          'description': '',
                          'ingredients': [],
                          'submitted': datetime.date,  # ???
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

        # Removes empty dicts in list and those without chosen categories (remove if wanted!)
        recipes = [i for i in recipes if i and len(i['category']) > 0]
        recipes = sorted(recipes, key=lambda d: len(d['ingredients']), reverse=True)

        return recipes, ingredients

    def sort_by_category(self, recipes):
        choice = list(input('Which categories are you interested in? Choose on or more alternatives:\n'
                            '1. 30 minutes or less\n'
                            '2. Desserts\n'
                            '3. Inexpensive\n'
                            '4. Fish\n'
                            '5. Meat\n'
                            '6. Vegetarian\n'
                            '> '))
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

    def show_top_recipes(self, sorted_recipes):
        print('These are the top five recipes for you:')
        for i in range(5):
            print(f'{i+1}. {sorted_recipes[i]["name"].title()}\n'  # tilldela index -1 strängen 'and ' + index -1
                  f'In this recipe you will use: {", ".join(sorted_recipes[i]["ingredients"])}\n')

        choice = int(input('Which recipe would you like to be directed to? '))
        self.convert_to_url(sorted_recipes[choice-1]['name'], sorted_recipes[choice-1]['id'])

        choice2 = input(f'Did you cook {sorted_recipes[choice-1]["name"]}? y/n\n'
                        '> ')
        if choice2 == 'y':
            for grade in self.grades:
                if grade['name'] == sorted_recipes[choice-1]["name"]:
                    grade['last_cooked'] = datetime.datetime.now()
                else:
                    self.grade_or_update_recipe(sorted_recipes[choice - 1]["name"])
        else:
            choice3 = input('Do you want to see the recipes again? y/n\n'
                            '> ')
            if choice3:
                pass  # Show recipes again, else go back?

    def convert_to_url(self, name, _id):
        base = 'https://www.food.com/recipe/'
        name = re.sub('[^A-Za-z0-9\-\s]+', '', name)
        name = '-'.join(name.split())

        url = f'{base}{name}-{_id}'
        webbrowser.open(url)


def main():
    # os.system("python detect.py --source 1 --weights ./trained_model/best.pt --save-txt")
    # python detect.py --source 1 --weights ./train_models/model_85_epochs.pt --save-txt
    user = User()
    labels = ['asparagus', 'banana', 'beans', 'bell pepper', 'broccoli', 'carrot', 'cheese', 'chicken', 'chili',  # 0-8
              'cucumber', 'egg', 'eggplant', 'garlic', 'ginger', 'lemon', 'lentils', 'milk', 'minced_meat',  # 9-17
              'olive_label', 'olives', 'onion', 'potato', 'red_onion', 'rhubarb', 'rice', 'salmon', 'spaghetti',  # 18-26
              'spinach', 'sun-dried_tomatoes', 'sun-dried_tomatoes_label', 'tomato_sauce', 'tomato', 'whipping_cream']
    c = user.get_labels()
    recipes, ingredients = user.get_recipes(labels, c)  # ingredients may be unnecessary
    sorted_recipes = user.sort_by_category(recipes)
    user.show_top_recipes(sorted_recipes)


if __name__ == '__main__':
    main()

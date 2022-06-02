import datetime
import os
import csv
import pathlib
import re


def convert_to_url(name, _id):
    base = 'https://www.food.com/recipe/'
    name = re.sub('[^A-Za-z0-9\-\s]+', '', name)
    name = '-'.join(name.split())

    url = f'{base}{name}-{_id}'

    return url


class User:
    def __init__(self):
        self.grades = []

    def grade_or_update_recipe(self, name):
        grade = int(input(f'Please grade the recipe {name}, 1-5:\n'
                          '> '))
        grade_dict = {'name': name,
                      'grade:': grade,
                      'last_cooked': datetime.datetime.now()}
        self.grades.append(grade_dict)

    def get_labels(self):
        path = pathlib.Path(__file__).parent.resolve()
        path = os.path.join(path, 'app/exp/labels')
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

        return mylist

    def get_recipes(self, labels, c):
        ingredients = [label for label in labels if labels.index(label) in c]
        recipes = []

        with open('../../datasets/RAW_recipes.csv', 'r', encoding='utf-8') as infile:
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
                        recipe['minutes'] = row[5]
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

        sorted_recipes = []
        for recipe in recipes:
            # Checking if the recipe contains all the chosen categories made by the user
            if all(item in recipe['category'] for item in categories):
                sorted_recipes.append(recipe)
        return sorted_recipes

    def show_url(self, sorted_recipes):
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

        choice = int(input('Which recipe would you like to be directed to? '))

        convert_to_url(sorted_recipes[choice - 1]['name'], sorted_recipes[choice - 1]['id'])

        choice2 = input(f'Did you cook {sorted_recipes[choice - 1]["name"]}? y/n\n'
                        '> ')
        if choice2 == 'y':
            for grade in self.grades:
                if grade['name'] == sorted_recipes[choice - 1]["name"]:
                    grade['last_cooked'] = datetime.datetime.now()
                else:
                    self.grade_or_update_recipe(sorted_recipes[choice - 1]["name"])
        else:
            choice3 = input('Do you want to see the recipes again? y/n\n'
                            '> ')
            if choice3:
                pass


def main():
    # Terminal commands:
    # os.system("python detect.py --source 1 --weights ./trained_model/best.pt --save-txt")
    # python detect.py --source 1 --weights ./train_models/model_85_epochs.pt --save-txt

    user = User()

    labels = ['wrong', 'asparagus', 'banana', 'beans', 'bell pepper', 'broccoli', 'carrot', 'cheese', 'chicken',
              'chili', 'cucumber', 'egg', 'eggplant', 'garlic', 'ginger', 'lemon', 'lentils', 'minced_meat',
              'not_food', 'olive_label', 'olives', 'onion', 'potato', 'red_onion', 'rhubarb', 'rice', 'salmon',
              'spaghetti', 'spinach', 'sun-dried tomatoes', 'sun-dried_tomatoes', 'sun-dried_tomatoes_label',
              'tomato sauce', 'tomato_sauce', 'tomato', 'whipping_cream']

    c = user.get_labels()
    recipes, ingredients = user.get_recipes(labels, c)
    sorted_recipes = user.sort_by_category(recipes)
    user.show_url(sorted_recipes)


if __name__ == '__main__':
    main()

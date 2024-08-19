import retrieve
import json
from recipies import Recipe

ingredients = input("Enter main ingredients: ")

meal_type = input("Enter meal type (breakfast, lunch, etc.): ")
while meal_type not in retrieve.MEAL_TYPE:
    print('Not a valid meal time')
    meal_type = input("Enter meal type (breakfast, lunch, etc.): ")

cuisine = input("Enter cuisine type or leave empty: ")
cuisine = None if len(cuisine) == 0 else cuisine

diet = input("Enter type of diet or leave empty: ")
diet = None if len(diet) == 0 else diet

data = None
if cuisine is None and data is None:
    data = retrieve.connect(ingredients, meal_type)
elif cuisine is None:
    data = retrieve.connect(ingredients, meal_type, diet=diet)
elif diet is None:
    data = retrieve.connect(ingredients, meal_type, cuisine=cuisine)
else:
    data = retrieve.connect(ingredients, meal_type, cuisine, diet)

j = json.loads(data)

for recipe in j['hits']:
    r = Recipe(recipe['recipe'])
    print(r)
    print('; '.join(r.get_ingredients()))
import retrieve
import json
from recipies import Recipe

j = dict()
with open('data.json', 'r') as infile:
    j = json.load(infile)

for recipe in j['hits']:
    r = Recipe(recipe['recipe'])
    print(r)
    print('; '.join(r.get_ingredients()))
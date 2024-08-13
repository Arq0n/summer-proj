import requests
import json
import os
from dotenv import load_dotenv

CUISINES = ['american', 'asian', 'british', 'caribbean', 'central europe', 'chinese',
            'eastern europe', 'french', 'greek', 'indian', 'italian', 'japanese', 'korean',
              'kosher', 'mediterranean', 'mexican', 'middle eastern', 'nordic', 
              'south american','south east asian', 'world']
MEAL_TYPE = ['breakfast', 'brunch', 'lunch' , 'dinner', 'snack', 'teatime']
DIET_LABELS = ['balanced', 'high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium']

load_dotenv()
EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')

def connect(text, cuisine, meal_type, diet, allergies=None):
    if cuisine not in CUISINES:
        raise ValueError('Not a valid cuisine type')
    if meal_type not in MEAL_TYPE:
        raise ValueError('Not a valid meal time')
    if diet not in DIET_LABELS:
        raise ValueError('Not a valid diet label')
    
    url = 'https://api.edamam.com/api/recipes/v2'
    params = {
        'type': 'any',
        'app_id': '04537fa2',
        'app_key': EDAMAM_API_KEY,
        'q': text,
        'cuisineType': cuisine,
        'mealType': meal_type,
        'diet': diet}
    headers = {'Accept-Language' : 'en'}

    response = requests.get(url, params=params, headers=headers)
    data = response.content.decode(encoding='utf-8')
    j = json.loads(data)
    with open('data.json', 'w') as outfile:
        json.dump(j, outfile)

if __name__ == "__main__":
    connect('chicken', 'american', 'dinner', 'balanced')
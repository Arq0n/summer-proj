import requests
import json
import os
from dotenv import load_dotenv

CUISINES = ['american', 'asian', 'british', 'caribbean', 'central europe', 'chinese',
            'eastern europe', 'french', 'greek', 'indian', 'italian', 'japanese', 'korean',
              'kosher', 'mediterranean', 'mexican', 'middle eastern', 'nordic', 
              'south american','south east asian', 'world']
DIET_LABELS = ['balanced', 'high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium']
MEAL_TYPE = ['breakfast', 'brunch', 'lunch' , 'dinner', 'snack', 'teatime']

load_dotenv()
EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')

def connect(text: str, meal_type: str, cuisine: str = 'world', diet: str = 'balanced', allergies: str = None) -> str:
    """
    Method to connect to edamam api to access meal information
    Returns the string recieved from the api
    """
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
    return response.content.decode(encoding='utf-8')
    

if __name__ == "__main__":
    data = connect('chicken', 'american', 'dinner', 'balanced')
    j = json.loads(data)
    with open('data.json', 'w') as outfile:
        json.dump(j, outfile)
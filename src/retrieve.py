import requests


def connect(text, cuisine, meal_type, diet, allergies=None):
    url = 'https://api.edamam.com/api/recipes/v2'
    params = {
        'type': 'any',
        'app_id': '04537fa2',
        'app_key': '229288441e21574ad74579f88e34b687',
        'q': text,
        'cuisineType': cuisine,
        'mealType': meal_type,
        'diet': diet}
    headers = {
            'Accept-Language' : 'en'}

    response = requests.get(url, params=params, headers=headers)
    print(response.content)

connect('chicken', 'american', 'dinner', 'balanced')
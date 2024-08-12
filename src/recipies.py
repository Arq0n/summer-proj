class Recipe:
    def __init__(self, json_data):
        self._name = json_data['label']
        self._health_labels = json_data['healthLabels']
        self._cautions = json_data['cautions']
        self._ingredients = json_data['ingredientLines']
        self._cuisine = json_data['cuisineType']
        self._meal_type = json_data['mealType']

    def __str__(self):
        return ' '.join(self._cuisine) + ' cuisine: ' + self._name + ' for ' + \
            ' '.join(self._meal_type)
    
    def get_health_labels(self) -> list[str]:
        return self._health_labels
    
    def get_cautions(self) -> list[str]:
        return self._cautions
    
    def get_ingredients(self) -> list[str]:
        return self._ingredients
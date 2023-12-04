spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    all_foods = [food["name"] for food in spicy_foods]
    return all_foods

def get_spiciest_foods(spicy_foods):
    hot_foods = [food for food in spicy_foods if food["heat_level"]>5]
    return hot_foods

def print_spicy_foods(spicy_foods):
    heat_emojis = "🌶"
    emoji_foods = [
        f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis*(food['heat_level'])}"
        for food in spicy_foods
    ]
    for emoji_food in emoji_foods:
        print(emoji_food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    heat_emojis = "🌶"
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis*(food['heat_level'])}")



def get_average_heat_level(spicy_foods):
    heat_level_total=sum(food['heat_level'] for food in spicy_foods)
    num_of_foods=len(spicy_foods)

    average_heat_level = heat_level_total/num_of_foods
    return average_heat_level



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
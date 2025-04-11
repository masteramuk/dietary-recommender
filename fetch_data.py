# This script fetches data from various APIs and inserts it into a SQLite database.
# It uses the Spoonacular API for detailed recipe information and TheMealDB for a broader range of recipes.
# The script is designed to be run as a standalone program, but can also be imported as a module.
# It requires the requests library for HTTP requests and sqlite3 for database operations.
# The script includes functions to fetch data from the APIs, insert food items into the database, and search for Malaysian recipes.
# It also includes error handling for network requests and database operations.
# The script is structured to allow for easy expansion and modification, making it a flexible tool for managing food data.
# dietary-recommender/src/db/fetch_data.py

import requests
import sqlite3
import json
import os

def fetch_data_from_url(url, params=None, headers=None):
    """Generic function to fetch data from a URL."""
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def insert_food_items(db_file, food_data):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        for item in food_data:
            name = item.get('name', 'Unknown')
            region = item.get('region', 'Unknown')
            food_type = item.get('food_type', 'Unknown')
            preparation_method = item.get('preparation_method', 'Unknown')
            dietary_tags = item.get('dietary_tags', 'Unknown')
            calories = item.get('calories', 0)
            protein = item.get('protein', 0)
            carbohydrates = item.get('carbohydrates', 0)
            fat = item.get('fat', 0)
            seasonal = item.get('seasonal', 'Unknown')
            recipe_variations = item.get('recipe_variations', 'Unknown')

            cursor.execute('''
                INSERT INTO food_items (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations
            ))
        conn.commit()

def search_malaysian_recipes(api_key=None, query="Malaysian food", num_results=100):
    """Fetches Malaysian recipes using a recipe API (example: Spoonacular)."""
    if not api_key:
        print("Spoonacular API key is required for this function.")
        return None

    base_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        'apiKey': '7a33293249f644168b1f1d450c7f9887',
        'query': query,
        'cuisine': 'Malaysian',  # Broaden to Asian initially
        'diet': '',
        'number': num_results,
        'instructionsRequired': True,
        'fillIngredients': False,
    }
    headers = {'Content-Type': 'application/json'}
    data = fetch_data_from_url(base_url, params=params, headers=headers)

    if data and 'results' in data:
        malaysian_recipes = [recipe for recipe in data['results'] if 'malaysian' in recipe['title'].lower() or any('malaysian' in ingredient['name'].lower() for ingredient in recipe.get('ingredients', []))]
        print(f"Found {len(malaysian_recipes)} Malaysian recipes from Spoonacular.")
        return malaysian_recipes
    else:
        print("Could not retrieve Malaysian recipes from Spoonacular.")
        return None

def fetch_malaysian_recipes_themealdb():
    """Fetches Malaysian recipes from TheMealDB API."""
    base_url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=Malaysian"
    #params = {'a': 'Malaysian'}
    data = fetch_data_from_url(base_url) #, params=params)
    print('data: ') 
    print(data)
    if data and 'meals' in data and data['meals'] is not None:
        print(f"Found {len(data['meals'])} Malaysian recipes from TheMealDB.")
        return data['meals']
    else:
        print("Could not retrieve Malaysian recipes from TheMealDB.")
        return None

if __name__ == "__main__":
    db_file = 'food_database.db'

    # --- Using Spoonacular API (Requires API Key) ---
    spoonacular_api_key = "7a33293249f644168b1f1d450c7f9887"  # Replace with your actual API key
    if spoonacular_api_key:
        malaysian_recipes_spoonacular = search_malaysian_recipes(api_key=spoonacular_api_key)
        if malaysian_recipes_spoonacular:
            insert_food_items(db_file, malaysian_recipes_spoonacular)
            print("\n--- Malaysian Recipes from Spoonacular inserted into database ---")

    # --- Using TheMealDB API (No API Key Required) ---
    malaysian_recipes_themealdb = fetch_malaysian_recipes_themealdb()
    if malaysian_recipes_themealdb:
        insert_food_items(db_file, malaysian_recipes_themealdb)
        print("\n--- Malaysian Recipes from TheMealDB inserted into database ---")
# This script updates the food items in the SQLite database with new data.

import sqlite3
import json

def update_food_items(db_file, food_data):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        for item in food_data:
            cursor.execute('''
                INSERT INTO food_items (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.get('name', ''),
                item.get('region', 'Unknown'),
                item.get('food_type', 'Unknown'),
                item.get('preparation_method', 'Unknown'),
                item.get('dietary_tags', 'Unknown'),
                item.get('calories', 0),
                item.get('protein', 0),
                item.get('carbohydrates', 0),
                item.get('fat', 0),
                item.get('seasonal', 'Unknown'),
                item.get('recipe_variations', 'Unknown')
            ))
        conn.commit()

if __name__ == "__main__":
    db_file = '../../food_database.db'
    food_data = json.loads(input("Enter food data as JSON: "))
    update_food_items(db_file, food_data)
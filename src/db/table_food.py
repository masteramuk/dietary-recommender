# This script creates the necessary tables for a dietary recommender system using SQLite.
import sqlite3

# This script creates the necessary tables for a dietary recommender system using SQLite.
def create_tables(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create user_profiles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL,
            activity_level TEXT,
            health_conditions TEXT,
            meal_timing_preferences TEXT,
            custom_goals TEXT
        )
    ''')

    # Create food_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            region TEXT,
            food_type TEXT,
            preparation_method TEXT,
            dietary_tags TEXT,
            calories INTEGER,
            protein INTEGER,
            carbohydrates INTEGER,
            fat INTEGER,
            seasonal TEXT,
            recipe_variations TEXT
        )
    ''')

    # Create nutritional_needs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nutritional_needs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            caloric_needs INTEGER,
            protein_needs INTEGER,
            carbohydrates_needs INTEGER,
            fat_needs INTEGER,
            custom_goals TEXT,
            FOREIGN KEY(user_id) REFERENCES user_profiles(id)
        )
    ''')

    # Create recommendations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            food_item_id INTEGER,
            recommendation_date TEXT,
            feedback TEXT,
            FOREIGN KEY(user_id) REFERENCES user_profiles(id),
            FOREIGN KEY(food_item_id) REFERENCES food_items(id)
        )
    ''')

    # Create user_feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            recommendation_id INTEGER,
            feedback TEXT,
            feedback_date TEXT,
            FOREIGN KEY(user_id) REFERENCES user_profiles(id),
            FOREIGN KEY(recommendation_id) REFERENCES recommendations(id)
        )
    ''')

    # Create user_contributions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_contributions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            food_item_id INTEGER,
            recipe_name TEXT,
            recipe_details TEXT,
            nutritional_info TEXT,
            contribution_date TEXT,
            FOREIGN KEY(user_id) REFERENCES user_profiles(id),
            FOREIGN KEY(food_item_id) REFERENCES food_items(id)
        )
    ''')

    conn.commit()
    conn.close()

create_tables('food_database.db')
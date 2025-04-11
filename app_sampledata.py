# Sample data for the dietary recommender system
# Sample data for the dietary recommender system
import sqlite3
from contextlib import closing

# Function to insert a user profile
def insert_user_profile(db_file, age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO user_profiles (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals))
            conn.commit()

# Function to insert a food item
def insert_food_item(db_file, name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO food_items (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations))
            conn.commit()

# Function to insert nutritional needs
def insert_nutritional_needs(db_file, user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO nutritional_needs (user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals))
            conn.commit()

# Function to insert a recommendation
def insert_recommendation(db_file, user_id, food_item_id, recommendation_date, feedback):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO recommendations (user_id, food_item_id, recommendation_date, feedback)
                VALUES (?, ?, ?, ?)
            ''', (user_id, food_item_id, recommendation_date, feedback))
            conn.commit()

# Function to insert user feedback
def insert_user_feedback(db_file, user_id, recommendation_id, feedback, feedback_date):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO user_feedback (user_id, recommendation_id, feedback, feedback_date)
                VALUES (?, ?, ?, ?)
            ''', (user_id, recommendation_id, feedback, feedback_date))
            conn.commit()

# Function to insert user contribution
def insert_user_contribution(db_file, user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO user_contributions (user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date))
            conn.commit()

# Insert sample data
if __name__ == "__main__":
    db_file = 'food_database.db'

    # Insert sample user profile
    insert_user_profile(db_file, 25, 'male', 70, 175, 'moderate', 'none', 'standard', 'reduce cholesterol')

    # Insert sample food items
    insert_food_item(db_file, 'Nasi Lemak', 'Malaysia', 'breakfast', 'cooked', 'halal', 600, 10, 100, 20, 'year-round', 'low-carb version available')
    insert_food_item(db_file, 'Chapati', 'India', 'lunch', 'grilled', 'vegetarian', 300, 5, 50, 10, 'year-round', 'whole wheat version available')
    insert_food_item(db_file, 'Char Kway Teow', 'Malaysia', 'lunch', 'stir-fried', 'halal', 500, 15, 80, 10, 'year-round', 'vegan version available')

    # Insert sample nutritional needs
    insert_nutritional_needs(db_file, 1, 2000, 100, 250, 70, 'reduce cholesterol')

    # Insert sample recommendation
    insert_recommendation(db_file, 1, 1, '2023-10-01', 'Great recommendation!')

    # Insert sample user feedback
    insert_user_feedback(db_file, 1, 1, 'Loved the meal!', '2023-10-02')

    # Insert sample user contribution
    insert_user_contribution(db_file, 1, 1, 'Nasi Lemak', 'A traditional Malaysian breakfast dish.', 'Calories: 600, Protein: 10g, Carbohydrates: 100g, Fat: 20g', '2023-10-03')
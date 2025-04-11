# This script creates a SQLite database with two tables: user_profiles and food_items.
import sqlite3

# This script creates the necessary tables for a dietary recommender system using SQLite.
def query_user_profiles(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_profiles')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def query_food_items(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM food_items')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def query_nutritional_needs(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM nutritional_needs')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def query_recommendations(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM recommendations')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def query_user_feedback(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_feedback')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def query_user_contributions(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_contributions')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

    
# Query and print data
query_user_profiles('food_database.db')
query_food_items('food_database.db')
query_nutritional_needs('food_database.db')
query_recommendations('food_database.db')
query_user_feedback('food_database.db')
query_user_contributions('food_database.db')
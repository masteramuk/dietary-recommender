#we are going to create a database for the food recommender system
# This script creates a SQLite database for the food recommender system
# Import necessary libraries
import os
import sqlite3

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    conn.close()

create_database('food_database.db')
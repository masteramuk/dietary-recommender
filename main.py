# Entry point for simulation
import pandas as pd
import sqlite3

def main():
    print("✅ Dietary Recommender System POC is working!")
    df = pd.DataFrame({'Food': ['Nasi Lemak', 'Chapati'], 'Calories': [600, 300]})
    print(df)
    # If this runs without any errors, then sqlite3 is already available.
    print("sqlite3 imported successfully!")

if __name__ == "__main__":
    main()
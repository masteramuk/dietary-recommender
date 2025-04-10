# Entry point for simulation
import pandas as pd

def main():
    print("✅ Dietary Recommender System POC is working!")
    df = pd.DataFrame({'Food': ['Nasi Lemak', 'Chapati'], 'Calories': [600, 300]})
    print(df)

if __name__ == "__main__":
    main()

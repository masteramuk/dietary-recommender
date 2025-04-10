# ✅ Step-by-Step Environment Setup (Local + Simulatable)

## 1. 🐍 Install Python (if not yet)
Make sure you have **Python 3.9 or later** installed. You can check by running:

\`\`\`bash
python --version
\`\`\`

If not installed:  
- Download from: [Download Python](https://www.python.org/downloads/) 

Make sure to check **“Add Python to PATH”** during installation.

**Additional Note**: Verify the installation by running `python --version` and `pip --version` to ensure both Python and pip are correctly installed and accessible from the command line.

---

## 2. 📁 Project Folder Structure

Create your main folder, for example:

\`\`\`
dietary-recommender/
│
├── data/                  # Food CSV files or datasets
├── src/                   # Source code
│   ├── __init__.py
│   ├── user_profile.py    # Handles user data input & processing
│   ├── food_db.py         # Loads & filters food data
│   ├── recommender.py     # Recommendation engine logic
├── main.py                # Entry point for simulation
├── requirements.txt       # Python dependencies
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── README.md              # Instructions for others to simulate
\`\`\`

**Additional Note**: Consider adding a `tests/` directory for unit tests and a `docs/` directory for documentation.

---

## 3. 💻 Setup Virtual Environment in VS Code

In your terminal inside VS Code:

\`\`\`bash
cd dietary-recommender
python -m venv venv
\`\`\`

Activate it:

- On **Windows**:
  \`\`\`bash
  .\venv\Scripts\activate
  \`\`\`

- On **macOS/Linux**:
  \`\`\`bash
  source venv/bin/activate
  \`\`\`

Then you’ll see `(venv)` in your terminal prompt. That’s good.

**Additional Note**: Ensure you deactivate the virtual environment when you're done working on the project by running `deactivate` in the terminal.

---

## 4. 📦 Install Core Dependencies

Create a file called `requirements.txt` and start with this:

\`\`\`txt
pandas
numpy
streamlit
scikit-learn
matplotlib
\`\`\`

Install them:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

You can add more later (e.g., `scikit-learn`, `matplotlib`).

**Additional Note**: Consider using a more comprehensive list of dependencies initially to avoid frequent updates to `requirements.txt`.

---

## 5. 🧪 Test Your Setup

Create a simple test file to ensure it's working:

**`main.py`**:

\`\`\`python
import pandas as pd

def main():
    print("✅ Dietary Recommender System POC is working!")
    df = pd.DataFrame({'Food': ['Nasi Lemak', 'Chapati'], 'Calories': [600, 300]})
    print(df)

if __name__ == "__main__":
    main()
\`\`\`

Run it:

\`\`\`bash
python main.py
\`\`\`

**Additional Note**: Ensure that the output matches your expectations. This step is crucial for verifying that your environment is correctly set up.

---

## 6. 📄 VS Code Setup Tips

- Install the **Python extension** (if not yet).
- Set your interpreter to the virtual environment:  
  Open Command Palette → “Python: Select Interpreter” → choose your `venv`.

**Additional Note**: Ensure that the Python extension is correctly configured to use the virtual environment interpreter. You can verify this by checking the Python interpreter path in the bottom-right corner of the VS Code window.

---

## Additional Recommendations

- **Version Control**: Initialize a Git repository in your project directory to track changes and collaborate with others:

  \`\`\`bash
  git init
  git add .
  git commit -m "Initial commit"
  \`\`\`

- **Environment Configuration**: Consider using a `.env` file to manage environment variables, especially if you plan to expand your project with more complex configurations.

- **Documentation**: Start documenting your project early. Update the `README.md` file with detailed instructions on how to set up and run the project, including any dependencies and configuration steps.

- **Testing**: Write unit tests for your core functionalities to ensure they work as expected. This will help catch issues early in the development process.

# 📝 Step-by-Step Guide to Set Up and Commit to GitHub

## Prerequisites
- **Git**: Ensure you have Git installed on your system. You can check by running `git --version` in your terminal. If not installed, download it from [Git's official website](https://git-scm.com/).
- **GitHub Account**: Make sure you have a GitHub account. If not, sign up at [GitHub](https://github.com/).

## Step 1: Create a New GitHub Repository
1. **Log in to GitHub**: Go to [GitHub](https://github.com/) and log in to your account.
2. **Create a New Repository**:
   - Click on the "+" icon in the upper right corner and select "New repository".
   - Enter a repository name (e.g., `dietary-recommender`).
   - Add a description (optional).
   - Choose whether the repository should be public or private.
   - **Do not initialize the repository with a README file**. We will add this from your local files.
   - Click "Create repository".

## Step 2: Initialize Your Local Project with Git
1. **Open a Terminal or Command Prompt**:
   - Navigate to your project directory where all your files are located. For example:
     ```bash
     cd path/to/your/dietary-recommender
     ```

2. **Initialize a Git Repository**:
   ```bash
   git init

You're right, I apologize for the oversight. Let's ensure that all parts of the guide are properly formatted in Markdown. Here’s the revised and fully formatted guide:

```markdown
# 📝 Step-by-Step Guide to Set Up and Commit to GitHub

## Prerequisites
- **Git**: Ensure you have Git installed on your system. You can check by running `git --version` in your terminal. If not installed, download it from [Git's official website](https://git-scm.com/).
- **GitHub Account**: Make sure you have a GitHub account. If not, sign up at [GitHub](https://github.com/).

## Step 1: Create a New GitHub Repository
1. **Log in to GitHub**: Go to [GitHub](https://github.com/) and log in to your account.
2. **Create a New Repository**:
   - Click on the "+" icon in the upper right corner and select "New repository".
   - Enter a repository name (e.g., `dietary-recommender`).
   - Add a description (optional).
   - Choose whether the repository should be public or private.
   - **Do not initialize the repository with a README file**. We will add this from your local files.
   - Click "Create repository".

## Step 2: Initialize Your Local Project with Git
1. **Open a Terminal or Command Prompt**:
   - Navigate to your project directory where all your files are located. For example:
     ```bash
     cd path/to/your/dietary-recommender
     ```

2. **Initialize a Git Repository**:
   ```bash
   git init
   ```

3. **Add Your Files to the Repository**:
   ```bash
   git add .
   ```

4. **Commit Your Changes**:
   ```bash
   git commit -m "Initial commit"
   ```

## Step 3: Link Your Local Repository to GitHub
1. **Get the Remote Repository URL**:
   - Go to your newly created GitHub repository.
   - Click on the "Code" button and copy the URL provided. It should look something like this:
     ```
     https://github.com/yourusername/dietary-recommender.git
     ```

2. **Add the Remote Repository URL to Your Local Repository**:
   ```bash
   git remote add origin https://github.com/yourusername/dietary-recommender.git
   ```

3. **Push Your Changes to GitHub**:
   ```bash
   git push -u origin main
   ```

## Step 4: Handle Merge Conflicts
If you encounter a merge conflict when pushing your changes, follow these steps:

1. **Fetch the Latest Changes from the Remote Repository**:
   ```bash
   git fetch origin
   ```

2. **Check the Status of Your Local Branch**:
   ```bash
   git status
   ```

3. **Pull the Latest Changes**:
   ```bash
   git pull origin main
   ```

4. **Resolve Any Merge Conflicts**:
   - If there are any merge conflicts, Git will prompt you to resolve them. Open the conflicting files and make the necessary changes.
   - After resolving the conflicts, add the files to the staging area:
     ```bash
     git add .
     ```

5. **Commit the Merge**:
   ```bash
   git commit -m "Merge changes from remote"
   ```

6. **Push Your Changes to the Remote Repository**:
   ```bash
   git push -u origin main
   ```

## Step 5: Verify Your Commit
1. **Check Your GitHub Repository**:
   - Go to your GitHub repository page.
   - You should see your files and the initial commit.

## Additional Tips
- **Check Status**: You can check the status of your Git repository at any time by running:
  ```bash
  git status
  ```

- **View Logs**: To view the commit history, you can run:
  ```bash
  git log
  ```

- **Branches**: If you need to work on a new feature or fix, you can create a new branch:
  ```bash
  git checkout -b new-feature
  ```

- **Pull Changes**: If you need to pull the latest changes from the remote repository:
  ```bash
  git pull origin main
  ```

- **Resolve Conflicts**: If there are any merge conflicts, resolve them manually, then add and commit the changes:
  ```bash
  git add .
  git commit -m "Resolve conflicts"
  ```

By following these steps, you should be able to set up your local project and commit it to a new GitHub repository. If you encounter any issues or have further questions, feel free to ask!
```

# 📝 Step-by-Step Guide to Set Up SQLite Database for Dietary Recommender System

## Prerequisites
- **Python**: Ensure you have Python installed on your system.
- **SQLite3**: SQLite3 is included with Python, so no additional installation is required.
- **Pandas**: Install pandas for data manipulation. You can install it using pip:
  ```bash
  pip install pandas
  ```

## Step 1: Set Up the Environment

1. **Install Required Libraries**:
   - Open a terminal or command prompt and run:
     ```bash
     pip install pandas
     ```

## Step 2: Define Features and Functions

List the features and functions you wish to build:
1. **User Profile Intake**:
   - Activity Level
   - Health Conditions
   - Meal Timing Preferences
2. **Nutritional Needs Calculator**:
   - Customizable Goals
   - Microbiome Considerations
3. **Cuisine-Specific Food Database**:
   - Seasonal Ingredients
   - Recipe Variations
   - User Contributions
4. **Recommendation Engine**:
   - Feedback Loop
   - Meal Planning
   - Nutritional Education

## Step 3: Form the Table Structures

Based on the features, define the necessary tables:

1. **User Profiles Table**:
   - `id`: Unique identifier for the user.
   - `age`: User's age.
   - `gender`: User's gender.
   - `weight`: User's weight.
   - `height`: User's height.
   - `activity_level`: User's activity level.
   - `health_conditions`: User's existing health conditions.
   - `meal_timing_preferences`: User's meal timing preferences.
   - `custom_goals`: User's specific health goals.

2. **Food Items Table**:
   - `id`: Unique identifier for the food item.
   - `name`: Name of the food item.
   - `region`: Region or country of origin.
   - `food_type`: Type of food.
   - `preparation_method`: Method of preparation.
   - `dietary_tags`: Dietary tags.
   - `calories`: Caloric content.
   - `protein`: Protein content.
   - `carbohydrates`: Carbohydrate content.
   - `fat`: Fat content.
   - `seasonal`: Seasonal availability.
   - `recipe_variations`: Variations of the recipe.

3. **Nutritional Needs Table**:
   - `id`: Unique identifier for the nutritional needs entry.
   - `user_id`: Foreign key linking to the user_profiles table.
   - `caloric_needs`: Daily caloric needs.
   - `protein_needs`: Daily protein needs.
   - `carbohydrates_needs`: Daily carbohydrate needs.
   - `fat_needs`: Daily fat needs.
   - `custom_goals`: Custom nutritional goals.

## Step 4: Create the Database and Tables

1. **Create the Database File**:
   ```python
   import sqlite3

   def create_database(db_file):
       conn = sqlite3.connect(db_file)
       conn.close()

   create_database('food_database.db')
   ```

2. **Create the Tables**:
   ```python
   def create_tables(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

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

   ```

## Step 5: Insert Sample Data

1. **Insert Sample Data into `user_profiles` Table**
   ```python
   def insert_user_profile(db_file, age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals):
       conn = sqlite3.connect(db_file)
       cursor = conn.cursor()

       cursor.execute('''
           INSERT INTO user_profiles (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''', (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals))

       conn.commit()
       conn.close()

   insert_user_profile('food_database.db', 25, 'male', 70, 175, 'moderate', 'none', 'standard', 'reduce cholesterol')
   ```

2. **Insert Sample Data into Tables**
    **Insert Sample Data into `food_items`**
   ```python
   def insert_user_profile(db_file, age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO user_profiles (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (age, gender, weight, height, activity_level, health_conditions, meal_timing_preferences, custom_goals))

    conn.commit()
    conn.close()

    insert_user_profile('food_database.db', 25, 'male', 70, 175, 'moderate', 'none', 'standard', 'reduce cholesterol')

   ```
   **Insert Sample Data into `food_items`**
   ```python
   def insert_food_item(db_file, name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO food_items (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, region, food_type, preparation_method, dietary_tags, calories, protein, carbohydrates, fat, seasonal, recipe_variations))

    conn.commit()
    conn.close()

    insert_food_item('food_database.db', 'Nasi Lemak', 'Malaysia', 'breakfast', 'cooked', 'halal', 600, 10, 100, 20, 'year-round', 'low-carb version available')
    insert_food_item('food_database.db', 'Chapati', 'India', 'lunch', 'grilled', 'vegetarian', 300, 5, 50, 10, 'year-round', 'whole wheat version available')
    insert_food_item('food_database.db', 'Char Kway Teow', 'Malaysia', 'lunch', 'stir-fried', 'halal', 500, 15, 80, 10, 'year-round', 'vegan version available')
    ```

    **Insert Sample Data into `nutritional_needs`**
    ```python
    def insert_nutritional_needs(db_file, user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO nutritional_needs (user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, caloric_needs, protein_needs, carbohydrates_needs, fat_needs, custom_goals))

        conn.commit()
        conn.close()

    insert_nutritional_needs('food_database.db', 1, 2000, 100, 250, 70, 'reduce cholesterol')
    ```

    **Insert Sample Data into `recommendations`**
    ```python
    def insert_recommendation(db_file, user_id, food_item_id, recommendation_date, feedback):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO recommendations (user_id, food_item_id, recommendation_date, feedback)
            VALUES (?, ?, ?, ?)
        ''', (user_id, food_item_id, recommendation_date, feedback))

        conn.commit()
        conn.close()

    insert_recommendation('food_database.db', 1, 1, '2023-10-01', 'Great recommendation!')
    ```
    **Insert Sample Data into `user_feedback`**
    ```python
    def insert_user_feedback(db_file, user_id, recommendation_id, feedback, feedback_date):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO user_feedback (user_id, recommendation_id, feedback, feedback_date)
            VALUES (?, ?, ?, ?)
        ''', (user_id, recommendation_id, feedback, feedback_date))

        conn.commit()
        conn.close()

    insert_user_feedback('food_database.db', 1, 1, 'Loved the meal!', '2023-10-02')
    ```

    **Insert Sample Data into `user_contributions`**
    ```python
    def insert_user_contribution(db_file, user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO user_contributions (user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, food_item_id, recipe_name, recipe_details, nutritional_info, contribution_date))

        conn.commit()
        conn.close()

    insert_user_contribution('food_database.db', 1, 1, 'Nasi Lemak', 'A traditional Malaysian breakfast dish.', 'Calories: 600, Protein: 10g, Carbohydrates: 100g, Fat: 20g', '2023-10-03')
    ```

## Step 6: Test the Sample Data

1. **Query the `user_profiles` Table**:
   ```python
   def query_user_profiles(db_file):
       conn = sqlite3.connect(db_file)
       cursor = conn.cursor()

       cursor.execute('SELECT * FROM user_profiles')
       rows = cursor.fetchall()

       for row in rows:
           print(row)

       conn.close()

   query_user_profiles('food_database.db')
   ```

2. **Test the data**
    **Query the `food_items` Table**:
   ```python
   def query_food_items(db_file):
       conn = sqlite3.connect(db_file)
       cursor = conn.cursor()

       cursor.execute('SELECT * FROM food_items')
       rows = cursor.fetchall()

       for row in rows:
           print(row)

       conn.close()

   query_food_items('food_database.db')
   ```
   
   **Query the `nutritional_needs`**
    ```python
    def query_nutritional_needs(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM nutritional_needs')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    query_nutritional_needs('food_database.db')
    ```

    **Query the `recommendations`**
    ```python
    def query_recommendations(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM recommendations')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    query_recommendations('food_database.db')
    ```
    **Query the `user_feedback`**
    ```python
    def query_user_feedback(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM user_feedback')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    query_user_feedback('food_database.db')
    ```
    **Query the `user_contributions`**
    ```python
    def query_user_contributions(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM user_contributions')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    query_user_contributions('food_database.db')
    ```
## Summary

By following these steps, you will have set up an SQLite database with the necessary tables and inserted sample data to support your dietary recommendation system. This guide provides a clear and structured approach to setting up the database environment.

```

This guide is now fully formatted in Markdown, ensuring consistency and readability. You can copy this content and paste it into your `README.md` file.
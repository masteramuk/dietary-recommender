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

This guide is now fully formatted in Markdown, ensuring consistency and readability. You can copy this content and paste it into your `README.md` file.
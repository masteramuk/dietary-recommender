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


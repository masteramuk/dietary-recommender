import sys

# Remove previous paths (if any)
try:
    sys.path.remove('/path/to/previous/site-packages')
except ValueError:
    pass  # Path not found, do nothing

# Add the correct path to the site-packages directory
sys.path.append('/Users/masteramuk/.pyenv/versions/3.11.11/lib/python3.11/site-packages')

# Now you can import your packages
import torch
import transformers
import faiss
import langchain
import streamlit
import pandas
import sklearn

print("Python version:", sys.version)
print("Torch version:", torch.__version__)
print("Transformers version:", transformers.__version__)
print("Faiss version:", faiss.__version__)
print("Langchain version:", langchain.__version__)
print("Streamlit version:", streamlit.__version__)
print("Pandas version:", pandas.__version__)
print("Scikit-learn version:", scikit-learn.__version__)
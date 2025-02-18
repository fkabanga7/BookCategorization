#!/bin/bash

# Install dependencies listed in requirements.txt
pip install -r requirements.txt

# Install the correct version of python if needed (but confirm the environment version first)
#brew install python@3.10  # You can skip this if your environment already has the correct version of Python

# Download spaCy model
python -m spacy download en_core_web_sm

# Ensure correct version of pip and setuptools
pip install --upgrade pip
pip install --upgrade setuptools

# Ensure all dependencies are correct
pip install --upgrade numpy scikit-learn pandas streamlit

#!/bin/bash

# Install dependencies listed in requirements.txt
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm


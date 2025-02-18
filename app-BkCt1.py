import streamlit as st
import pandas as pd
import spacy
from sklearn.cluster import KMeans

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Load the dataset
data = pd.read_excel('AllITBooks_DataSet.xlsx')  # Adjust the path to your .xlsx file

# Preprocess the descriptions (clean the text)
data['Description'] = data['Description'].str.replace(r'\nBook Description:', '', regex=True)
data['Description'] = data['Description'].str.strip()  # Remove any extra spaces

# Vectorize the descriptions using spaCy's word embeddings
def vectorize_text(text):
    doc = nlp(text)  # Process text with spaCy
    return doc.vector  # Return the vector representation of the document

# Apply vectorization to the descriptions
data['Description_Vector'] = data['Description'].apply(vectorize_text)

# Create a 2D array for KMeans (each row is a vector of a book description)
X = list(data['Description_Vector'])

# Apply KMeans clustering (you can change the number of clusters)
num_clusters = 5  # Adjust the number of clusters as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['Category_Predicted'] = kmeans.fit_predict(X)

# Streamlit Title
st.title("IT Book Categorizer")

# User Input - Search for a book by name
book_name = st.text_input("Enter Book Name:")

if book_name:
    # Filter book based on user input (ignore case)
    book = data[data['Book_name'].str.contains(book_name, case=False, na=False)].iloc[0]
    
    st.subheader(f"Book: {book['Book_name']}")
    st.write(f"Predicted Category: {book['Category_Predicted']}")
    st.write(f"Description: {book['Description']}")
    
    # Display most related books (bonus part)
    related_books = data[data['Category_Predicted'] == book['Category_Predicted']].sort_values(by='Description')
    st.write("Related Books:")
    st.write(related_books[['Book_name', 'Description']].head(2))  # Show top 2 related books

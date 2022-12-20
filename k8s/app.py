import streamlit as st
import spacy
from spacy import displacy
from google.cloud import storage

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""

st.header('Streamlit.io on Google Cloud Kubernetes')

user_input = st.text_input('Enter a Phrase for Spacy')

if user_input:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(user_input)
    html = displacy.render(doc, style="ent")
    html = html.replace("\n", " ")
    st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)

# Initialize a storage client
storage_client = storage.Client()

# Define storage bucket with name
bucket = storage_client.get_bucket('ruicosta-blog-public')

# Get bucket data as blob
blob = bucket.get_blob('test.json')

st.header('Reading from Google Cloud Storage')

# convert to string
json_data = blob.download_as_string()
st.write(json_data)
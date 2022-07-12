# Core Pkgs
import streamlit as st 

# NLP Pkgs
import spacy_streamlit
import spacy

nlp_ner = spacy.load("model-last")

def main():
		"""A NLP app with Spacy-Streamlit"""

		st.title("Enter the SMS recieved and get NLP data")
		message = st.text_area("Enter SMS Text","Type Here ..")
		if st.button("Submit"):
			doc = nlp_ner(message)
			spacy_streamlit.visualize_ner(doc,labels=nlp_ner.get_pipe('ner').labels)
			
 
 
if __name__ == '__main__':
     main()


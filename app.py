import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import WebBaseLoader



st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
def main():
    api_key = st.text_input("🔑 Enter your Groq API Key", type="password")
    

    
    st.title("📊Sentiment Analyzer using Gemma by Google (Groq API)")
    text= st.text_input("write your sentence")

    if st.button("Analyze Sentiment"):
        
        model = ChatGroq(model="gemma2-9b-it", api_key=api_key)


        st.markdown("### Sentiment Analysis Results")
        prompt = (
                "Analyze the sentiment of the following text and respond with "
                "Positive, Negative, or Neutral.\n\n"
                f"Text: {text}"
        )
        response = model.invoke([HumanMessage(content=prompt)])
        sentiment = response.content.strip()
        
        st.write(f"**Text:** {text}")
        st.write(f"**Sentiment:** {sentiment}")
        st.markdown("---")
        if sentiment == "negative":
            st.image()
if __name__ == "__main__":
    main()

from Image2Code.ocr import OCRProcessor
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
import os
from Image2Code.prompt import *

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Function to perform OCR on the uploaded image
def extract_layout_from_image(image_path):
    ocr_processor = OCRProcessor()
    layout = ocr_processor.extract_layout(image_path)
    return layout

# Custom prompt template for HTML generation
CUSTOM_PROMPT_TEMPLATE = PROMPT


# Function to generate HTML code from the layout
def generate_html(layout):
    prompt = PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["layout"])
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=1,
        api_key=GOOGLE_API_KEY
    )
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(layout=layout)
    return output



# Function to handle image processing and HTML generation
def process_image():
    if st.session_state.image:
        layout = extract_layout_from_image(st.session_state.image)
        if layout:
            st.session_state.html = generate_html(layout)
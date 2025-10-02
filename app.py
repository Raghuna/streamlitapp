# import packages
from dotenv import load_dotenv
import openai
import streamlit as st
import google.generativeai as genai
import os
from dotenv import dotenv_values


# load environment variables from .env file
# load_dotenv()

# Initialize OpenAI client
# client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Load the .env file and set the API key from it

config = dotenv_values(".env")
genai.configure(api_key=config.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

@st.cache_data
def get_response(user_prompt, temperature):
    response = model.generate_content(
        user_prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=100
        )
    )
    return response

# Add a text input box for the user prompt
user_prompt = st.text_input("Enter your prompt:", "Explain generative AI in one sentence.")

# Add a slider for temperature
temperature = st.slider(
    "Model temperature:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.01,
    help="Controls randomness: 0 = deterministic, 1 = very creative"
)

with st.spinner("AI is working..."):
    response = get_response(user_prompt, temperature)
    st.write(response.text)

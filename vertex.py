import os
import streamlit as st  
import vertexai
from vertexai.generative_models import GenerativeModel

# TODO: Rename ".env.template" to ".env" and add your project ID to it.
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("my-ai-shoe-starter-c4"), location="us-central1")

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


model = GenerativeModel("gemini-1.5-flash-002")

# Section A: Add in your Vertex AI API call below
response = model.generate_content(
    "What are the neighboring states to " + users_state + "?"
)

# End of Section A


st.write("The neighboring states are:")


# Section B:  Output the results to the user below
st.write(response.text)


# End of Section B

print(response)

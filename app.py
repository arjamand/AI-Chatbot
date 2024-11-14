# import google.generativeai as genai
# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv


# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")


# genai.configure(api_key=api_key)

# def get_text_response(prompt):
#     try :
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(prompt)
    
#         print("AI :",response.text)
    
#     except Exception as e :
#         return f"Error : {e}"
    
# get_text_response(prompt=input("User Input : "))



# V2


import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Authenticate with the Gemini API
genai.configure(api_key=api_key)

def get_text_response(prompt):
    """Generate a text response using the Gemini API."""
    try:
        # Create a generative model instance
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content based on the user prompt
        response = model.generate_content(prompt)
        
        # Return the generated text
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Gemini Text Generation Chatbot")
st.write("Ask me anything, and I'll generate a response!")

# User input field
user_input = st.text_input("You: ")

# Generate and display response when the user clicks the button
if st.button("Ask"):
    if user_input:
        response = get_text_response(user_input)
        st.write(f"QABot: \n{response}")
    else:
        st.write("Please enter a question.")

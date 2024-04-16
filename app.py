from openai import OpenAI
import streamlit as st


# Read the API Key and Setup an OpenAI Client
f = open("C:/Users/saksh/OneDrive/Desktop/GenAI_App/genai_app_1/keys/.openai_api_key.txt")
OPENAI_API_KEY = f.read()


###########################################################
st.title("🐍PyGenius: Python Code Analyzer & Fixer")
st.subheader("Feel free to submit as many code snippets as you'd like for review. We're here to help you improve your code quality!👩‍💻")

###########################################################

client = OpenAI(api_key=OPENAI_API_KEY)

# Take User's input
prompt = st.text_area("Enter your Python Code here....")

# If the button is clicked, generate responses
if st.button("Review Code") == True:

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """You are an intelligent AI assistant and an expert in Python programming language.
                           Given a python code to you, your job is to review and analyze the complete code and give a feedback on potential bugs or errors found in the code along with the suggestions for fixes and areas of improvement. 
                           You generate efficient and accurate bug reports and fixed code snippets."""
                
                           
            },
            {
                "role": "user",
                "content": f"Fix and explain the bugs in the following Python code:{prompt}"
            }
        ],
        temperature=0.5
    )

# Print the response on the Web app
st.write(response.choices[0].message.content)
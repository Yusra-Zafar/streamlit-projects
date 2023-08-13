import openai
import streamlit as st
import pyperclip

def doc_generator(prompt):
    messages = [
        {
            'role': 'system', 'content': f'''
                                        You are a trained documentation generator. You will be given python code. You have to understand the code, identify the main points and generate a documentation. The documentation should not include any links and code. It should be formatted in markdown. 
                                        If any language other than python is given, say: 'Sorry! I only understand Python'. The documentation should only
                                        contain plain text.
                                      '''
        },
        {
            'role': 'user', 'content': f"```({prompt})```"
        }
    ]

    response = openai.ChatCompletion.create(
        messages=messages,
        model='gpt-3.5-turbo',
        temperature=0
    )

    doc = response['choices'][0]['message']['content']
    return doc


def add_bg():
    st.markdown(
        f"""
         <h1 style= 'text-align: center; font-size: 60px;'>Code2Paper</h1>",
         <style>
         .stApp {{             
             background-image: url("https://i.pinimg.com/564x/08/1e/e2/081ee29221e1feb033d887b4268fca8e.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg()

# STREAMLIT CODE

code = st.text_area('Paste your python code', height=90,
                    max_chars=None, key=None, help=None, placeholder='python code')

                    
# Function to display the API key input in the sidebar
def display_api_key_input():
    st.sidebar.header("API Configuration")
    api_key = st.sidebar.text_input(
        "Enter your OpenAI API Key", placeholder='Your key here')
    return api_key


# Display API key input in the sidebar
api_key = display_api_key_input()


# Hitting API for doc

if st.button('Generate documentaton'):
    with st.spinner('OpenAI is working on it'):
        doc = doc_generator(code)

    st.write(doc)

    # Store the generated documentation in the Streamlit cache
    st.session_state.generated_doc = doc


# Add a "Copy" button
if 'generated_doc' in st.session_state and st.button('Copy'):

    # Copy the generated documentation to the clipboard
    pyperclip.copy(st.session_state.generated_doc)
    st.success('Documentation copied to clipboard!')


if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")
else:
    # Set the user-provided API key
    openai.api_key = api_key

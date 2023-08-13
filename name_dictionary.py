import openai
import streamlit as st

# openai.api_key = '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'

def name_dictionary(prompt):
  messages = [
      {
          'role':'system', 'content': f'''
                                        You are a trained model who gives the meaning/translation of urdu or arabic name provided to you in triple backticks. You will give one meaning in urdu and one in english. Also return the sex of the name in the following format:
                                        Name: {prompt} \n
                                        Gender: (male/female/both) \n
                                        Urdu meaning: (urdu) \n
                                        English meaning: (english)
                                        The name given to you will be urdu or arabic name.
                                        Make sure to satisfy the following conditions:
                                        - if any name other than urdu or arabic is given, just return: '**please provide urdu or arabic name**'.
                                        - Don't forget to double check the meaning before telling. The meaning should not be wrong.
                                        - If a name is given which does not exist, then dont make the meaning by yourself. In that
                                          case say, "This name does not exist"
                                        - Be as concise as possible
                                        - If a name belong to both genders, say: 'Both' in gender
                                      '''
      },
      {
          'role': 'user', 'content': f"```({prompt})```"
      }
  ]

  response = openai.ChatCompletion.create(
      messages = messages,
      model = 'gpt-3.5-turbo',
      temperature = 0
  )

  meaning = response['choices'][0]['message']['content']
  return meaning


# CSS for background image

def add_bg_from_url():
    st.markdown(
         f"""
         <h1 style= 'text-align: center;'>NAME DICTIONARY</h1>",
         <style>
         .stApp {{             
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# Function to display the API key input in the sidebar
def display_api_key_input():
    st.sidebar.header("API Configuration")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", placeholder='Your key here')
    return api_key


# Display API key input in the sidebar
api_key = display_api_key_input()

name = st.text_input('Enter name', placeholder='your name here')

if st.button('Find meaning'):
    with st.spinner('OpenAI is processing your name'):
        meaning = name_dictionary(name)
    
    st.write(meaning)

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")
else:
    # Set the user-provided API key
    openai.api_key = api_key





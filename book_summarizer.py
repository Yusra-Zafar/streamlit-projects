import openai
import streamlit as st

# openai.api_key = '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'

def book_summarizer(prompt):
  messages = [
      {
          'role':'system', 'content': f'''
                                        You are a trained model which summarizes the book given to you. 
                                                                                                      
                                        To write a good summary, read and analyze the text of the book carefully while taking notes on important ideas, plot twists, and main characters. Then, find the main idea, keep it brief, write in your own words without judgment, and make sure it flows. 
                                        
                                        The summary should be one-third of the original text.

                                        Follow the five key steps to write the summary:
                                        1. Read the text
                                        2. Break it down into sections
                                        3. Identify the key points in each section
                                        4. Draft the summary before writing
                                        5. Check the summary against the main book
                                        6. Write the final summary

                                        Do not involve critiquing or evaluating the source. You should simply provide an accurate account of the most important information and ideas (without copying any text from the original).
                                        '''
      },

      {
          'role': 'user', 'content': f"(<<<{prompt}>>>)"
      }
  ]

  response = openai.ChatCompletion.create(
      messages = messages,
      model = 'gpt-3.5-turbo',
      temperature = 0.3
  )

  summary = response['choices'][0]['message']['content']
  return summary


# CSS for background image

def add_bg_from_url():
    st.markdown(
         f"""
         <h1 style= 'text-align: center'>Book Summarizer</h1>
         <style>
         .stApp {{             
             background-image: url("https://png.pngtree.com/back_origin_pic/04/14/75/b4c36f5628854af5de1b9a66e3264987.jpg");
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


book_name = st.text_input('Enter the Book Name', placeholder='e.g. The Alchemist')

if st.button('Generate summary'):
    with st.spinner('OpenAI is generating the summary'):
        summary = book_summarizer(book_name)
    
    st.write(summary)


if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")
else:
    # Set the user-provided API key
    openai.api_key = api_key

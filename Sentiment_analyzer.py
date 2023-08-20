import openai
import streamlit as st

# Function to perform sentiment analysis using ChatGPT
def sentiment_analysis_using_chatgpt(prompt):
  messages = [
      {
          'role':'system', 'content': '''You are a trained sentiment analyzer. Return the sentiment and emotions of the given
                                            text. The sentiment should be either 'Positive', 'Negative' or 'Neutral'. Format the response as the following:
                                            (sentiment)\n 
                                            Emotions:
                                           '''
      },
      {
          'role': 'user', 'content': f"```{prompt}```"
      }
  ]

  response = openai.ChatCompletion.create(
      messages = messages,
      model = 'gpt-3.5-turbo',
      temperature = 0
  )

  sentiment = response['choices'][0]['message']['content']
  return sentiment

  

# Function to display the API key input in the sidebar
def display_api_key_input():
    st.sidebar.header("API Configuration")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password", placeholder='Your key here')
    return api_key


# Here comes the streamlit magic!!

st.title("ChatGPT Sentiment Analyzer")

# Display API key input in the sidebar
api_key = display_api_key_input()



model = 'gpt-3.5-turbo'
text = st.text_input('Enter text', value= 'I love reading')

if st.button('Submit'):
    with st.spinner('OpenAI is processing your text'):
        sentiment = sentiment_analysis_using_chatgpt(text)
    
    st.write(f"Sentiment: {sentiment} ")


if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")
else:
    # Set the user-provided API key
    openai.api_key = api_key

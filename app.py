import os
import lyzr
from PIL import Image
import streamlit as st
from lyzr import FormulaGen

# Setup your config
st.set_page_config(
    page_title="Query2Excel",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png"
)

os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply the styles
style_app()

# Load and display the logo
image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Query2Excel built using Lyzr SDK🚀")
st.markdown("### Welcome to Query2Excel!📑")
st.markdown("Query2Excel simplifies data management by converting natural language queries into Excel format, streamlining report generation and information organization with its intuitive interface, enhancing productivity by eliminating manual data entry and complex formula creation.")

# Button to start query

generate = FormulaGen()

# Define the Streamlit app
def main():

    # Input field for natural language query
    query = st.text_input("Enter your natural language query :")

    # Generate formulas button
    if st.button("Generate"):
        if query:
            # Generate formulas based on the query
            result = generate.spreadsheets(query)
            st.write("Results:")
            st.write(result)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
    
 
# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Core to generate notes from transcribed audio. The audio transcription is powered by OpenAI's Whisper model. For any inquiries or issues, please contact Lyzr.
    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width=True)

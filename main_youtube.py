import streamlit as st
import langchain_helper_youtube as lch
import textwrap
from dotenv import load_dotenv

load_dotenv()

st.title("YouTube Assistant")

with st.sidebar:
    with st.sidebar.form(key='my_form'):
        youtube_url = st.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
            )
        query = st.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
            )
        # openai_api_key = st.sidebar.text_input(
        #     label="OpenAI API Key",
        #     key="langchain_search_api_key_openai",
        #     max_chars=50,
        #     type="password"
        #     )
        # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        # "[View the source code](https://github.com/rishabkumar7/pets-name-langchain/tree/main)"
        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()
    # else:
        db = lch.create_db_from_youtube_video_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85))
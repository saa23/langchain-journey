import streamlit as st
import langchain_helper_youtube as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
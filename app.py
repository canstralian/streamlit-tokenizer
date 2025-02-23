import streamlit as st
import tiktoken

# Streamlit page configuration
st.set_page_config(page_title='Token Counter', page_icon='📚', layout='wide')

# Initialize tokenizer with error handling
try:
    enc = tiktoken.get_encoding("cl100k_base")
except Exception as e:
    st.error(f"Error initializing tokenizer: {e}")
    st.stop()

# App title and instructions
st.title("Token Counter")
st.markdown("---")
st.write("This tool counts the number of tokens in a given text. To use it, type or paste your text in the text box below and click the 'Calculate' button.")

# Text input area
text_input = st.text_area("Type or paste your text here...", height=200)

# Calculate button with error handling and input validation
if st.button("Calculate", key="calculate_button"):
    if not text_input.strip():
        st.warning("Please enter some text before calculating tokens.")
    else:
        with st.spinner("Counting tokens..."):
            try:
                tokens = len(enc.encode(text_input))
                st.success(f"Number of tokens: {tokens}")
            except Exception as e:
                st.error(f"An error occurred during token counting: {e}")

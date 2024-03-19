import streamlit as st
import json
import requests


# Due to streamlit's lack of a function to clear a text field, I had to use a workaround.
# I created a function that stores the user's input in a session state variable and then 
# clears the text field when the "Generate Summary" button is clicked.
# This way, the user's input is not lost when the text field is cleared.


if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

def clear_text_field():
    st.session_state.user_input = st.session_state.text
    st.session_state.text = ''

# Function to get the summary from the API
def get_summary(user_input):
    url = 'https://ykzmqit5u9.execute-api.us-east-1.amazonaws.com/prod'
    input = json.dumps({'inputs': user_input})
    output = requests.post(url, data=input, headers={'content-type': 'application/json', 'x-api-key':''})
    return output.text[1:-1]

def main():
    
    st.title("Text Summarization with BART")

    st.text_area("Enter text to summarize:", key="text")

    if st.button("Generate Summary", on_click=clear_text_field):
        if st.session_state.user_input.strip():
            user_input = st.session_state.user_input
            
            st.subheader("Your Input:")
            st.write(user_input)

            summary = get_summary(user_input)
            
            st.subheader("Summary:")
            st.write(summary)
            
        else:
            st.warning("Please enter text to summarize.")
        
if __name__ == "__main__":
    main()
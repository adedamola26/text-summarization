import streamlit as st
from transformers import pipeline

# import psutil

# process = psutil.Process()
# memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes
# print(f"Memory Usage: {memory_usage} MB")


@st.cache_data
def get_summarizer():
    return pipeline('summarization', model='luisotorres/bart-finetuned-samsum')


def generate_summary(text):
    summarizer = get_summarizer()
    summary = summarizer(text)[0]['summary_text']
    return summary

def main():
    st.title("Text Summarization with BART")

    user_input = st.text_area("Enter text to summarize:")
    
    if st.button("Generate Summary"):
        if user_input:
            summary = generate_summary(user_input)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter text to summarize.")

if __name__ == "__main__":
    main()
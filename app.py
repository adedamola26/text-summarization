import streamlit as st
from transformers import pipeline

# model_name = "facebook/bart-large-cnn"
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

summarizer = pipeline('summarization', model = 'luisotorres/bart-finetuned-samsum')

def generate_summary(text):
    # inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    # summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    # summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary = summarizer(text)[0]['summary_text']
    return summary

# st.write("""
# # Text Summarization

# Enter your long-form text below to get a summary!

# """)

# st.text_area(
#             "",
#             placeholder="Enter your long form input here",
#         )

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
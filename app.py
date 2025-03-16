import nltk
import streamlit as st
import docx
from PyPDF2 import PdfReader
from langchain.llms import HuggingFaceHub
from nltk.sentiment import SentimentIntensityAnalyzer

# Define styles for sentiment analysis output
positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"

# Load Mistral AI model for summarization
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    model_kwargs={
        "temperature": 0.7,  # Control randomness
        "max_new_tokens": 10000,  # Limit token generation
    },
    huggingfacehub_api_token="Replace_with_your_HF_api_key"
)

# Function to extract text from different file types
def extract_text_from_txt(file):
    return file.read().decode("utf-8")

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

# Summarization function using Mistral AI
def summarize(text, summarizer, max_value=350, min_value=50):
    prompt = f"Summarize the following text in {min_value}-{max_value} words:\n\n{text}"
    summary = summarizer(prompt)
    return summary.strip()

# Sentiment analysis function
def analyze_sentiment(text):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    if sentiment_scores['pos'] > 0.15 and sentiment_scores['pos'] > sentiment_scores['neg']:
        return 'Positive', positive_style
    elif sentiment_scores['neg'] > 0.15 and sentiment_scores['neg'] > sentiment_scores['pos']:
        return 'Negative', negative_style
    return 'Neutral', ""

# Streamlit UI
def main():
    st.title('Text Summarizer and Sentiment Analysis App')

    user_input = st.text_area('Enter text here')
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "docx", "pdf"])

    text = ""
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "txt":
            text = extract_text_from_txt(uploaded_file)
        elif file_extension == "docx":
            text = extract_text_from_docx(uploaded_file)
        elif file_extension == "pdf":
            text = extract_text_from_pdf(uploaded_file)

    # Generate summary
    if st.button("Generate Summary"):
        if user_input or text:
            summary = summarize(user_input or text, llm, max_value=350, min_value=90)
            st.subheader("Generated Summary:")
            st.write(summary)
        else:
            st.warning("Please enter text or upload a file.")

    # Perform sentiment analysis
    if st.button("Perform Sentiment Analysis"):
        if user_input or text:
            sentiment_result, style = analyze_sentiment(user_input or text)
            st.subheader("Sentiment Analysis Result:")
            st.markdown(f"**Sentiment:** <span style='{style}'>{sentiment_result}</span>", unsafe_allow_html=True)
        else:
            st.warning("Please enter text or upload a file.")

if __name__ == '__main__':
    main()

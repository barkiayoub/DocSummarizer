# **DocSummarizer – AI-Powered Text Summarization & Sentiment Analysis**  

DocSummarizer is a **Streamlit-based web app** that extracts, summarizes, and analyzes sentiment from **TXT, DOCX, and PDF files** using **T5-Large** for text summarization and **NLTK** for sentiment analysis.  

---

## **Features**  
- AI-powered summarization using `T5-Large`.  
- Supports text extraction from **TXT, DOCX, and PDF** files.  
- Sentiment analysis to classify text as **Positive, Neutral, or Negative**.  
- User-friendly web app built with **Streamlit**.  
- Efficient processing for handling large text chunks.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/DocSummarizer.git
cd DocSummarizer
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit App**  
```bash
streamlit run app.py
```

---

## **Supported File Formats**  
- **TXT Files** – Reads raw text.  
- **DOCX Files** – Extracts text from Microsoft Word documents.  
- **PDF Files** – Extracts text from all pages using `PyPDF2`.  

---

## **Usage**  
1. Upload a **TXT, DOCX, or PDF** file through the Streamlit interface.  
2. Choose a summarization length (minimum and maximum words).  
3. Click **"Summarize"** to generate a summary.  
4. View the sentiment analysis result (**Positive, Neutral, or Negative**).  

---

## **Dependencies**  
- `transformers` – Hugging Face's `T5-Large` for summarization.  
- `nltk` – Sentiment analysis using `VADER`.  
- `streamlit` – Web interface.  
- `PyPDF2` – PDF text extraction.  
- `python-docx` – DOCX text extraction.  

---

<!-- ## **Demo Screenshot**  
_(You can add a screenshot of the app interface here.)_  

--- -->

## **License**  
This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.  

---

## **Contributing**  
Fork this repository and contribute by creating a **GitHub Issue** or submitting a **Pull Request**.  


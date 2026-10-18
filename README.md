# 🤖 GenAI Concept Explainer

An interactive GenAI application that explains complex technical concepts using intuitive real-world analogies. Built with LangChain Expression Language (LCEL), OpenAI's `gpt-4o-mini`, and Streamlit.

---

## ✨ Features
- **Modern LCEL Architecture:** Clean pipeline connecting Prompt Template, LLM, and Output Parser.
- **Real-Time Streaming:** Responsive token-by-token output using Streamlit's `st.write_stream`.
- **Conversational Memory:** Preserves multi-turn conversation context across interactions.
- **Interactive Web UI:** Simple and clean chat interface built with Streamlit.

---

## 🛠️ Tech Stack
- **Framework:** LangChain
- **Model:** OpenAI (`gpt-4o-mini`)
- **Frontend:** Streamlit
- **Environment Management:** Python `dotenv`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/filmr-oss/GenAI_W2_D5.git](https://github.com/filmr-oss/GenAI_W2_D5.git)
cd GenAI_W2_D5
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install langchain langchain-openai streamlit python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Application
- **Streamlit Web UI:**
  ```bash
  streamlit run streamlit_app.py
  ```
- **Terminal CLI:**
  ```bash
  python app.py
  ```

# 🤖 agentic-ai

**agentic-ai** is a smart conversational agent powered by LLMs like **Google Gemini**, enhanced with web search via **DuckDuckGo**. Built using the [phi](https://github.com/joaomdmoura/phi) framework, this project demonstrates agentic reasoning, tool use, and LLM integration.

---

## 🚀 Features

- 🌐 Web search using DuckDuckGo
- 📥 Accepts user input from the command line
- 📄 Markdown-enabled responses with visible tool calls

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentic-ai.git
cd agentic-ai
```

### 2.Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# Or use `source venv/bin/activate` on macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a .env file in the root folder and add your API keys:

.env
```bash
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 🧪 Run the App
```bash
python app.py
```

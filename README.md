# 🤖 QA Assistant Bot

**AI-powered assistant for QA engineers**  
Uses OpenAI + LangChain to answer questions from test cases, feature files, logs, specs, and more — all from natural language.

---

## 🧠 Purpose

This bot helps QA engineers:

- ✅ Ask natural questions like:  
  _"What are the steps in TC-001?"_  
  _"List test cases for login."_

- 📄 Understand test specs and logs quickly
- 🔍 Search across multiple formats (JSON, Markdown, PDF, etc.)
- 🧪 Automate documentation understanding and reduce manual effort

---

## 📁 Supported File Types

It can read and index:

- `.json` — Test cases
- `.feature` — BDD specs
- `.md` — Requirements
- `.txt` — Logs
- `.html` — Reports
- `.pdf` — Test documents
- `.docx` — Word specs

Place files inside the `data/` folder.

---

## ⚙️ Installation

### ✅ 1. Clone the repo

```bash
git clone https://github.com/aiqualitylab/AI-QA-Assistant-Bot
cd qa-bot
```

### ✅ 2. Set up Python environment
Make sure Python 3.10+ is installed. Then:

```bash
pip install -r requirements.txt
```

### ✅ 3. Create .env file
In the project root, create a file called .env:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

🔐 You can get your API key from: https://platform.openai.com/account/api-keys

## 🚀 Run the Assistant

```bash
python bot.py
```

If it's your first run, it will index the documents. After that, it reuses the saved index.

You'll see:

```bash
🤖 QA Assistant Ready! Ask anything (type 'exit' to quit')
```

## 💬 Example Questions to Try

- What is the expected result of TC-002?
- What steps are in TC-003?
- Summarize all login test cases.
- What's inside the markdown spec?

## 🛠️ Optional Fix (LangChain warning)

If you see a deprecation warning about run(), you can change:

```python
qa.run(query)
```

To:

```python
qa.invoke(query)
```

## ✅ Tips

- You can add any number of files inside the data/ folder
- Re-run the bot to re-index updated content
- The assistant uses FAISS + OpenAI to give accurate, contextual answers

## 📌 Project Structure

```arduino
qa-bot/
├── data/                ← Your documents go here
├── bot.py               ← Main script
├── qa_utils.py         ← Loaders + vector index
├── requirements.txt     ← Python dependencies
├── .env                ← Your OpenAI API key
```

## 👨‍💻 Built With

- LangChain
- OpenAI API
- FAISS Vector Search


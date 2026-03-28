# 💰 AI-Powered Money Mentor

An AI-driven personal finance assistant that provides financial health scoring, strategic advice, and a conversational chatbot — all personalized to your financial profile. Built with Python, Streamlit, LangChain, and Groq's LLM backend.

---

## Features

- **📊 Financial Health Score** — Get a percentage-based score reflecting your overall financial well-being, along with AI-generated improvement steps.
- **💡 Strategic Advice** — Receive a numbered list of actionable steps tailored to your goals, including insurance and investment suggestions.
- **🤖 Q&A Chatbot** — Ask follow-up financial questions in a multi-turn conversational interface that remembers your entire financial profile.

---

## Project Structure

```
ai-money-mentor/
│
├── main.py            # App entry point, UI controller, input form
├── calculations.py    # Financial health score logic (JSON output)
├── suggestions.py     # Strategic advice generation (text output)
├── chatbot.py         # Multi-turn conversational chatbot
├── .env               # API keys (not committed to version control)
└── requirements.txt   # Python dependencies
```

---

## Tech Stack

| Component         | Technology                          |
|-------------------|-------------------------------------|
| UI Framework      | Streamlit                           |
| LLM Integration   | LangChain + ChatGroq                |
| LLM Model         | `groq/compound`                     |
| Output Parsing    | `JsonOutputParser`, `StrOutputParser` |
| Environment Config| `python-dotenv`                     |

---

## Prerequisites

- Python 3.9 or higher
- A [Groq API key](https://console.groq.com/)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-money-mentor.git
cd ai-money-mentor
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## Running the App

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Usage

1. Enter your financial details in the input form:
   - **Income** (₹)
   - **Expenses** (₹)
   - **Savings** (₹)
   - **Loans** (₹)
   - **Financial Goals** (comma-separated, e.g. `buy a house, clear debt, build emergency fund`)

2. Use the sidebar to choose a feature:
   - **📈 Check Financial Health** — View your health score and improvement advice.
   - **💡 Get Advice** — Get a strategic, goal-oriented action plan.
   - **🤖 Q&A Chatbot** — Ask any financial question in a live chat.

---

## Requirements

Add the following to your `requirements.txt`:

```
streamlit
langchain
langchain-groq
langchain-core
python-dotenv
```

---

## Architecture Overview

```
User Input (Income, Expenses, Savings, Loans, Goals)
            │
            ▼
      main.py (Streamlit UI + session state)
            │
    ┌───────┼───────────┐
    ▼       ▼           ▼
calc.py  suggest.py  chatbot.py
    └───────┴───────────┘
                │
                ▼
    LangChain + ChatGroq (groq/compound)
                │
                ▼
           Groq LLM API
```

---

## Notes

- All financial inputs must be valid numeric values.
- The chatbot session resets each time the **Q&A Chatbot** button is clicked.
- The `.env` file must never be committed to version control. Add it to `.gitignore`.

---

## Future Improvements

- Add inputs for existing investments and insurance (as planned in the architecture).
- Persist financial history across sessions using a database.
- Add user authentication for a personalized multi-user experience.
- Improve input validation for edge cases (negative values, expenses exceeding income).
- Deploy on Streamlit Cloud or a cloud platform for public access.

---

## License

This project is intended for educational purposes as part of the AI & ML curriculum at CMR Institute of Technology, Bengaluru.

from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import json

load_dotenv()
model = ChatGroq(model="groq/compound")

def progress(income: float, expenses: float, savings: float, loans: float, goals: list[str]):
    prompt = f"""
    You are a financial advisor. You are given the following financial data of a user:
    Income: {income}
    Expenses: {expenses}
    Savings: {savings}
    Loans: {loans}
    Financial Goals: {goals}

    Based on the above data, calculate the financial health score of the user
    and provide advice on how to improve it.
    The output should be a valid JSON object with:
    - score: financial health score (as a percentage number)
    - advice: a list of steps the user can take to improve their financial health
    Return only the JSON object, no extra text.
    """
    response = model.invoke(prompt)          # use .invoke(), not model(prompt)
    parsed = JsonOutputParser().parse(response.content)  # parse .content string
    st.subheader("📊 Financial Health Score")
    st.metric("Score", f"{parsed.get('score', 'N/A')}%")
    st.subheader("💡 Advice")
    for step in parsed.get("advice", []):
        st.write(f"- {step}")
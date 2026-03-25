from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGroq(model="groq/compound")

def advice(income: float, expenses: float, savings: float, loans: float, goals: list[str]) -> None:
    prompt = f"""
    You are a financial advisor. You are given the following financial data of a user:
    Income: {income}
    Expenses: {expenses}
    Savings: {savings}
    Loans: {loans}
    Financial Goals: {goals}

    Based on the above data, give strategic advice to the user on how to achieve their financial goals,
    including suggestions on insurance and investment options.
    Format the output as a numbered list of actionable steps.
    """
    response = model.invoke(prompt)           # use .invoke()
    parsed = StrOutputParser().parse(response.content)  # parse .content
    st.subheader("🎯 Strategic Advice")
    st.write(parsed)
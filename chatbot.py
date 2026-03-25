from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGroq(model="groq/compound")

def chat(income: float, expenses: float, savings: float, loans: float, goals: list[str]):
    system_prompt = f"""
    You are a helpful financial advisor chatbot. The user's financial profile is:
    - Income: {income}
    - Expenses: {expenses}
    - Savings: {savings}
    - Loans: {loans}
    - Financial Goals: {goals}

    Answer the user's questions based on this profile. Be concise and practical.
    """

    # Init chat history only if not already present
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.subheader("🤖 Financial Q&A Chatbot")

    # Render full chat history first
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)
        else:
            st.chat_message("assistant").write(msg.content)

    # Chat input at the bottom
    user_input = st.chat_input("Ask a financial question...")

    if user_input:
        # Append and show user message
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.chat_message("user").write(user_input)

        # Build full message list with system context
        messages = [SystemMessage(content=system_prompt)] + st.session_state.chat_history

        # Get model response
        response = model.invoke(messages)
        reply = StrOutputParser().parse(response.content)

        # Append and show assistant response
        st.session_state.chat_history.append(AIMessage(content=reply))
        st.chat_message("assistant").write(reply)
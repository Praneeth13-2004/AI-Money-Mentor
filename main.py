import streamlit as st
import suggestions
import calculations
import chatbot

if __name__ == "__main__":
    st.set_page_config(page_title="AI Powered Money Mentor", layout="wide")
    st.sidebar.header("AI Powered Money Mentor")
    st.title("💰 AI Powered Money Mentor")

    # Track which section is active across reruns
    if "active_section" not in st.session_state:
        st.session_state.active_section = None

    # Input section
    st.subheader("Enter Your Financial Details")
    income   = st.text_input("Income (₹)")
    expenses = st.text_input("Expenses (₹)")
    savings  = st.text_input("Savings (₹)")
    loans    = st.text_input("Loans (₹)")
    goals    = st.text_input("Financial Goals (comma-separated)")

    inputs_ready = all([income, expenses, savings, loans, goals])

    if inputs_ready:
        try:
            inc  = float(income)
            exp  = float(expenses)
            sav  = float(savings)
            loan = float(loans)
            goal_list = [g.strip() for g in goals.split(",")]

            # Sidebar buttons set the active section
            if st.sidebar.button("📈 Check Financial Health"):
                st.session_state.active_section = "health"

            if st.sidebar.button("💡 Get Advice"):
                st.session_state.active_section = "advice"

            if st.sidebar.button("🤖 Q&A Chatbot"):
                st.session_state.active_section = "chatbot"
                st.session_state.chat_history = []  # reset chat on re-open

            # Render the active section — persists across reruns
            if st.session_state.active_section == "health":
                calculations.progress(inc, exp, sav, loan, goal_list)

            elif st.session_state.active_section == "advice":
                suggestions.advice(inc, exp, sav, loan, goal_list)

            elif st.session_state.active_section == "chatbot":
                chatbot.chat(inc, exp, sav, loan, goal_list)

        except ValueError:
            st.error("⚠️ Please enter valid numeric values for Income, Expenses, Savings, and Loans.")
    else:
        st.info("Please fill in all fields above to get started.")
# Financial Guide — System Overview

**Financial Guide** is an AI-powered personal finance assistant designed to help users understand, evaluate, and improve their financial health. It takes basic financial inputs from users, analyzes them using rule-based logic, and enhances the results with AI-driven explanations and personalized advice.

The goal is to make financial planning simple, accessible, and actionable for everyone.

---

## How the System Works

The system follows a straightforward pipeline:

### 1. User Input (Financial Data & Goals)

The process starts with the user providing essential financial information. This includes:

- Income  
- Expenses  
- Savings  
- Existing investments  
- Loans  
- Insurance  

This data forms the **financial profile** of the user, which is used for all further analysis.

---

### 2. Backend Logic (Core Processing Layer)

Once the input is collected, it is passed to the backend logic, which performs two main tasks:

#### a) Score Calculation  
The system evaluates the user's financial health across multiple dimensions such as:

- Emergency preparedness  
- Debt management  
- Investment habits  
- Insurance coverage  
- Savings consistency  

Each category is scored (out of 100) and combined into an overall **Money Health Score**.

#### b) Rule-Based Suggestions  
Based on predefined financial rules, the system generates initial recommendations.  

Examples:
- If savings are low → suggest building an emergency fund  
- If debt is high → suggest reducing liabilities  
- If investments are missing → suggest starting SIPs  

This layer ensures reliable and consistent baseline advice.

---

### 3. Gen AI Layer (Intelligence & Personalization)

The output from the backend is passed to the Gen AI layer, which enhances the experience by:

- Converting raw scores into **easy-to-understand explanations**  
- Providing **personalized financial advice**  
- Highlighting strengths and weaknesses in a conversational manner  

Instead of showing just numbers, this layer makes the system feel like a **human financial mentor**.

**Example:**
> Your emergency fund is currently low. Ideally, you should have savings covering 6 months of expenses. Consider setting aside ₹5,000 monthly to improve this.

---

### 4. Output (Insights & Guidance)

The final output presented to the user includes:

- A detailed **financial report card**  
- Category-wise scores  
- Overall financial health score  
- Personalized suggestions for improvement  

This helps users clearly understand their financial position and take actionable steps.

---

## System Architecture Summary

The architecture consists of three main layers:

- **Input Layer** → Collects user financial data  
- **Backend Logic** → Performs calculations and rule-based analysis  
- **Gen AI Layer** → Adds explanations and personalized guidance  

### Flow
<img width="825" height="630" alt="Basic Skeleton of Project" src="https://github.com/user-attachments/assets/42e1d6f5-d55a-47e2-93e4-4d30a4771c88" />


---

## Key Advantages

- **Simple and Accessible** — Requires only basic financial inputs  
- **Actionable Insights** — Provides clear next steps, not just analysis  
- **AI-Powered Guidance** — Personalized and easy-to-understand advice  
- **No Dependency on External APIs** — Works entirely with user-provided data  

---

## Conclusion

Financial Guide bridges the gap between complex financial planning and everyday users. By combining structured financial analysis with AI-driven explanations, it transforms raw financial data into meaningful, personalized guidance—helping users move from confusion to confident financial decision-making.

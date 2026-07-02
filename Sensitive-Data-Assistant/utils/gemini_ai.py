import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a currently supported model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(text, detected, risk_level):

    prompt = f"""
You are a Cyber Security and Compliance Expert.

Analyze the uploaded document.

Risk Level:
{risk_level}

Sensitive Data Found:
{detected}

Document:
{text}

Generate the response in this format.

## Compliance Summary

(Explain in 2-3 lines)

## Security Risks

- Risk 1
- Risk 2
- Risk 3

## Suggested Remediation

- Recommendation 1
- Recommendation 2
- Recommendation 3

Keep it professional.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"
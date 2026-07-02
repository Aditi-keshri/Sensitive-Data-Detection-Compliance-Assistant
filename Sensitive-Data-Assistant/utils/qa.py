from utils.gemini_ai import model



def ask_question(document_text, question):

    prompt = f"""
You are an AI Document Assistant.

Answer ONLY using the uploaded document.

If the answer is not present in the document, reply:

"The document does not contain that information."

Uploaded Document:

{document_text}

Question:

{question}

Answer:
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
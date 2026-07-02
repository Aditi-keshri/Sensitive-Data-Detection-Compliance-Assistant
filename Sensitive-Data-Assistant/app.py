from flask import Flask, render_template, request, session,send_file
from utils.qa import ask_question
import os

from utils.pdf_reader import read_pdf
from utils.txt_reader import read_txt
from utils.csv_reader import read_csv
from utils.detector import detect_sensitive_data
from utils.classifier import classify_risk
from utils.gemini_ai import generate_summary
from utils.pdf_report import generate_pdf_report

app = Flask(__name__)
app.secret_key = "my_secret_key_123"

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed extensions
ALLOWED_EXTENSIONS = {"pdf", "txt", "csv"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "document" not in request.files:
        return "No file selected."

    file = request.files["document"]

    if file.filename == "":
        return "Please choose a file."

    if file and allowed_file(file.filename):

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

        file.save(filepath)

        extension = file.filename.rsplit(".", 1)[1].lower()

        # Read file
        if extension == "pdf":
            text = read_pdf(filepath)

        elif extension == "txt":
            text = read_txt(filepath)

        elif extension == "csv":
            text = read_csv(filepath)

        else:
            text = "Unsupported File"

        # Detect sensitive data
        detected = detect_sensitive_data(text)
        session["detected"] = detected
        session["document_text"] = text

        # Classify Risk
        risk_level, risk_score = classify_risk(detected)
        session["risk_level"] = risk_level
        session["risk_score"] = risk_score

        
        # Generate AI Summary
        ai_summary = generate_summary(
            text,
            detected,
            risk_level
)
        session["ai_summary"] = ai_summary

        return render_template(
            "result.html",
            text=text,
            detected=detected,
            risk_level=risk_level,
            risk_score=risk_score,
            ai_summary=ai_summary
)

    return "Invalid file type."
@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question")

    document_text = session.get("document_text")

    detected = session.get("detected")

    risk_level = session.get("risk_level")

    risk_score = session.get("risk_score")

    ai_summary = session.get("ai_summary")

    if not document_text:
        return "Please upload a document first."

    answer = ask_question(document_text, question)

    return render_template(
        "result.html",
        text=document_text,
        detected=detected,
        risk_level=risk_level,
        risk_score=risk_score,
        ai_summary=ai_summary,
        question=question,
        answer=answer
    )

@app.route("/download-report")
def download_report():

    detected = session.get("detected")
    risk_level = session.get("risk_level")
    risk_score = session.get("risk_score")
    ai_summary = session.get("ai_summary")

    if not detected:
        return "Please upload a document first."

    pdf_path = generate_pdf_report(
        detected,
        risk_level,
        risk_score,
        ai_summary
    )

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
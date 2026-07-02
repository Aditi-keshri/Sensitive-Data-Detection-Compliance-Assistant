from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_pdf_report(
    detected,
    risk_level,
    risk_score,
    ai_summary
):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/security_report_{timestamp}.pdf"
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>Sensitive Data Detection & Compliance Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk_level}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk_score}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    story.append(
        Paragraph(
            "<b>Detected Sensitive Data</b>",
            styles["Heading2"]
        )
    )

    for category, values in detected.items():

        if values:

            value = ", ".join(values)

        else:

            value = "None"

        story.append(

            Paragraph(

                f"<b>{category}</b>: {value}",

                styles["BodyText"]

            )

        )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    story.append(
        Paragraph(
            "<b>AI Compliance Analysis</b>",
            styles["Heading2"]
        )
    )

    story.append(

        Paragraph(

            ai_summary.replace("\n", "<br/>"),

            styles["BodyText"]

        )

    )

    doc.build(story)

    return filename
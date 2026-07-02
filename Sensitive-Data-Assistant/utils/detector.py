import re
from utils.masking import (
    mask_email,
    mask_phone,
    mask_pan,
    mask_aadhaar,
    mask_credit_card,
    mask_api_key,
    mask_password,
)


def detect_sensitive_data(text):

    results = {}

    # Email

    emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
    )
    results["Emails"] = [mask_email(email) for email in emails]

   

    # Phone Numbers
    phones = re.findall(
    r"\b\d{10}\b",
    text
)

    results["Phone Numbers"] = [mask_phone(phone) for phone in phones]

    # Aadhaar
    aadhaar = re.findall(
    r"\b\d{4}\s\d{4}\s\d{4}\b",
    text
)

    results["Aadhaar Numbers"] = [mask_aadhaar(a) for a in aadhaar]
    
    # PAN
    pan = re.findall(
    r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    text
)

    results["PAN Numbers"] = [mask_pan(p) for p in pan]

    # Credit Card
    cards = re.findall(
    r"\b(?:\d[ -]*?){13,16}\b",
    text
)

    results["Credit Card Numbers"] = [
    mask_credit_card(card) for card in cards
]

    # IFSC
    results["IFSC Codes"] = re.findall(
        r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        text
    )

    # Employee IDs
    results["Employee IDs"] = re.findall(
        r"\bEMP\d+\b",
        text,
        re.IGNORECASE
    )

    # API Keys
    keys = re.findall(
    r"(?:api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?([A-Za-z0-9_\-]+)",
    text,
    re.IGNORECASE
)

    results["API Keys"] = [mask_api_key(key) for key in keys]

    # Passwords
    passwords = re.findall(
    r"password\s*[:=]\s*['\"]?([^\s'\"]+)",
    text,
    re.IGNORECASE
)

    results["Passwords"] = [
    mask_password(password) for password in passwords
]

    keywords = [
        "confidential",
        "internal",
        "salary",
        "trade secret",
        "private",
        "financial report",
        "acquisition"
    ]

    found = []

    for word in keywords:
        if word.lower() in text.lower():
            found.append(word)

    results["Confidential Keywords"] = found

    return results
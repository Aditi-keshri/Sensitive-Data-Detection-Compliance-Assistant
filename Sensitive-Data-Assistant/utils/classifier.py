def classify_risk(detected):

    score = 0

    # High Risk Data
    score += len(detected["Aadhaar Numbers"]) * 5
    score += len(detected["Credit Card Numbers"]) * 5
    score += len(detected["Passwords"]) * 5
    score += len(detected["API Keys"]) * 5

    # Medium Risk Data
    score += len(detected["PAN Numbers"]) * 3
    score += len(detected["IFSC Codes"]) * 3
    score += len(detected["Employee IDs"]) * 2

    # Low Risk Data
    score += len(detected["Emails"])
    score += len(detected["Phone Numbers"])

    score += len(detected["Confidential Keywords"]) * 2

    if score >= 15:
        return "HIGH", score

    elif score >= 6:
        return "MEDIUM", score

    else:
        return "LOW", score
def mask_email(email):
    """
    Example:
    keshriaditi01@gmail.com
    ↓
    ***********01@gmail.com
    """

    username, domain = email.split("@")

    if len(username) <= 2:
        return "*" * len(username) + "@" + domain

    visible = username[-2:]

    masked = "*" * (len(username) - 2)

    return masked + visible + "@" + domain


def mask_phone(phone):
    """
    7541979140
    ↓
    ******9140
    """

    return "*" * 6 + phone[-4:]


def mask_pan(pan):
    """
    ABCDE1234F
    ↓
    ******234F
    """

    return "*" * 6 + pan[-4:]


def mask_aadhaar(aadhaar):
    """
    1234 5678 9012
    ↓
    ********9012
    """

    digits = aadhaar.replace(" ", "")

    return "*" * 8 + digits[-4:]


def mask_credit_card(card):
    """
    4532123412345678
    ↓
    ************5678
    """

    digits = card.replace(" ", "").replace("-", "")

    return "*" * (len(digits) - 4) + digits[-4:]


def mask_api_key(key):
    """
    AIzaSyABC123XYZ
    ↓
    ***********XYZ
    """

    if len(key) <= 4:
        return "*" * len(key)

    return "*" * (len(key) - 4) + key[-4:]


def mask_password(password):
    """
    admin123
    ↓
    ********
    """

    return "*" * len(password)
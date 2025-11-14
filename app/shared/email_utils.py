from email_validator import validate_email, EmailNotValidError


def is_valid_email(email: str) -> bool:
    try:
        # valida e normaliza o e-mail
        valid = validate_email(email)
        return True
    except EmailNotValidError:
        return False
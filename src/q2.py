"""HW1 Question 2

Please implement the following function according to the provided documentation.
Tests are provided for this question in the file tests/test_q2.py."""

def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in "!@#$%^&*":
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

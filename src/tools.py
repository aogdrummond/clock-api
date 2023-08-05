import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_parameters(hours: str, minutes: str) -> dict:
    """
    Normalizes and validates the hour and minute parameters for clock calculations,
    providing error message if the inputs are not as expected.

    Args:
        hours (str): The hour value as a string.
        minutes (str): The minute value as a string.

    Returns:
        dict: A dictionary containing the normalized hours and minutes, or an error message.
    """
    normalized = {}
    try:
        if isinstance(hours, str) and isinstance(minutes, str):
            if 1 <= int(hours) <= 12:
                normalized['hours'] = int(hours)
            else:
                error_message = "Value for hour not allowed. A clock has hour values between 1 and 12."
                normalized["message"] = error_message

            if 0 <= int(minutes) < 60:
                normalized['minutes'] = int(minutes)
            else:
                error_message = "Value for minutes not allowed. A clock has minutes values between 0 and 59."
                normalized["message"] = error_message
        else:
            error_message = "Invalid input provided. Hours and minutes must be provided as strings."
            logger.warning(error_message)
            normalized["message"] = error_message
    except ValueError:
        error_message = "The input provided must be an integer!"
        logger.warning(error_message)
        normalized["message"] = error_message

    return normalized

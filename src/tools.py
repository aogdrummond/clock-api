import logging
logger = logging.getLogger()
logger.setLevel("INFO")

def normalize_parameters(hours,minutes):
    
    if isinstance(hours,str) and isinstance(minutes,str):
        normalized = {}
        try:
            if 1 <= int(hours) and int(hours) <= 12:
                normalized['hours'] = int(hours)
            else:
                error_message = " Value for hour not allowed. A clock has hour values between 1 and 12."
                normalized["message"] = error_message
            if 0 <= int(minutes) and int(minutes) < 60:
                normalized['minutes'] = int(minutes)
            else:
                error_message = " Value for minutes not allowed. A clock has minutes values between 0 and 60."
                normalized["message"] = error_message
        except ValueError:
            error_message = "The input provided must be an integer!"
            normalized["message"] = error_message
    else:
        message = f"Invalid input provided. Hours: {hours}. Minutes: {minutes}"
        logging.warning(message)
    

    return normalized
import logging
from flask import Flask, request
from flask_caching import Cache
from flask_restx import Api
from typing import Dict, Union, Tuple
from src.clock_calculator import calculate_angle_between_arrows

def process_parameters(params: Dict[str, Union[int, str]], args: str) -> Dict[str, Union[float, str]]:
    """
    Process parameters and calculate the angle between arrows based on hours and minutes.

    This function takes in two dictionaries, 'params' and 'args', and performs the following tasks:
    
    1. Check if both 'hours' and 'minutes' keys in 'params' have integer values.
    2. If yes, calculate the angle between the arrows using 'calculate_angle_between_arrows' function
       with 'params["hours"]' and 'params["minutes"]' as input.
    3. If the 'mode' in 'args' is "local", persist the result and the client's IP address to the database.
       The result is stored under the 'angle' key in the 'params' dictionary.
    4. If any exception occurs during the process, log a warning message and return an error message.
    
    Parameters:
        params (Dict[str, Union[int, str]]): A dictionary containing the parameters 'hours', 'minutes', and 'message'.
                                             The 'hours' and 'minutes' keys should have integer values.
        args (Dict[str, str]): A dictionary containing arguments. It should have a key 'mode' with value "local"
                               to trigger database persistence.
    
    Returns:
        Dict[str, Union[float, str]]: A dictionary containing the calculated angle or an error message.
        
    Example:
        params = {"hours": 3, "minutes": 15, "message": "Optional error message"}
        args = {"mode": "local"}
        result = process_parameters(params, args)
        # Example of successful calculation:
        # result = {"angle": 97.5}
        
        # Example of error due to invalid parameters:
        # result = {"ERROR": "Optional error message"}
    """

    logger = logging.getLogger("appLogger")
    if all([isinstance(params.get(key),int) for key in ["hours","minutes"]]):
        try:
            params["angle"] = calculate_angle_between_arrows(params["hours"], params["minutes"])
            
            if args.mode == "local":
                from db.connector import dB_Cursor
                cursor = dB_Cursor()
                cursor.persist_result(params, request.remote_addr)
            
            result = {"angle": params["angle"]}
        except Exception as e:
            logger.warning(f"There was found an error: {e}")
            result = {"Error found": str(e)}
    else:
        result = {"ERROR": params.get('message')}

    return result


def setup_flask() -> Tuple[Flask, Cache]:
    """
    Set up Flask application and caching.

    This function creates a Flask application and sets up caching using Flask-Caching.
    
    Returns:
        Tuple[Flask, Cache]: A tuple containing the Flask application and the Cache instance.
    """
    app = Flask(__name__)
    cache = Cache(app)
    return app, cache

def setup_api(app: Flask) -> Api:
    """
    Set up Flask-RESTx API.

    This function creates a Flask-RESTx API instance with the provided Flask application and configures
    its title, version, and URL prefix.
    
    Parameters:
        app (Flask): The Flask application instance to which the API will be attached.
    
    Returns:
        Api: The Flask-RESTx API instance.
    """
    api = Api(app, title="Clock API", version="1.0", prefix="/vn/rest",
              description="API aiming to calculate the smallest angle between clock's arrows.")
    return api
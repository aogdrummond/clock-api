import os
import logging
from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_caching import Cache
from src.clock_calculator import calculate_angle_between_arrows
from src.tools import validate_parameters
from db.connector import dB_Cursor

logger = logging.getLogger()
logger.setLevel(logging.INFO)
cursor = dB_Cursor()
app = Flask(__name__)
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)
api = Api(
    app,
    title="Clock API",
    version="1.0",
    prefix="/vn/rest",
    description="API aiming to calculate the smallest angle between clock's arrows.",
)

@api.route("/calculate-clock/<hours>", defaults={"minutes": '0'})
@api.route("/calculate-clock/<hours>/<minutes>")
# @cache.cached(timeout=600)
class DegreeCalculator(Resource):
    """
    Resource class to handle clock angle calculation.
    """

    def get(self, hours: str, minutes: str):
        """
        Calculate the smallest angle between the clock's arrows.

        Args:
            hours (str): The hour value (1 to 12 or 0 to 23).
            minutes (str)[Default = 0]: The minute value (0 to 59).

        Returns:
            dict: A dictionary containing the calculated angle.
        """
        
        parameters = validate_parameters(hours, minutes)
        if isinstance(parameters.get("hours"), int) and isinstance(parameters.get("minutes"), int):
            try:
                parameters["angle"] = calculate_angle_between_arrows(parameters["hours"], parameters["minutes"])
                cursor.persist_result(parameters, request.remote_addr)
                result = {"angle": parameters["angle"]}
            except Exception as e:
                logger.warning(f"There was found an error: {e}")
                result = {"Error found": str(e)}
        else:
            result = {"ERROR": parameters.get('message')}

        return jsonify(result)


if __name__ == "__main__":

    port = int(os.environ.get("API_PORT"))
    app.run(port=port, debug=True)
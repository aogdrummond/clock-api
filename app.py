import os
from logs.logging_config import LOG_CONFIG,setup_logging
import argparse
from dotenv import load_dotenv
from flask import jsonify
from flask_restx import Resource
from api_procedures import process_parameters, setup_flask, setup_api
from src.utils import validate_parameters

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--mode",default="local")
args = parser.parse_args()

app, cache = setup_flask()
api = setup_api(app)

@api.route("/calculate-clock/<hours>", defaults={"minutes": '0'})
@api.route("/calculate-clock/<hours>/<minutes>")

class DegreeCalculator(Resource):
    """
    Resource class to handle clock angle calculation.
    """
    @cache.cached(timeout=600)
    def get(self, hours: str, minutes: str):
        """
        Calculate the smallest angle between the clock's arrows.

        Args:
            hours (str): The hour value (1 to 12 or 0 to 23).
            minutes (str)[Default = 0]: The minute value (0 to 59).

        Returns:
            dict: A dictionary containing the calculated angle.
        """
        
        params = validate_parameters(hours, minutes)
        result = process_parameters(params,args)

        return jsonify(result)

if __name__ == "__main__":

    setup_logging(LOG_CONFIG)
    app.run(port=os.environ.get("API_PORT"),
            host = os.environ.get("API_HOST"),
            debug=False)
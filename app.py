import os
import logging
import argparse
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_caching import Cache
from src.clock_calculator import calculate_angle_between_arrows
from src.tools import validate_parameters
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--mode",default="local")
args = parser.parse_args()

logging.basicConfig(filename='logs/app.log', level=logging.INFO,format='%(asctime)s -  %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = Flask(__name__)
app.config["CACHE_TYPE"] = "SimpleCache"
api = Api(app,title="Clock API",version="1.0",prefix="/vn/rest",
          description="API aiming to calculate the smallest angle between clock's arrows.",)
cache = Cache(app)

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
        
        params = validate_parameters(hours, minutes)
        if isinstance(params.get("hours"), int) and isinstance(params.get("minutes"), int):
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

        return jsonify(result)

if __name__ == "__main__":

    port = int(os.environ.get("API_PORT"))
    host = os.environ.get("API_HOST")
    app.run(port=port,host = host, debug=False)
import os
import logging
from flask import Flask, request,jsonify
from flask_restx import Api, Resource
from flask_caching import Cache
from src.clock_calculator import calculate_angle_between_arrows
from src.tools import normalize_parameters
from db.connector import dB_Cursor

logger = logging.getLogger()
logger.setLevel("INFO")
cursor = dB_Cursor()

app = Flask(__name__)
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)
api = Api(app, title="Clock API", version="1.0", prefix="/vn/rest")

# @api.route("/")
# class HelloWorld(Resource):
#     def get(self):
#         """
#         Hello World route.

#         Returns:
#             str: A greeting message.
#         """
#         return "Hello, World!"

@api.route("/clock/<hours>",defaults = {"minutes":"0"})
@api.route("/clock/<hours>/<minutes>")
# @cache.cached(timeout=600)
class DegreeCalculator(Resource):
    def get(self,hours,minutes):
        """
        """
        #IMPLEMENTAR CACHE
        #CONFIGURAR SWAGGER
        parameters = normalize_parameters(hours,minutes)
        if (isinstance(parameters["hours"],int) and isinstance(parameters["minutes"],int)):          
            try:
                parameters["angle"] = calculate_angle_between_arrows(parameters["hours"],parameters["minutes"])
                cursor.persist_result(parameters,request.remote_addr)
                result = {"angle":parameters["angle"]}
            except Exception as e: 
                logger.warning(f"There was found an error: {e}")
                result = {"Error found":e}
        else:
            result = {"ERROR":parameters.get('message')}
        return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("API_PORT"))
    app.run(port=port, debug=True)
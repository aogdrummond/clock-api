import logging
from flask import Flask, request
from flask_caching import Cache
from flask_restx import Api

from src.clock_calculator import calculate_angle_between_arrows

def process_parameters(params,args):
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
        logger.warning(f"There was found an error: {params.get('message')}")
        result = {"ERROR": params.get('message')}

    return result

def setup_flask():
    app = Flask(__name__)
    app.config["CACHE_TYPE"] = "SimpleCache"
    cache = Cache(app)
    return app, cache

def setup_api(app):
    api = Api(app,title="Clock API",version="1.0",prefix="/vn/rest",
              description="API aiming to calculate the smallest angle between clock's arrows.",)

    return api
    
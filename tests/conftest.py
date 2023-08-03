import os
import sys
sys.path.append('.')
import pytest
from dotenv import load_dotenv
from run import app
from unittest import mock
from db.connector import connect_to_database
load_dotenv()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def database_cursor():
    # Mock the environment variables for the database connection
    with mock.patch.dict(os.environ, {"DB_HOST": "localhost",
                                 "DB_PORT": "5432",
                                 "DB_NAME": "test_db",
                                 "DB_USER": "test_user",
                                 "DB_PASSWORD": "password"}):
        conn = connect_to_database()
        yield conn.cursor()
        conn.close()
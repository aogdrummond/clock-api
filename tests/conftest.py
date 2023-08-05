import os
import sys
sys.path.append('.')
import pytest
from dotenv import load_dotenv
from app import app
from unittest import mock
from db.connector import dB_Cursor
load_dotenv()


cursor = dB_Cursor()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def database_cursor():
    yield cursor
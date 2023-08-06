import os
import sys
sys.path.append('.')
import pytest
import json
from unittest import mock

class Test_API:
    def test_degree_calculator_valid_input(self,client):
        response = client.get("/vn/rest/calculate-clock/6/30")
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert "angle" in data
        assert isinstance(data["angle"], int)

    route1 = "/vn/rest/calculate-clock/15/0"
    route2 = "/vn/rest/calculate-clock/12/60"
    route3 = "/vn/rest/calculate-clock/-2/10"
    @pytest.mark.parametrize("route",[route1,route2,route3])
    def test_degree_calculator_invalid_integer_input(self,client,route):
    
        response = client.get(route)
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert "ERROR" in data

    def test_degree_calculator_no_minutes_specified(self,client):
        response = client.get("/vn/rest/calculate-clock/3")
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert "angle" in data
        assert isinstance(data["angle"], int)

    def test_degree_calculator_non_integer_input(self,client):
        response = client.get("/vn/rest/calculate-clock/abc/xyz")
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert "ERROR" in data

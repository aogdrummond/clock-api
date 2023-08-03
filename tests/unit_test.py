import sys
sys.path.append('.')
import pytest
from src.clock_calculator import calculate_angle_between_arrows, calculate_minute_degree_from_zero, calculate_smaller_angle_between_arrows, calculate_hour_degree_from_zero

class Test_Calculations:
    case1 ={"hour":6,"minute":10,"degree":125}
    case2 ={"hour":9,"minute":0,"degree":90}
    case3 ={"hour":7,"minute":35,"degree":17}
    case4 ={"hour":12,"minute":17,"degree":94}
    @pytest.mark.parametrize("arrow",[case1,case2,case3,case4])
    def test_angle_calculation(self,arrow):

        hour = arrow['hour']
        minute = arrow['minute']
        expected = arrow['degree']
        degree = calculate_angle_between_arrows(hour,minute)
    
        assert degree == expected
    
    case1 = {"minute":0,"angle":0}
    case2 = {"minute":45,"angle":270}
    case3 = {"minute":17,"angle":102}
    @pytest.mark.parametrize("case",[case1,case2,case3])
    def test_calculate_minute_degree_from_zero(self,case):
    
        assert calculate_minute_degree_from_zero(case["minute"]) == case["angle"]
        
    case1 = {"hour":0,"minute":0,"angle":0}
    case2 = {"hour":4,"minute":15,"angle":127}
    case3 = {"hour":11,"minute":54,"angle":357}
    @pytest.mark.parametrize("case",[case1,case2,case3])
    def test_calculate_hour_degree_from_zero(self,case):
        # Test with various hours and minutes
        assert calculate_hour_degree_from_zero(case["hour"], case["minute"]) == case["angle"]
        
    case1 = {"angle1":0,"angle2":30,"smaller":30}
    case2 = {"angle1":45,"angle2":180,"smaller":135}
    case3 = {"angle1":250,"angle2":50,"smaller":160}
    @pytest.mark.parametrize("case",[case1,case2,case3])
    def test_calculate_smaller_angle_between_arrows(self,case):
        # Test with various arrow positions
        assert calculate_smaller_angle_between_arrows(case["angle1"], case["angle2"]) == case["smaller"]
        
def calculate_minute_degree_from_zero(minute:int)->int:
    """
    Calculates the degree between the number given and zero on the clock
    """
    return int(minute * 360/60)
    
def calculate_hour_degree_from_zero(hours:int,minute:int)->int:
    """
    Calculates the degree between the number given and zero on the clock
    
    """
    deg_per_hour = 360/12
    angle_per_minute = 30/60
    minute_angle = minute*angle_per_minute
    return int(hours * deg_per_hour) + int(minute_angle)

def calculate_smaller_angle_between_arrows(arrow_one_position:int,arrow_two_position:int)->tuple:
    """
    Calculates the angles in degrees between the two arrows
    """
    angle_1 = abs(arrow_one_position-arrow_two_position)
    if angle_1 < 180:
        smaller_angle = angle_1
    else:
        smaller_angle = 360 - angle_1
    return smaller_angle

def calculate_angle_between_arrows(hour:int,minute:int=0)->int:
    """
    """
    hour_angle = calculate_hour_degree_from_zero(hour,minute)
    minute_angle = calculate_minute_degree_from_zero(minute)
    smaller_angle = calculate_smaller_angle_between_arrows(hour_angle,minute_angle)

    return smaller_angle
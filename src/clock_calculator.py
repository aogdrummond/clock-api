def calculate_minute_degree_from_zero(minute: int) -> int:
    """
    Calculates the degree between the minute given and zero on the clock.

    Args:
        minute (int): The minute value (0 to 59).

    Returns:
        int: The degree between the minute and zero on the clock.
    """
    return int(minute * 360 / 60)


def calculate_hour_degree_from_zero(hours: int, minute: int) -> int:
    """
    Calculates the degree between the hour given and zero on the clock.

    Args:
        hours (int): The hour value (0 to 11 or 0 to 23).
        minute (int): The minute value (0 to 59).

    Returns:
        int: The degree between the hour and zero on the clock.
    """
    deg_per_hour = 360 / 12
    angle_per_minute = 30 / 60
    minute_angle = minute * angle_per_minute
    return int(hours * deg_per_hour) + int(minute_angle)


def calculate_smaller_angle_between_arrows(arrow_one_position: int, arrow_two_position: int) -> int:
    """
    Calculates the smaller angle in degrees between two arrow positions on the clock.

    Args:
        arrow_one_position (int): The first arrow position (0 to 359 degrees).
        arrow_two_position (int): The second arrow position (0 to 359 degrees).

    Returns:
        int: The smaller angle in degrees between the two arrow positions.
    """
    angle_1 = abs(arrow_one_position - arrow_two_position)
    if angle_1 < 180:
        smaller_angle = angle_1
    else:
        smaller_angle = 360 - angle_1
    return smaller_angle


def calculate_angle_between_arrows(hour: int, minute: int = 0) -> int:
    """
    Calculates the smallest angle in degrees between the clock's hour and minute arrows.

    Args:
        hour (int): The hour value (0 to 11 or 0 to 23).
        minute (int, optional): The minute value (0 to 59). Default is 0.

    Returns:
        int: The smallest angle in degrees between the clock's hour and minute arrows.
    """
    hour_angle = calculate_hour_degree_from_zero(hour, minute)
    minute_angle = calculate_minute_degree_from_zero(minute)
    smaller_angle = calculate_smaller_angle_between_arrows(hour_angle, minute_angle)

    return smaller_angle

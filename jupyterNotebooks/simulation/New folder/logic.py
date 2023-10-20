import math
# calculates the velocity based on the acceleration
def calculate_velocity(v0, dt, acceleration) -> float:
    delta_vel = acceleration*dt
    return v0 + delta_vel


# TODO figure out scaling methods

def scale_change(height) -> float:
    return 0.6 * (1/height)




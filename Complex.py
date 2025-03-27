import time
import numpy as np
from collections import deque
import random

# receive from accelerometer: (accelerometer) 3 m/s^2 for x, y, z axis
# receive from gyroscope: (angular velocity) 3 degrees/s for x, y, z

# TEMP
# generates ramdomized data to simulate the data from accelerometer and gyroscope
# "uniform" ensures that the data will stay within the stated range
def get_sensor_data():
    import random
    ax = random.uniform(-1, 1) # accelerometer x axis
    ay = random.uniform(-1, 1) # accelerometer y axis
    az = random.uniform(9, 12) # accelerometer z axis
    gx = random.uniform(-100, 100) # gyroscope x axis
    gy = random.uniform(-100, 100) # gyroscope y axis
    gz = random.uniform(-100, 100) # gyroscope z axis
    return ax, ay, az, gx, gy, gz

STEP_THRESHOLD = 1.2 # minimum amount of strength for a step to count as valid
STEP_DELAY = 0.3 # minimum time between steps to ensure they are separate steps
GYRO_THRESHOLD = 50 # maximum amount of strength to prevent false data
ACCEL_TO_SPEED = 0.1  # converts acceleration to the speed/velocity (change depending on testing of accelerometer)

step_count = 0
distance_traveled = 0.0
last_step_time = 0
recent_accel = deque(maxlen=10) # stores recent zaxis acceleration

try:
    while True:
        # Read real-time accelerometer and gyroscope data
        ax, ay, az, gx, gy, gz = get_sensor_data()
        recent_accel.append(az)
        smoothed_az = np.mean(recent_accel)

        total_rotation = abs(gx) + abs(gy) + abs(gz) # abs is just absolute value
        if total_rotation > gyro_threshold:
            continue  # Skip if too much rotation detected (arm movement or noise)
        
        current_time = time.time()
        if smoothed_az > step_threshold and (current_time - last_step_time) > step_delay:
            step_count += 1
            distance_traveled += step_length # estimating distance based on step count
            last_step_time = current_time
            print(f"Step detected! Total Steps: {step_count}, Distance: {distance_traveled:.2f} meters")

            time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\nIdle mode stopped.\nTotal Steps: {step_count}\nTotal Distance Traveled: {distance_traveled:.2f} meters")

# If you know the time (t) of the acceleration: Velocity (v) = Acceleration (a) * Time (t). Since acceleration due to gravity is 9.8 m/s², if an object is accelerating at 1g, its velocity change is 9.8 m/s every second. 
# 1g = 9.8
# accel = 9.8 * Gs (given)
# vel = accel * time

#     if acceleromoeter is active in x direction2
#
# make adjustments every 5 seconds? second? - figure out optimal time
# // alterations: calculate velocity using acceleration 
#                   then calculate distance using velocity
#                       using gyroscope to catch swing motion for each step
#         if gyroscope = swing motion:
#           steps += 1
#         velocity = v_prev + (acceleration * time_diff)
#         distance = d_prev + (velocity * time_diff)

#         # assuming average step length is 2ft
#         print(f"your steps: {steps} \n distance: {distance}")
class Active:
 # This is the initializer (constructor) for the Active class. It initializes all attributes to zero
    def __init__(self):
        # these are all attributes of the instance, initialized to zero
        self.grav = 0
        self.distance = 0
        self.speed = 0
        self.time = 0
        self.velocity = 0
        self.acceleration = 0

    def run_time():
    # recursive fxn that will continously update the values during run time
    # define class active 
    #     asteps = 0
    #     adistance = 0
    #     
    #     speeds[]
    #     def runstart()
    #         timer() # displays timer + starts timer

    #         if accelerometer is active in x direction

    # make adjustments every 5 seconds? second? - figure out optimal time
    # // alterations: calculate velocity using acceleration
    #                   then calculate distance using velocity
    #                       using gyroscope to catch swing motion for each step
    #             if gyroscope = swing motion:
    #                 steps += 1
    #             velocity = v_prev + (acceleration * time_diff)
    #             distance = d_prev + (velocity * time_diff)
    #             every 5s log speed to speeds[]
    #             if current_speed > max_speed:
    #                max_speed = current_speed

    def runend():
        print(f"End of Run Summary: \n\nTime: {time_ran}\nAverage Speed: {avg_speed}\nHighest Speed Reached: {max_speed}\nDistance: {dist_ran}")
    #         average speed = 0
    #         time = 0

    #         time = stopwatch result    #         average speed = sum(speeds) / length of speeds[]

    #         print ( # include some flavor text
    #             average speed
    #             distance run
    #             time
    #             max(speeds)
    #         )

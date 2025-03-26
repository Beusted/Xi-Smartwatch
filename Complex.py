import time
import numpy as np
from collections import deque

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

def idle ():
    tsteps = 0
    tdist = 0
    period = 10 # ten second period
    
    while True:
        grav = float(input("Input the amount of gravity force felt: ")) # placeholder till accelerometer integration
        
        vel = (grav * 32.2) * period # calculating velocity in feet per second
        distance = vel * period # getting distance from velocity and period of time elapsed 
        step = distance / 2 # getting total steps assuming a step is about 2 feet long 

        tsteps += step
        tdist += distance / 5280
        print(f"\nTotal Steps: {int(tsteps)} \nTotal Distance: {tdist: 0.2f} Miles")
        time.sleep(period)
idle()

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

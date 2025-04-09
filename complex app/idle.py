import time
import json
import calendar
import logs
import numpy as np
from collections import deque
import random
import datetime
import os

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

step_threshold = 1.2 # minimum amount of strength for a step to count as valid
step_delay = 0.3 # minimum time between steps to ensure they are separate steps
gyro_threshold = 50 # maximum amount of strength to prevent false data
accel_to_speed = 0.1  # converts acceleration to the speed/velocity (change depending on testing of accelerometer)
step_length = 0.7

# tracking steps across days

# IMPORTANT!!! CHANGE STEP LOG PATH DEPENDING ON DEVICE OR IT WILL NOT WORK
step_log = '/Users/kaitlynlee/Documents/Xi-Smartwatch/complex app/steps.dat' # file holding tracked steps over time
step_data = {} # dictionary to use for reading/writing from/to step log file


step_count = 0
distance_traveled = 0.0
last_step_time = 0
recent_accel = deque(maxlen=10) # stores recent zaxis acceleration
start_time = time.time() # get the start time
last_reset_date = datetime.date.today()

try:
    while True:
        current_date = datetime.date.today()
        if current_date != last_reset_date:
            date_str = last_reset_date.strftime('%Y%m%d')
            logs.save_daily_totals(
                filename=step_log,
                date=date_str,
                steps=step_count,
                distance=distance_traveled / 1000  # Convert meters to km
            )
            print(f"Daily saved: {step_count} steps, {distance_traveled/1000:.2f} km")

            step_count = 0
            distance_traveled = 0.0
            last_reset_date = current_date

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
    
    # Save today's data before reporting
    date_str = datetime.date.today().strftime('%Y%m%d')
    logs.save_daily_totals(
        filename=step_log,
        date=date_str,
        steps=step_count,
        distance=distance_traveled / 1000  # Convert meters to km
    )
    print(f"Data saved for today: {step_count} steps, {distance_traveled/1000:.2f} km")

    #print("Looking for file:", step_log)
    #print("File exists:", os.path.exists(step_log))

    print("\n--- Weekly Summary ---")
    print(logs.report_weekly_summary(step_log))

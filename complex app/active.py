import time
import numpy as np
from collections import deque

import complex_app
class Active:
 # This is the initializer (constructor) for the Active class. It initializes all attributes to zero
    def __init__(self):
        # these are all attributes of the instance, initialized to zero
        self.step_count = 0
        self.distance_traveled = 0.0
        self.last_time_step = 0.0
        self.start_time = time.time()
        self.recent_accel = deque(maxlen=10)
        
        self.max_speed = 0.0
        self.previous_distance = 0.0
        self.previous_time = 0.0

    def start_run(self):
        
        self.step_count = 0
        self.distance_traveled = 0.0
        self.last_time_step = 0.0
        self.start_time = time.time()
        
        self.max_speed = 0.0
        self.previous_distance = 0.0
        self.previous_time = self.start_time
        
        self.STEP_THRESHOLD = complex_app.STEP_THRESHOLD
        self.STEP_DELAY = complex_app.STEP_DELAY
        self.GYRO_THRESHOLD = complex_app.GYRO_THRESHOLD
        self.STEP_LENGTH = complex_app.STEP_LENGTH
        print("Active mode started. Press Ctrl + C to stop.")
        
    def run_loop(self):
        
        try:
            while True:
                ax, ay, az, gx, gy, gz = complex_app.get_sensor_data()
                complex_app.recent_accel.append(az)
                smoothed_az = np.mean(self.recent_accel)
                
                total_rotation = abs(gx) + abs(gy) + abs(gz)
                if total_rotation > self.GYRO_THRESHOLD:
                    continue
                current_time = time.time()
                if smoothed_az > self.STEP_THRESHOLD and (current_time - self.last_step_time) > self.STEP_DELAY:
                    self.step_count += 1
                    self.distance_traveled += self.STEP_LENGTH # estimating distance based on step count
                    self.last_step_time = current_time
                    print(f"Steps: {self.step_count}, Distance: {self.distance_traveled:.2f} meters")
                    
                dt = current_time - self.previous_time
                if dt > 0:
                    dist_diff = self.distance_traveled - self.previous_distance
                    current_speed = dist_diff / dt  # m/s

                    if current_speed > self.max_speed:
                        self.max_speed = current_speed

                    self.previous_distance = self.distance_traveled
                    self.previous_time = current_time
                    
                    time.sleep(0.1)
        except KeyboardInterrupt:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if self.start_time is not None:
                elapsed_time = end_time - self.start_time
            else:
                elapsed_time = 0
            
            avg_speed = (self.distance_traveled / elapsed_time) if elapsed_time else 0
            print(f"End of Run Summary: \n\nTime: {current_time}\nAverage Speed: {avg_speed}\nMax Speed: {current_speed}\nTotal Distance: {self.distance_traveled}\nSteps: {self.step_count}")
    

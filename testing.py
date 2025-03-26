import time
import numpy as np
from collections import deque

# Simulated function to read accelerometer data (replace this with actual sensor readings)
def get_accelerometer_data():
    """Simulate real-time accelerometer data reading (Replace with real sensor reading)"""
    import random
    return random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(9, 10)  # Simulated X, Y, Z acceleration

# Step counter settings
STEP_THRESHOLD = 1.2  # Adjust based on sensor sensitivity
STEP_DELAY = 0.3  # Minimum time between steps in seconds

# Real-time tracking variables
last_step_time = 0
step_count = 0
recent_accel = deque(maxlen=10)  # Stores recent Z-axis acceleration values for smoothing

print("Starting real-time step counter... Press Ctrl+C to stop.")

try:
    while True:
        # Read real-time accelerometer data
        ax, ay, az = get_accelerometer_data()

        # Smooth the acceleration using moving average
        recent_accel.append(az)
        smoothed_az = np.mean(recent_accel)

        # Step detection: Detect peaks when acceleration crosses threshold
        current_time = time.time()
        if smoothed_az > STEP_THRESHOLD and (current_time - last_step_time) > STEP_DELAY:
            step_count += 1
            last_step_time = current_time
            print(f"Step detected! Total Steps: {step_count}")

        # Simulate real-time delay (Adjust based on sensor refresh rate)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nReal-time step counter stopped.")

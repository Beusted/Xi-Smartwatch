# If you know the time (t) of the acceleration: Velocity (v) = Acceleration (a) * Time (t). Since acceleration due to gravity is 9.8 m/s², if an object is accelerating at 1g, its velocity change is 9.8 m/s every second. 
# 1g = 9.8
# accel = 9.8 * Gs (given)
# vel = accel * time


# def idle
#     steps = 0
#     distance = 0
grav = float(input("Input the amount of gravity force felt: ")) # placeholder till accelerometer integration
time = float(input("Input amount of seconds elapsed: ")) # placeholder till accel integra

def idle (grav, time):
    vel = (grav * 32.2) * time # calculating velocity in feet per second
    distance = vel * time # getting distance from velocity and period of time elapsed 
    step = distance / 2 # getting total steps assuming a step is about 2 feet long 
    return step, distance # returns units to be printed 
step, distance = idle(grav, time) # gets the steps and distances and splits them up into seperate varable from a tuple

print(f"Steps: {step} \nDistance: {distance}ft") # displays values 


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

#     def runend()
#         average speed = 0
#         time = 0

#         time = stopwatch result
#         average speed = sum(speeds) / length of speeds[]
#         print ( # include some flavor text
#             average speed
#             distance run
#             time
#             max(speeds)
#         )

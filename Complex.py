# If you know the time (t) of the acceleration: Velocity (v) = Acceleration (a) * Time (t). Since acceleration due to gravity is 9.8 m/s², if an object is accelerating at 1g, its velocity change is 9.8 m/s every second. 
# 1g = 9.8
# accel = 9.8 * Gs (given)
# vel = accel * time


# def idle
#     steps = 0
#     distance = 0
grav = float(input("Input the amount of gravity force felt: ")) # placeholder till accelerometer integration
time = float(input("Input amount of seconds elapsed: "))

def idle (grav, time):
    vel = (grav * 32.2) * time
    distance = vel * time
    step = distance / 2 # average step is 2 feet long
    return step, distance # Unit is in feet
step, distance = idle(grav, time)

print(f"Steps: {step} \nDistance: {distance}ft")


#     if acceleromoeter is active in x direction2
#         steps += 1
#         distance = steps * 2
#         # assuming average step length is 2ft
#         print(f"your steps: {steps} \n distance: {distance}")

# define class active 
#     asteps = 0
#     adistance = 0
#     speeds[]
#     def runstart()
#         timer() # displays timer
#         if accelerometer is active  in x direction
#             steps += 1
#             distance = steps * 2
#             every 5s log speed to speeds[]

#     def runend()
#         average speed = 0
#         time = 0

#         time = stopwatch result
#         average speed = sum(speeds) / length of speeds[]
#         print ( # include some flavor text
#             average speed
#             distance run
#             time
#             min(speeds)
#             max(speeds)
#         )

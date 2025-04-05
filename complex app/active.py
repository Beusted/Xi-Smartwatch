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
    
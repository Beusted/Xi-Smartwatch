from logging import root
import time # meant to import the time module so that we can use the timer for our stopwatch and the timer function


options = input("Stopwatch     Timer\n\n") # gives the user options to use stopwatch or timer: will be changed
                                           # when we add the buttons

if options == 'Timer': # if user types in Timer it runs this code under it
    def format_time(seconds): # makes it so that the code is readable. HH:MM:SS.ss more presentable
        hours = int(seconds // 3600) # divdes the seconds by 3600 because that's how many seconds are in an hour.
                                     # // is added to remove any decimals
        minutes = int((seconds % 3600) // 60) # the % gives you the remainder after dividing by hours then divides
                                              # by 60 to get the min.
        seconds = seconds % 60  # Remaining seconds
        return f"{hours:02}:{minutes:02}:{seconds:05.2f}"  # Makes sure that we keep hours and minutes to 2 digits
                                                           # and makes seconds have 2 digits with 2 decimals.

    def countdown_timer(seconds): # defines our countdown timer by it's seconds
        print(f"Timer set for {format_time(seconds)}") # prints the message in the format indicated

        try:
            while seconds > 0: # starts the infinite loop and only ends once the timer in seconds reaches 0
                print(f"\rTime left: {format_time(seconds)}", end="") #\r is used to overwrite the
                                                                      # previous output to make it look clean
                                                                      # the end="" prevents automatic new lines
                time.sleep(0.01) # puases the loop for 0.01 seconds before the time get updated again
                seconds -= 0.01 # decreases by 0.01 in each iteration of the loop
            print("\nTime's up!") # when timer reaches 0 then this prints
        except KeyboardInterrupt: # lets the code stop smoothly instead of the program crashing
            print("\nTimer Stopped")




# Get user input for hours, minutes, and seconds
    if __name__ == "__main__": # makes sure that the code is run directly and not through a module
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = float(input("Enter seconds: "))

        total_seconds = (hours * 3600) + (minutes * 60) + seconds # converts the hours and minutes to seconds and added to seconds
        countdown_timer(total_seconds)



if options == 'Stopwatch': # if user types in Stopwatch it runs this code under it
    def format_time(seconds): # makes it so that the code is readable. HH:MM:SS.ss more presentable
        hours = int(seconds // 3600) # divdes the seconds by 3600 because that's how many seconds are in an hour.
                                     # // is added to remove any decimals
        minutes = int((seconds % 3600) // 60) # the % gives you the remainder after dividing by hours then divides
                                              # by 60 to get the min.
        seconds = seconds % 60  # Remaining seconds
        return f"{hours:02}:{minutes:02}:{seconds:05.2f}"  # Makes sure that we keep hours and minutes to 2 digits
                                                           # and makes seconds have 2 digits with 2 decimals.

    def stopwatch(): # defines the stopwatch function
        print("Press ENTER to start the stopwatch, and CTRL+C to stop.") # prints the instructions to user, will change
                                                                         # after we implement buttons
        input() # waits for user input
        print("Stopwatch started...") # lets user know that the stop watch started
        start_time = time.time() # keeps track of the current time

        try: # allows us to use CTRL+C to stop the stopwatch 
            while True: # lets the code loop uninterupted
                elapsed_time = time.time() - start_time # by subtracting the time to the start time we get the elapsed time
                                                        # how much time that has passed
                print(f"\rElapsed Time: {format_time(elapsed_time)}", end="") # prints out the elapsed time in the format
                                                                              # of HH:MM:SS.ss. \r is used to overwrite the
                                                                              # previous output to make it look clean
                                                                              # the end="" prevents automatic new lines
                time.sleep(0.01) # adds a delay of 0.01 to display smoothly
        except KeyboardInterrupt: # lets the code stop smoothly instead of the program crashing
            print("\nStopwatch stopped.") # prints out after the keyboard interrupts
            print(f"Total time: {format_time(time.time() - start_time)}") # prints the total time in the format
    if __name__ == "__main__": #makes it so that the code is run directly
        stopwatch()


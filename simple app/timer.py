import time
import pygame

# Initialize pygame for keyboard events
pygame.init()
pygame.display.set_mode((100, 100))
pygame.display.set_caption("Timer & Stopwatch")

# Main function for the application
def main():
    options = input("Stopwatch     Timer\n\n")  # gives the user options to use stopwatch or timer
    Enter = True

    while Enter:
        if options == 'Timer':  # if user types in Timer it runs this code under it
            def format_time(seconds):  # makes it so that the code is readable. HH:MM:SS.ss more presentable
                hours = int(seconds // 3600)  # divdes the seconds by 3600 because that's how many seconds are in an hour.
                                          # // is added to remove any decimals
                minutes = int((seconds % 3600) // 60)  # the % gives you the remainder after dividing by hours then divides
                                                   # by 60 to get the min.
                seconds = seconds % 60  # Remaining seconds
                return f"{hours:02}:{minutes:02}:{seconds:05.2f}"  # Makes sure that we keep hours and minutes to 2 digits
                                                               # and makes seconds have 2 digits with 2 decimals.

            def countdown_timer(seconds):  # defines our countdown timer by it's seconds
                print(f"Timer set for {format_time(seconds)}")
                print("Press P to pause, R to resume, Q to quit")
                paused = False
                start_time = time.time()  # prints the message in the format indicated
                running = True
                
                try:
                    while seconds > 0 and running:  # starts the loop and only ends once the timer in seconds reaches 0
                        print(f"\rTime left: {format_time(seconds)}", end="")  #\r is used to overwrite the
                                                                          # previous output to make it look clean
                                                                          # the end="" prevents automatic new lines
                        time.sleep(0.01)  # pauses the loop for 0.01 seconds before the time gets updated again
                        
                        # Handle pygame events
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:  # Pause on 'p' key
                                    print("\nPaused. Press R to resume.")
                                    paused = True
                                    while paused and running:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                running = False
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_r:  # Resume on 'r' key
                                                    print("Resumed.")
                                                    start_time = time.time()
                                                    paused = False
                                                elif event.key == pygame.K_q:  # Quit on 'q' key
                                                    running = False
                                                    paused = False
                                        pygame.time.delay(10)  # Small delay to prevent CPU hogging
                                elif event.key == pygame.K_q:  # Quit on 'q' key
                                    running = False
                        
                        if not paused:
                            seconds -= 0.01  # decreases by 0.01 in each iteration of the loop

                    if seconds <= 0:
                        print("\nTime's up!")  # when timer reaches 0 then this prints
                    else:
                        print("\nTimer Stopped")
                        
                except KeyboardInterrupt:  # lets the code stop smoothly instead of the program crashing
                    print("\nTimer Stopped")
                
                # Ask if user wants to return to main menu
                print("\nPress M to return to main menu or any other key to exit")
                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_m:
                                return True  # Return to main menu
                            else:
                                return False  # Exit program
                    pygame.time.delay(10)  # Small delay to prevent CPU hogging
            
            # Get user input for hours, minutes, and seconds
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = float(input("Enter seconds: "))

            total_seconds = (hours * 3600) + (minutes * 60) + seconds  # converts the hours and minutes to seconds and added to seconds
            return_to_menu = countdown_timer(total_seconds)
            if return_to_menu:
                options = input("\nStopwatch     Timer\n\n")  # Show options again
            else:
                break  # Exit the program

        elif options == 'Stopwatch':  # if user types in Stopwatch it runs this code under it
            def format_time(seconds):  # makes it so that the code is readable. HH:MM:SS.ss more presentable
                hours = int(seconds // 3600)  # divdes the seconds by 3600 because that's how many seconds are in an hour.
                                          # // is added to remove any decimals
                minutes = int((seconds % 3600) // 60)  # the % gives you the remainder after dividing by hours then divides
                                                   # by 60 to get the min.
                seconds = seconds % 60  # Remaining seconds
                return f"{hours:02}:{minutes:02}:{seconds:05.2f}"  # Makes sure that we keep hours and minutes to 2 digits
                                                               # and makes seconds have 2 digits with 2 decimals.

            def stopwatch():  # defines the stopwatch function
                print("Press ENTER to start the stopwatch, P to pause, R to resume, and Q to stop.")
                input()  # waits for user input
                print("Stopwatch started...")
                start_time = time.time()  # keeps track of the current time
                running = True
                paused = False
                paused_time = 0
                pause_start = 0

                try:
                    while running:  # lets the code loop until user stops it
                        # Handle pygame events
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p and not paused:  # Pause on 'p' key
                                    paused = True
                                    pause_start = time.time()
                                    print("\nPaused. Press R to resume.")
                                elif event.key == pygame.K_r and paused:  # Resume on 'r' key
                                    paused = False
                                    paused_time += time.time() - pause_start
                                    print("\nResumed.")
                                elif event.key == pygame.K_q:  # Quit on 'q' key
                                    running = False
                        
                        if not paused:
                            elapsed_time = time.time() - start_time - paused_time  # by subtracting the time to the start time we get the elapsed time
                                                                      # how much time that has passed
                            print(f"\rElapsed Time: {format_time(elapsed_time)}", end="")  # prints out the elapsed time in the format
                                                                                      # of HH:MM:SS.ss. \r is used to overwrite the
                                                                                      # previous output to make it look clean
                                                                                      # the end="" prevents automatic new lines
                        
                        time.sleep(0.01)  # adds a delay of 0.01 to display smoothly
                    
                    print("\nStopwatch stopped.")  # prints out after the keyboard interrupts
                    print(f"Total time: {format_time(time.time() - start_time - paused_time)}")  # prints the total time in the format
                    
                except KeyboardInterrupt:  # lets the code stop smoothly instead of the program crashing
                    print("\nStopwatch stopped.")
                    print(f"Total time: {format_time(time.time() - start_time - paused_time)}")
                
                # Ask if user wants to return to main menu
                print("\nPress M to return to main menu or any other key to exit")
                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_m:
                                return True  # Return to main menu
                            else:
                                return False  # Exit program
                    pygame.time.delay(10)  # Small delay to prevent CPU hogging
            
            return_to_menu = stopwatch()
            if return_to_menu:
                options = input("\nStopwatch     Timer\n\n")  # Show options again
            else:
                break  # Exit the program
        
        else:
            print("Invalid option. Please enter 'Stopwatch' or 'Timer'.")
            options = input("\nStopwatch     Timer\n\n")  # gives the user options again

    pygame.quit()  # Clean up pygame when exiting

if __name__ == "__main__":
    main()

def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")


# This code defines a function called countdown that takes in an integer argument called number. 

# Here's what the function does: 
# 1. Starts a while loop: This loop will continue as long as the number argument is greater than 0.
# 2. Prints the current number of seconds: In each iteration of the loop, the function uses print() to output a string that includes the current value of number.
# 3. Decrements number: After printing the number of seconds, the function decrements the number variable by 1.
# 4. Prints "HAPPY NEW YEAR!": After the loop finishes (i.e., when number becomes 0), the function uses print() to output the string "HAPPY NEW YEAR!".


def countdown_with_sleep(number):
    import time
    while number > 0:
        print(f"{number} SECOND(S)!")
        time.sleep(1)
        number -= 1
    print("HAPPY NEW YEAR!")

# This code defines a function called countdown_with_sleep that takes in an integer argument called number. 

# Here's what the function does:
# 1. Imports the time module: This module provides functions for working with time, including a function called sleep() that can be used to pause the program for a specified amount of time.
# 2. Starts a while loop: This loop will continue as long as the number argument is greater than 0.
# 3. Prints the current number of seconds: In each iteration of the loop, the function uses print() to output a string that includes the current value of number.
# 4. Pauses the program for 1 second: After printing the number of seconds, the function calls time.sleep(1), which pauses the program for 1 second before continuing.
# 5. Decrements number: After pausing for 1 second, the function decrements the number variable by 1.
# 6. Prints "HAPPY NEW YEAR!": After the loop finishes, the function uses print() to output the string "HAPPY NEW YEAR!".

# This function is similar to the countdown() function previously defined, with the addition of the time.sleep() function. This function pauses the program for 1 second in each iteration of the loop, which can be useful for creating a more realistic countdown effect.

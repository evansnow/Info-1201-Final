# @ 9:40am: Code is running and executing on the Microbit, however, it fails to record the data
# and I only get the headers appearing in my CSV. I'm guesing this is an issue with the "collect_data" and "main"
# functions and the different tasks they perform. But my code is exactly the same as others, so I don't know
# where my issues lies.
# Citations: Maddie C, Luke N

"""
This code was remixed from
https://microbitmathsblog.wordpress.com/2017/03/01/microbit-data-logging/

Remixed by Riacrose Roque for INFO 1201

Remixed again by <Add your name here>

"""

from microbit import *

# Initialize global variables
log_time = 0
read_interval = 250
filename = "mydata.csv"
#counter = 0

# Load the content in the given filename
# Return a String of all the content from a given file
def read_data(filename):
    with open(filename) as my_file:
        data = my_file.read()
    return str(data)

# Write the given data at the file located at the given filename
def write_data(filename, data):
    with open(filename, 'w') as my_file:
        data = str(data)
        my_file.write(data)

# This function returns a String of comma separated elements based on the
# elements inside the given datalist
def format_data(data_list):
    # return a single String that contains the elements inside datalist
    # elements are converted to Strings and separated by a comma
    # String ends with a \r or a carriage return
    return ",".join(map(str, data_list)) + "\r"

# Set the headers in the file
def write_headers(headers_list):
    headers = ",".join(headers_list) + "\r"
    write_data(filename, headers)

# Collect data using at least one of the input features of micro:bit
# TODO adapt this code to program your micro:bit to collect data
# and write that data into the file in CSV format
def collect_data(Count, SleepTime):
    log_data = read_data(filename)
    log_data = log_data + format_data([Count, SleepTime])

    # write the formatted data to the file
    write_data(filename, log_data)

# main() function
def main():
    Count = 0
    # write in the headers in the file
    write_headers(["Total Count (Click of B)", "Total Minutes Since Flash (Click of A"])
    
    # Left the delay in place. Hsd trouble testing if my microbit was beginning the timer after the countdown, or if it all initaites at once.
    for i in range(10,0,-1):
        display.scroll(str(i))
        display.show("*")
        #X will appear on LED until first set of data is recored
        
    start = running_time()
    Count = 0
    
    #Directions: 1. Flash Microbit and start exercise 
                #2. At Lap 1 > Press B; Then A
                #3. At Lap 2 > Repeat Step 1
                #4. Unload Data (Using Terminal)
                #5. More Data can be captured. For the purposes of (2) 1/2 mi. laps, I will only record (2) laps,
                # totaling (1) mile and timing (1) mile from flash time (running_time()).
   
    while True:
        
        if button_b.is_pressed():
            SleepTime = (running_time() - start)/60000
            #display.show("1")
            Count += button_b.get_presses()
            display.scroll(str(Count))
            #Achieved minutes by diving by 60,000: Divide by 1000 to get seconds, then multiple by 60 seconds to get minutes
            #Count increases by 1, but only gets recored when A is pressed.
            
        if button_a.is_pressed():
            display.scroll(str(Count))
            collect_data(Count, SleepTime)
            
# Start the program by calling the main() function.
main()


# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 1

# input seconds as type string
second = input('Please enter # of seconds: ')
# typecast seconds to integer
s = int(second)

if s >= 0: # if seconds is greater than 0, this is a valid input
    hours = (s // 60) // 60 # calculate hours with integer division
    h = int(hours) # typecast hours to integer for proper conversion
    minutes = (s // 60) % 60 # calculate minutes by dividing by 60 with modulo 60
    m = int(minutes) # typecast minutes to integer for proper conversion
    seconds = (((s % 60) % 60)) % 60 # calculate seconds by dividing by 60 with modulo 60 twice
    s1 = int(seconds) # typecast seconds to integer for proper conversion

    # print result in the terminal
    print(s, 'seconds is ', h, 'hours, ', m, 'minutes, and ', s1, 'seconds.')

else: # if the input is negative
    print('Invalid number') # this is not a valid input

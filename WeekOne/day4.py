import time

#format
#approach 1
# b1 = "bread"
# b2 = "eggs"
# b3 = "ham"
# print(f"For breakfast i had {b1}, {b2}, and {b3}")

#Approach 2
count = 1
program_start = time.time() # there is a 
#class time: with function 
# def time()
# def space()
# so we are inheriting a function time from a class time
while count < 1000:
    now = time.time() #current time stamp
    print(f" It has been {now  - program_start} seconds since the loop started \n ")
    count += 1

#Importance of f, what goes into curly braces is the variable 

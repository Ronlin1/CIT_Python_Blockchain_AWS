# #functions modularize your code

# def greet():
#     print("hello World")
# #you have to call the function for it to work
# greet()     #function call

# # with params
# # initialise first

# a = 2
# b = 1

# def sum(x, y): #takes two parameters x & y
#     res = x + y
#     print(res)

# sum(a, b) #variables as function parameters

# #functions can be re used
# sum (-2, 9) 

# sum('cat ', 'dog') # + concatenates

#function with return
# def sum(x, y): #takes two parameters x & y
#     z = x + y
#     return z # value of the func is z
#     # return has a datatype and value

# result = sum(2, 3) # This is how you access the function returned use!!

# print(result)
#return means passing data, whatever the func does, is stores it in z

#algorithm challenge

# define a max_num function, create a list inside the fun 
# write a for loop / iterate through the list, 
# find the max number

# if l[0] > l[1], print less than, else not greater than
def max_num():
    lis =  [1, 3, 2, 12, 4, 13]
    for i in lis:
        if i > lis[-1]:
            print(i)
    #return fir

max_num()
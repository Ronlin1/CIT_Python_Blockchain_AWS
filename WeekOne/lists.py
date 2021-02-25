# #lists

# '''
# lists can be counted like
# -6 -5 -4 -3 -2 -1 0 1 2 3 4 5
# 0 is the first element
# -1 is the last element
# you can count the list backwards
# '''

#days = ['mon', 'tues', 'wednes', 'thurs', 'fri', 'satur', 'sun']

# #print list
# print(type(days))
# print(days)

# #accessing list elements
# #index start at 0

# monday = days[0]
# wendnesday = days[2] # or wendnesday = days[-1]

# #checking for the length
# print(len(days))

# #iterate thru a list mthd1 to get specific element
# for i in range(len(days)):
#     #print all days
#     print(days[i])

# #iterate thru a list mth2 without indices
# for item in days:
#     print(item+'day')


#print the list backwards method 1
#length = len(days)
# for i in range(length):
#     length -=1
#     print(days[length])


# # second, This one reproduces(traversing) the list in a reverse direction
# for i in range(length):
#     print(days[::-1])
# #['sun', 'satur', 'fri', 'thurs', 'wednes', 'tues', 'mon']
#days = ['mon', 'tues', 'wednes', 'thurs', 'fri', 'satur', 'sun']
# length = len(days)
# while length != 0:
#     length -= 1
#     print(days[length])

#meth 3
days = ['mon', 'tues', 'wednes', 'thurs', 'fri', 'satur', 'sun']
# ddays = days[::-1]
# for item in ddays:
#     print(item)

#meth 3 Best solution
for i in range(len(days)):
    # it starts printing from index 0, so 0-1 = -1
    print(days[-i-1])

#range(start, stop, step) <--takes three parameters
#print(-i-1) works

# documentation for pyhthon lists
# https://docs.python.org/3/tutorial/datastructures.html


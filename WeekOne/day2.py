#string
greeting = "Hello World!"

#integer, whole number
num = 2
#float
dec = 4.5

scinot = 10e-2 #10x10**-2  # push 2 dec places to left
print(scinot)

#float * integer
print (4.5 * 2)

#boolean
t = True
f = False

print(t)
print(f)

#logical operators and conditionals

day =  'Sunny'
month = 4

if day == "Sunny" and month == 4: # for and to run, both conditions have to be true
    print("Sunny in April")

# or - at least one of the conditions has to be true
if  day == "Sunny" or month == 2:
    print("it is Sunny, February, or both!")

    #escaping using backward slash
    print('it\'s Sunny, February, or both!')

#lists and loops
#for loops will execute with a given range, Once
# it begins counting from 0, last value is n-1 where n is the maximum of range
# always  specify the range before and use max + 1
n = 10
for i in range(1, n+1): # has the iterator, range then what to do
    print (i)


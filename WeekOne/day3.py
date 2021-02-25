#todays challenge 1. Challenge: Code the Fibonacci sequence in Python


# escape sequences

# the fibonnacci sequence  previous number plus current
# you need temporally number
# you need for loop

# def fib(nth_term):
#     prev, curr, temp, count, = 0, 1, 0, 0
#     while count < nth_term:
#        print(prev)
#        temp = prev + curr
#        # update values
#        prev = curr
#        curr = temp
#        count += 1
# fib(10)    

#meth2 better
def fib(x):
    a = 0
    b = 1
    for i in range(x):
        temp = a
        a = b
        b = temp + b
        print(a)
fib(10)

#the fractal
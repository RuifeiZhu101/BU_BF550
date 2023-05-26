# Problem 3
# Write a module that contains a function sqrt(y, tol= 1e-6)
# to compute a square root of a number using Heron's algorithm 
# with guaranteed relative error < tol

def sqrt(tol=1e-6):
    #ask user to input a number
    print('This program returns the square root of a number with a relative deviation < 1e-6.')
    y = eval(input('Enter a number to get its suqare root: '))
    if y <= 0:
        print('You must enter a positive number.')
        return    
    else:
        x = y/2 # first guess
        
        while abs(x*x-y) >= tol: #while deviation between x^2 and y greater or equals tol
            x = 0.5*(x+y/x)   #take a new guess 
    print('A close square root for',y,'is',x)
    
sqrt()
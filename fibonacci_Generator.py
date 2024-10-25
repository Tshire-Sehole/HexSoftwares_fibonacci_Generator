# creating a fibonacci function
def fibonacci_funtion (k): 
    f, x = -5, 1
    count = 0  # in order to monitor the quantity of numbers printed
    
    while count < k:
        print(f, end= " ")  # print the current value of f
        f, x = x, f + x  # the following fibonacci figure
        count += 1  # increment the count to control the loop
        
# calling the funtion to call the first 20 fibonacci numbers
fibonacci_funtion(20)
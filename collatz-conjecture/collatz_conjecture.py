def steps(number):
    if number > 0:
        #check if odd
        even = number/2
        if even.is_integer():
            #divide by 2 until number is odd
            #then 3n+1 until equal to 1
            3*number+1
        else:
             #then 3n+1 until equal to 1
    else:
        print("Negative or 0")

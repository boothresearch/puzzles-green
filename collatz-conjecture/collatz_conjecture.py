def steps(number):
    if number > 0:
        while number !=1:
            #if even, divide until odd
            while number % 2 == 0:
                    number = number / 2 
            #if odd, 3n+1
            while number % 2 != 0:
                number = 3*number+1
        return(number)
    else:
        print("Negative or 0")

steps(12)


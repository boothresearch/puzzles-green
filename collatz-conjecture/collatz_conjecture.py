def steps(number):
    count = 0
    if number > 0:
        while number !=1:
            #if even, divide until odd
            while number % 2 == 0:
                    number = number / 2 
                    count +=1
            #if odd, 3n+1
            while number % 2 != 0 and number !=1:
                number = 3*number+1
                count +=1
        return(count)
    else:
        raise ValueError("This is a 0 or negative number")


def leap_year(year):
    hun = year/100
    fhun = year/400
    four = year/4
    if four.is_integer():
        if fhun.is_integer():
            return(True)
        if hun.is_integer():
            return(False)
        else:
            return(True)
    else:
        return(False)
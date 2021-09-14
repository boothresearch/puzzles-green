def leap_year(year):
    hun = year/100
    fhun = year/400
    four = year/4
    print(four.is_integer() and (not hun.is_integer() and fhun.is_integer()))

leap_year(2100)
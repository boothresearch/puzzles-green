def score(word):
    word_upper=word.upper()

    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    for i in word_upper:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='L' or i=='N' or i=='R' or i=='S' or i=='T':
            count1=count1+1
        elif i=='D' or i=='G':
            count2=count2+1
        elif i=='B' or i=='C' or i=='M' or i=='P':
            count3=count3+1
        elif i=='F' or i=='H' or i=='V' or i=='W' or i=='Y':
            count4=count4+1
        elif i=='K':
            count5=count5+1
        elif i=='J' or i=='X':
            count6=count6+1
        elif i=='Q' or i=='Z':
            count7=count7+1
    value=1*count1+2*count2+3*count3+4*count4+5*count5+8*count6+10*count7

    return value
 
       
   

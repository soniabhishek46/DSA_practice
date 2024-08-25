def count_no_of_digits(num: int):
    '''
    num=1234
    dig=num%10
    num=num//10
    '''
    count=0
    while num > 0:
        dig=num%10
        num=num//10
        count+=1    
    print(count)

count_no_of_digits(123456)

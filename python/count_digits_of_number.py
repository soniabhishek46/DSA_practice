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

#-------------------------
# Other way of doing this
#-------------------------
import math

#Count number of digits in a number
def count_num_of_digits(num: int):
  return round(math.log(num, 10))

print(count_num_of_digits(45345678901))

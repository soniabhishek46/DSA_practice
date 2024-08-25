mport math

#Count number of digits in a number
def count_digits(num: int):
  cnt=0
  while num > 0:
    num=num//10
    cnt+=1
  return cnt

def check_if_num_is_armstrong(num: int):
  num_dig = count_digits(num)
  print(num_dig)
  com_num = 0
  giv_num = num
  digits = []
  while num > 0:
    dig = num%10
    num = num//10
    digits.insert(0, dig)

  for v in digits:
    com_num += (v**num_dig)
    print(v, com_num)
  
  print(f'{giv_num}|{com_num}')
  
  if giv_num == com_num:
    return True
  return False

print(check_if_num_is_armstrong(153))

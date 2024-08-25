#Reverse a number
def reverse_a_number(num: int):
  res=0
  while num > 0:
    dig=num%10
    res = (res*10)+dig
    num=num//10
  return res

print(reverse_a_number(12345))

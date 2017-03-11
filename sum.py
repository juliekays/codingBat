"""Given 2 ints, a and b, return their sum. However, sums in the range 
10..19 inclusive, are forbidden, so in that case just return 20."""

def sorta_sum(a, b):
 #if (a+b)>=10 and (a+b)<=19:
  if (a+b) in range(10,20):  
    return 20
  else:
    return (a+b)
print sorta_sum(5,7)
print sorta_sum(5,3)
print sorta_sum(5,12)
print sorta_sum(20,3)    

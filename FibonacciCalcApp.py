#40 days of coding
#November 13th 2021
#Loops Challenge 14: Fibonacci Calculator App

import cmath

#Print Welcome INformation
print("Wlecome to the fibonacci Calculator App")

num=int(input("How many digits off the fibonacci sequence would you like to compute: "))

#Compute the values of the fib
fib = [1,1]
for i in range(num-1):
  new_fib=fib[i] + fib[i+1]
  fib.append(new_fib)

#Display the fib values
print("\nThe first " + str(num) + " numbers of the Fibonacci Sequence are: ")
for number in fib:
  print(number)

#Compute the golden ratio 
golden=[]
for i in range(len(fib)-1):
   ratio = fib[i+1]/fib[i]
   golden.append(ratio)

#Display the ratios
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
  print(ratio)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number=int(input("Enter number to check whether the no. is prime or not"))
if number>1:
    for each in range(2,number):  #takes till number -1
        if (number%each)==0:
            print (number," is not a prime number") #because prime number is only divided by 1 and the number itself
            break
    else:
        print (number," is a prime number")
else:
    print (number," is not a prime number")#for number <=1


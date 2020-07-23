#!/usr/bin/env python
# coding: utf-8

# In[36]:


string="Hi! This is a history relating to him"
substring=input("Enter the substring: ")
a=0
for each in range(len(string)):
    
    if(string[each:each+len(substring)] == substring):
        print("\nThe substring",substring," is present at:")
        print(each,end=" ")
        a=1
if(a==0):
    print("The substring is not present in main string.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





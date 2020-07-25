#!/usr/bin/env python
# coding: utf-8

# In[19]:


list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list2=[]
for each in list1:
    if each==0:
        list2.append(each)
        list1.remove(each)
list1.sort()
list1+=list2
list1


# In[ ]:





# In[ ]:





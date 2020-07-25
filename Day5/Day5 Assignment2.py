#!/usr/bin/env python
# coding: utf-8

# In[7]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
sortedlist=[]
i=0
j=0
while i<len(list1)and j<len(list2):
    if list1[i]<list2[j]:
        sortedlist.append(list1[i])
        i+=1
    else:
        sortedlist.append(list2[j])
        j+=1
print(i,j)
print(sortedlist+list1[i:]+list2[j:])


# In[ ]:





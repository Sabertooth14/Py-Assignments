#!/usr/bin/env python
# coding: utf-8

# In[4]:


def vol(rad):
    radius= (4/3)*(rad**3)*(3.14)
    return radius


# In[5]:


vol(4)


# In[6]:


vol(5)


# In[17]:


def run_check(num,low,high):
    if(num in range(low,high+1)):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print("No it's not")


# In[18]:


run_check(5,2,7)


# In[19]:


run_check(2,2,7)


# In[20]:


run_check(7,2,7)


# In[32]:


def up_low(s):
    count_up=0
    count_low=0
    for c in s:
        if(c.isupper()):
            count_up+=1
        elif(c.islower()):
            count_low+=1
    print(s)
    print(f"No. of Upper case characters :  {count_up}")
    print(f"No. of Lower case Characters :  {count_low}")


# In[33]:


s='Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# In[44]:


def unique_list(mylsit):
    new_list=[]
    for n in mylsit:
        if n not in new_list:
            new_list.append(n)
        
    return new_list


# In[45]:


unique_list([1,3,4,4,5])


# In[53]:


def multiply(nums):
    total=1
    for n in nums:
        total*=n
    return total


# In[54]:


multiply([1, 2, 3, -4])


# In[55]:


multiply([3,5,1,-6])


# In[59]:


def palindrome(s):
    if(s[::-1]==s):
        return True
    else: return False


# In[60]:


s="helleh"
palindrome(s)


# In[5]:


import string

def ispangram(mystr,alpha=string.ascii_lowercase):
    alphabet=set(alpha)
    mystr=mystr.replace(" ","")
    mystr=mystr.lower()
    mystr=set(mystr)
    return mystr==alphabet


# In[6]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[7]:


string.ascii_lowercase


# In[8]:


string.ascii_uppercase


# In[9]:


string.ascii_letters


# In[ ]:





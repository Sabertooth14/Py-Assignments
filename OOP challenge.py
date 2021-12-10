#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Account():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance} rupees")
              
    def deposit(self,addamt):
        
        self.balance = self.balance + addamt
        print("{} amount has been deposited".format(addamt))
        return ("New balance = {}".format(self.balance))
    
    def withdarw(self,subamt):
        
        if (subamt<self.balance):
            self.balance = self.balance - subamt
            print("{} amount has been withdrawn".format(subamt))
            return ("New balance = {}".format(self.balance))
        else:
            print("Funds Unavailable")
            
    


# In[20]:


acct1=Account("Pranav",400)


# In[21]:


acct1.owner


# In[22]:


acct1.balance


# In[23]:


acct1.deposit(300)


# In[24]:


acct1.withdarw(1000)


# In[25]:


acct1.withdarw(600)


# In[26]:


str(acct1)


# In[ ]:





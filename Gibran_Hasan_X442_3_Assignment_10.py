#!/usr/bin/env python
# coding: utf-8

# 1. Write a simple Rectangle class. It should do the following:
# 
# Accepts length and width as parameters when creating a new instance
# Has a perimeter method that returns the perimeter of the rectangle
# Has an area method that returns the area of the rectangle
# Don't worry about coordinates or negative values, etc.

# In[1]:


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

 
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width
      
    def get_perimeter(self):
        return 2 *(self.length + self.width)

    def __str__(self):
        return 'length = {}, width = {}'.format(self.length, self.width)


# In[ ]:


rec= Rectangle(5,5)


# In[ ]:


print rec


# In[ ]:


print rec.length


# In[ ]:


rec.set_length(6)


# In[ ]:


rec.get_area()


# In[ ]:


rec.get_perimeter()


# Python provides several modules to allow you to easily extend some of the basic objects in the language. Among these modules are UserDict, UserList, and UserString. (Refer to the chart in Topic 10.3 to see what the methods you need to override look like. Also, since UserDict and UserList are part of the collection module, you can import them using from collections import UserDict and from collections import UserList.)
# 
# 2. Using the UserList module, create a class called Ulist, and override the __add__, append, and extend methods so that duplicate values will not be added to the list by any of these operations.
# 
# 3. (Extra Credit) Using the UserDict module, create a class called Odict, which will be just like a dictionary but will "remember" the order in which key/value pairs are added to the dictionary. (Hint: Override the built-in __setitem__ method.) Create a new method for the Odict object called okeys, which will return the ordered keys.

# In[4]:


import UserDict
import UserList


# In[ ]:


class Ulist(UserList.UserList):
    def __init__(self, data = [], **kw):
        UserList.UserList.__init__(self)
        self.data = data

    def __add__(self, vals):
        for num in vals:
            if num in self.data:
                print "%r Sorry no duplicates allowed." % num
            else:
                self.data += [num]
        return self.data

    def append(self,vals = None):
        if vals in self.data:
            print "%r Sorry no duplicates allowed." % vals
        else:
            return self.data.append(vals)

    def extend(self, vals = []):
        for num in vals:
            if num in self.data:
                print "%r Sorry no duplicates allowed." % num
            else:
                return self.data.extend(num)
        return self.data

try_list = Ulist([1,2,3])


# In[20]:


try_list


# In[21]:


try_list.__add__([5,6,1])


# In[ ]:





# In[2]:


class Odict(UserDict.UserDict):
    def __init__(self, data = {}, **kw):
        UserDict.UserDict.__init__(self)
        self.update(data)
        self.update(kw)
        self.keylist = []

    def __setitem__(self,key,value):
        self.data[key] = value
        self.keylist.append(key)

    def okeys(self):
        return self.keylist


od = Odict()
od['a'] = '27'
od['d'] = '2'
od['i'] = '22'


# In[32]:


od


# In[33]:


od.okeys()


# In[ ]:





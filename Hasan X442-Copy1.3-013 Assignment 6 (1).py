
# coding: utf-8

# # 1.

# In[2]:


file = 'file.txt'
file


# In[3]:


def counting(file):
    try: 
        f = open(file, 'r') 
    except IOError: 
        print("Unable to open", file ,"for reading")

    line = f.readlines()
    f.close()
    words = 0
    lettercounts = 0
    linecounts = 0
    for word in line:
        linecounts += 1
        lettercounts += len(word)
        words += len(word.split())
        
    return linecounts, lettercounts, words

counting(file)


# # 2.

# In[59]:


every = []
i=0
for item in lit:
    i+=1
    for i in item:
        every.append(i)
        t= list(set(every))
print(t)


# In[98]:


def strip(*args):
    i=0
    every= []
    for item in args:
        i+=1
        for i in item:
            every.append(i)
            t= list(set([every]))
            return t
    


# In[100]:


def strip(*args):
    every= list(set())
    for item in args:
        every+=item
    return list(set(every))


# In[101]:


strip([1,2,3,3,4,1], [6,6,6,9], [1,1,6,0,7,8812,9])


# # 3

# In[211]:


#Use the map function to add a constant to each element of a list.
#Perform the same operation using a list comprehension. 

#For example, the list (1, 20, 300, 400) and constant 8, will result in: 9, 28, 308, 408


# In[244]:


def add(item):
    d=[]
    for x in item:
        d.append(x+8)
    return d
        
add([1,2,3])


# In[241]:


def add(x):
    return x + 8


# In[243]:


h = [2,4,6,7]
list(map(add, h))


# In[246]:



[x + 8 for x in h]


# # 4.

# In[ ]:


Write a function that will take a variable number of lists. Each list can contain any number of words. 
This function should return a dictionary where the words are the keys and 
the values are the total count of each word in all of the lists

For example, if we are given the following lists:

wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

the function should output the following dictionary (The order of the words is not important):
{'float': 1, 'int': 2, 'quadruple': 1, 'home run': 1, 'triple': 1, 'double': 3}

Note, you may have to create an empty dictionary first (for example: dict = {}).


# In[77]:


a = ["double", "triple", "int", "quadruple"]
b = ["double", "home run"]
c = ["int", "double", "float"]


# In[52]:


dicy= {}
for word in w:
    if word in dicy: 
        dicy[word]+=1
    else:
        dicy[word]=1
print(dicy)


# In[236]:


def diction(*args):
    new= []
    for word in args:
        new += word
        dicy={}
        for item in new:
            if item in dicy:
                dicy[item]+=1
            else:
                dicy[item]=1
    print(dicy)
            
            


# In[237]:


diction(a,b,c)


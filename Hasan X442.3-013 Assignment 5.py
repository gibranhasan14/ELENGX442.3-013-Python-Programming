
# coding: utf-8

# # Hasan X442.3 Assignment 5

# # Question 1

# In[ ]:


#Using the keys method for dictionaries and the sort method for lists, write a for loop 
#that prints the keys and corresponding values of a dictionary in the alphabetical order of the keys


# In[25]:


dicty = {'a': 10, 't': 11, 'f': 1, 'z':5, 'q':2, 'b':20}

for i,k in dicty.items():
    new=sorted(dicty.items())
print(new)


# In[20]:


dicty.items()


# # Question 2. 

# In[ ]:


#As an alternative to the range function, some programmers like to increment a counter inside a while loop 
#and stop the while loop when the counter is no longer less than the length of the array. 
#Rewrite the following code using a while loop instead of a for loop.


# In[ ]:


a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [] 
for i in range(len(a)): 
    big.append(max(a[i],b[i]))


# In[9]:


a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [] 
t = -1
while t < len(a):
    t+=1
    if t >= len(a):
        break
    big.append(max(a[t],b[t]))


# In[10]:


big


# In[6]:


a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big2 = [] 
t = -1
while True:
    t+=1
    if t >= len(a):
        break
    big2.append(max(a[t],b[t]))


# In[7]:


big2


# # Question 3

# In[101]:


#Write a loop that reads each line of a file and counts the number of lines that are read until
 #the total length of the lines is 1,000 or more characters. Use a break statement to make sure that 
 #you don't continue reading the file once at least 1,000 characters are read.



# In[221]:


try: 
    f = open(file, 'r') 

except IOError: 
    print("Unable to open", file ,"for reading")

line = f.readlines()
#f.close()

lettercounts = 0
linecounts = 0
for word in line:
    linecounts += 1
    lettercounts += len(word)
    if lettercounts >= 1000:
        break

print("Number of lines =", linecounts, "Number of characters =" ,lettercounts)


# In[222]:


lettercounts = 0
linecounts = 0
for word in line:
    linecounts += 1
    lettercounts += len(word)
print(linecounts, lettercounts)


# # Question 4

# In[223]:


#Modify the program written in question 3 so that it doesn't count 
#characters on any line that begins with a pound sign (#).


# In[225]:


try: 
    f = open(file, 'r') 

except IOError: 
    print("Unable to open", file ,"for reading")

line = f.readlines()
f.close()

lettercounts = 0
linecounts = 0
for word in line:
    if '#' not in word[0]:
        linecounts += 1
        lettercounts += len(word)    
    if lettercounts >= 1000:
        break

print("Number of lines =", linecounts, "Number of characters =" ,lettercounts)


# In[213]:


for word in line:
    print(word[0])


# In[226]:


for word in line:
    if '#' not in word[0]:
        print(word[0])


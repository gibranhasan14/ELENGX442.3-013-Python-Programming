
# coding: utf-8

# In[ ]:


# Suppose you want to determine whether an arbitrary text string can be converted to a number. 
# Write a function that uses a try/except clause to solve this problem. Can you think of another way to solve this problem?
# The input function will read a single line of text from the terminal. 
# If you wanted to read several lines of text, you could embed this function inside a while loop and terminate the loop 
# when the user of the program presses the interrupt key (Ctrl-C under UNIX, Linux and Windows.) Write such a program, 
# and note its behavior when it receives the interrupt signal. Use a try/except clause to make the program behave more gracefully.

#1. First Method
def convert(string):
    try:
        int(text_string)
    
    except ValueError:
        print('Sorry this text string cannot be converted to a number')
    
    
    #else:

text_string = '669t'

convert(text_string)

#1. Method two
import re
def convert2(string):
    try:
        int(string)
    
    except ValueError:
        print('You entered an invalid text string but I corrected it anyway')
        
    finally:
        result = re.sub('[^0-9]','', string)
        return int(result)
        
        

text_string2= '891uu'
convert2(text_string2)


# In[70]:


def disgracefulexit():
    while True:
        text = input("Feed me more!")
        print (text)
        


# In[71]:


disgracefulexit()


# In[66]:


#2.
def gracefulexit():
    while True:
        try:
            text = input("Feed me more! or ctl+c to stop")
            print (text)
        except KeyboardInterrupt:
            print("You hit ctrl+C! BYE!")
            break


# In[67]:


gracefulexit()


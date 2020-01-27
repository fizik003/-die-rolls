#!/usr/bin/env python
# coding: utf-8

# In[53]:


from random import randint
import pygal


# In[41]:


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)


# In[70]:


die_1 = Die()
die_2 = Die(10)


# In[71]:


results = []
for roll_num in range (50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# In[72]:


frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# In[73]:


hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = [ str(i) for i in range (2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')


# In[ ]:





# In[ ]:





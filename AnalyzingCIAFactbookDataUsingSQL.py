#!/usr/bin/env python
# coding: utf-8

# Introduction

# In[10]:


get_ipython().system('conda install -yc conda-forge ipython-sql')


# In[14]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# Getting an idea of what the data looks like

# In[15]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\n  FROM facts\n LIMIT 5;')


# Here are the descriptions for some of the columns:
# 
# name - The name of the country.
# area - The total land and sea area of the country.
# population - The country's population.
# population_growth- The country's population growth as a percentage.
# birth_rate - The country's birth rate, or the number of births a year per 1,000 people.
# death_rate - The country's death rate, or the number of death a year per 1,000 people.
# area- The country's total area (both land and water).
# area_land - The country's land area in square kilometers.
# area_water - The country's waterarea in square kilometers.
# Let's start by calculating some summary statistics and see what they tell us.

# In[ ]:


Calculating Summary Statistics


# In[17]:


get_ipython().run_cell_magic('sql', '', 'SELECT MIN(population), \n        MAX(population), \n        MIN(population_growth), \n        MAX(population_growth)\n    FROM facts;')


# In[18]:


get_ipython().run_cell_magic('sql', '', 'SELECT name,  \n        MIN(population)\n        FROM facts;\n    ')


# In[19]:



get_ipython().run_cell_magic('sql', '', 'SELECT name,  \n        MAX(population)\n        FROM facts;        ')


# In[21]:



get_ipython().run_cell_magic('sql', '', "SELECT MIN(population), \n        MAX(population), \n        MIN(population_growth), \n        MAX(population_growth)\n    FROM facts\nWHERE name <> 'World';")


# Finding the countries with the minimum population

# In[24]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\n  FROM facts\n WHERE population == (SELECT MIN(population)\n                        FROM facts\n                     );')


# Finding the countries with the max population

# In[25]:



get_ipython().run_cell_magic('sql', '', 'SELECT *\n  FROM facts\n WHERE population == (SELECT MAX(population)\n                        FROM facts\n                     );')


# The table contains a row for the World, which has the highest population. 
# 
# It also seems like the table contains a row for Antarctica, which explains the population of 0. 
# 
# Let's recalculate the summary statistics excluding the row for the whole world.

# In[28]:


get_ipython().run_cell_magic('sql', '', "SELECT MIN(population) AS min_pop,\n       MAX(population) AS max_pop,\n       MIN(population_growth) AS min_pop_growth,\n       MAX(population_growth) AS max_pop_growth \n  FROM facts\n WHERE name <> 'World';")


# In[27]:



get_ipython().run_cell_magic('sql', '', "SELECT AVG(population),\n    AVG(area)\nFROM facts\nWHERE name <> 'World';")


# Let's find densely populated countires that have the following:
# 
# Above-average values for population.
# Below-average values for area.

# In[29]:


get_ipython().run_cell_magic('sql', '', "SELECT *\n  FROM facts\n WHERE population > (SELECT AVG(population)\n                       FROM facts\n                      WHERE name <> 'World'\n                    )\n   AND area < (SELECT AVG(area)\n                 FROM facts\n                WHERE name <> 'World'\n);")


# 

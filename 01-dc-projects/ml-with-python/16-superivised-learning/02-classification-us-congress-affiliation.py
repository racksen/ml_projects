
# coding: utf-8

# # US Congressmen Party Affiliation
# 
# ## Process
# 1. Business Requirements 
# 2. Data Prep
# 3. Spot Check Algorithms
# 4. Improve Results
# 5. Finalize Project
# 

# ## 1). Business Requirements
# 
# The goal of this project is to predict their party affiliation ('Democrat' or 'Republican') based on how they voted on certain key issues. 
# 
# We'll be working with a dataset obtained from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records) consisting of votes made by US House of Representatives Congressmen. 
# 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Pretty print
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


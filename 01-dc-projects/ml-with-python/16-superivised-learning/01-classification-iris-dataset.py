
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Pretty print
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[3]:


import sklearn.datasets as ds


# In[4]:


# Load Iris dataset BUNCH dictionary
ds_iris = ds.load_iris()

#print keys and its types of the iris bunch
["{0} : {1}".format(k,type(ds_iris[k])) for k in ds_iris.keys()]


# ## EDA

# In[5]:


# assign Features and Target variables as X, y
X, y = ds_iris.data, ds_iris.target

# create panda dataframe
df_iris = pd.DataFrame(X, y, columns=ds_iris.feature_names)

#print the head of df
print(df_iris.head() , '\n')

#print the shape
print('df_iris.shape:', df_iris.shape)


# In[6]:


# Numerical EDA - by describing it
df_iris.describe()


# In[7]:


## Draw box plot to see outliers
df_iris.boxplot(column=ds_iris.feature_names, rot=30)


# In[8]:


# Visual EDA

_ = pd.scatter_matrix(df_iris, c=y, figsize=[10,10], marker='D', s=150)


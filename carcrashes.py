#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset('car_crashes')
df


# In[5]:


sns.lineplot(x='total',y='alcohol',data=df)


# In[30]:


sns.scatterplot(x='total',y='ins_losses',data=df,hue="ins_losses")
plt.title('Car crashes',font='Times New Roman')


# In[13]:


import plotly.express as px
fig=px.scatter(df,x='total',y='ins_losses',color='ins_losses')
fig.show()


# In[59]:


import plotly.express as px
fig=px.histogram(df,x='total',y='alcohol',color='abbrev',marginal='rug',color_discrete_sequence=["black","red","blue",'green','pink','yellow','orange','grey','brown','aqua','springgreen'],hover_data='abbrev')
fig.show()


# In[45]:


df.describe()


# In[67]:


import plotly.express as px
fig=px.scatter(df,x='total',y='alcohol',color='abbrev',color_discrete_sequence=["black","red","blue",'green','pink','yellow','orange','grey','brown','aqua','springgreen'],hover_data='abbrev')
fig.show()


# In[ ]:





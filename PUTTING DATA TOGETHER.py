#!/usr/bin/env python
# coding: utf-8

# DATA TRANSFORMATION
# 

# REMOVING UNWANTED DATA AND DUPLICATE

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


myframe5= pd.DataFrame({'student name':['Imoh', 'James', 'Daniel', 'Edidiong'],
                        'sex':['F', 'M', 'M', 'F'],
                        'Age':[10, 15, 14, 17],
                        'School':['primary','high','high','university']})
#we use the Del command to remove an unwanted column,
#we use the drop() to remove an unuwanted row
myframe5


# In[ ]:


##suppose we want to drop row index 1


# In[4]:


myframe5.drop(1)


# In[6]:


myframe5.drop(0)


# In[ ]:


##suppose we want to delete column


# In[9]:


del myframe5['sex']
myframe5


# In[15]:


myframe5= pd.DataFrame({'student name':['Imoh', 'James', 'Daniel', 'Edidiong'],
                        'sex':['F', 'M', 'M', 'F'],
                        'Age':[10, 15, 14, 17],
                        'School':['primary','high','high','university']})


# In[16]:


del myframe5['School']
myframe5


# In[6]:


import pandas as pd


# DELETING DUPLICATES

# To detect duplicates, we use the duplicated() function

# In[7]:


item_frame= pd.DataFrame({'items':['Ball','Bat','Hockey','football','Ball'],
          'colours':['White','Gray','White','Red','White'],
          'Price':[100,500,700,200,100]})
item_frame


# In[8]:


item_frame.duplicated()


# To display the duplicated entry(ies), we can use the item_frame.duplicated() fubction as the index to the DataFrame item_frame.

# In[9]:


item_frame[item_frame.duplicated()]


# We want to remove the duplicate entry

# In[10]:


item_frame.drop_duplicates()


# In[11]:


item_frame= pd.DataFrame({'items':['Ball','Bat','Hockey','football','Ball'],
          'colours':['White','Gray','White','Red','White'],
          'Price':[100,500,700,200,100]})
item_frame


# #HANDLING OUTLIERS

# In[12]:


student_frame= pd.DataFrame({'student name':['Imoh', 'James', 'Daniel', 'Edidiong', 'Isidore','Grace', 'saviour', 'Lawerence'],
                        'sex':['F', 'M', 'M', 'F','F', 'F','M','M'],
                        'Age':[10, 15, 14, 17, 70, 12,13,15],
                        'School':['primary','high','high','university','high','primary', 'high', 'high']})
student_frame


# In[13]:


student_frame.describe()


# DETERMINING THE OUTLIER

# In[14]:


Q1= student_frame.quantile(0.25)
Q3= student_frame.quantile(0.75)
IQR= Q3-Q1
IQR
#obtain interquartile range multiplier
IQR_Mul= IQR*1.5
IQR_Mul
#obtain your lower limit
lower= Q1-IQR_Mul
lower
upper= Q3+IQR_Mul
print('the lower limit is=', lower)
print('the upper limit is=', upper)


# Next after filtering the outlier present in your student_frame dataset, we pass in some codes to updayes the table with the following lines of code.

# In[15]:


student_frame= student_frame[student_frame['Age']>int(lower)]
student_frame= student_frame[student_frame['Age']<int(upper)]
student_frame


# HANDLING MISSING OR INVALID DATA

# ##There are basically three(3) things we can do regarding missing or invalid data.
# 1) Ignore, fill-in#remove or drop.
# 
# to illustrate;

# In[28]:


myseries6= pd.Series([10,20,30,None,40,50,np.NaN], index=[0,1,2,3,4,5,6])
print (myseries6.isnull())
myseries6


# In[29]:


myseries6= pd.Series([10,20,30,None,40,50,np.NaN], index=[0,1,2,3,4,5,6])
#print (myseries6.isnull())
myseries6


# 
# 
# 
# To show the indices containing the missing values

# In[31]:


myseries6[myseries6.isnull()]


# In[32]:


##next we can decide to drop the missing values thus;


# In[33]:


myseries6_dropped= myseries6.dropna()
myseries6_dropped


# DATA INPUTATION
# This is the process in which values are filled-in in a given dataset

# In[34]:


myseries6_filled= myseries6.fillna(myseries6.mean())
myseries6_filled


# In[39]:


myseries6_filled2 = myseries6.fillna(myseries6.median())
myseries6_filled2


# In[ ]:





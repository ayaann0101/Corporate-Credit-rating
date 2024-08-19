#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sklearn
import numpy as np


# In[3]:


df = pd.read_csv("corporate_rating.csv")


# In[4]:


# Class distribution
df['Rating'].value_counts()


# ### AAA : Extremely strong capacity to meet financial commitments. Highest rating. -7
# 
# ### AA :Very strong capacity to meet financial commitments. -89
# 
# ### A :Strong capacity to meet financial commitments, but somewhat susceptible to adverse economic conditions and changes in circumstances. -398
# 
# AAA+AA+A = Grade A = 494
# 
# ### BBB : Adequate capacity to meet financial commitments, but more subject to adverse economic conditions. 671
# 
# BBB - 671
# 
# ### BBB- : Considered lowest investment-grade by market participants. General Summary of the Opinions Reflected by Our Ratings Speculative Grade
# 
# ### BB+ : Considered highest speculative-grade by market participants.
# 
# ### BB : Less vulnerable in the near-term but faces major ongoing uncertainties to adverse business, financial and economic conditions. 490
# 
# BB - 490
# 
# ### B : More vulnerable to adverse business, financial and economic conditions but currently has the capacity to meet financial commitments. 302
# 
# ### CCC :Currently vulnerable and dependent on favorable business, financial and economic conditions to meet financial commitments. 64
# 
# ### CC :Highly vulnerable; default has not yet occurred, but is expected to be a virtual certainty. 5
# 
# ### C :Currently highly vulnerable to non-payment, and ultimate recovery is expected to be lower than that of higher rated obligations. 2
# 
# ### D :Payment default on a financial commitment or breach of an imputed promise; also used when a bankruptcy petition has been filed or similar action taken 1
# 
# B+CCC+CC+C+D = Speculative grade = 374

# In[16]:


new_labels = {"AAA":"Grade A","AA":"Grade A","A":"Grade A", "BBB":"TripleB","BB":"DoubleB", "B":"Speculative Grade"
               ,"CCC":"Speculative Grade","CC":"Speculative Grade","C":"Speculative Grade","D":"Speculative Grade"}
df['new_rating']= df['Rating'].map(new_labels)                                                                                            


# In[18]:


df.head(10)
df['new_rating'].value_counts()


# # FINAL DATASET

# In[9]:


import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("corporate_rating.csv")


# In[3]:


new_labels = {"AAA":"Grade A","AA":"Grade A","A":"Grade A", "BBB":"Grade B","BB":"Grade B", "B":"Grade B"
               ,"CCC":"Grade C","CC":"Grade C","C":"Grade C","D":"Grade C"}
df['new_rating']= df['Rating'].map(new_labels)                                                                                            


# In[4]:


df['new_rating'].value_counts()


# In[10]:


rating_counts = df['new_rating'].value_counts()

# Create a horizontal bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='viridis')
plt.xlabel('Distribution of Ratings')
plt.ylabel('Ratings')
plt.title('Horizontal Bar Plot of Rating Counts')
plt.show()


# In[11]:


df.describe()


# In[13]:


df.columns


# ### No missing value

# In[14]:


# contingency table
contingency_table = pd.crosstab(df['new_rating'], df['Sector'])


# In[16]:


plt.figure(figsize=(8,4))
sns.heatmap(contingency_table, annot=True, cmap='viridis', fmt='d')
plt.xlabel('Sector')
plt.ylabel('Ratings')
plt.title('Heatmap of Ratings by Sector')
plt.show()


# In[17]:


normalized_contingency_table = contingency_table.div(contingency_table.sum(axis=1), axis=0)

# Plot heatmap of normalized contingency table
plt.figure(figsize=(10, 7))
sns.heatmap(normalized_contingency_table, annot=True, cmap='YlGnBu', fmt='.2f')
plt.xlabel('Sector')
plt.ylabel('Ratings')
plt.title('Heatmap of Normalized Ratings by Sector')
plt.show()


# Liquidity Measurement Ratios: currentRatio, quickRatio, cashRatio, daysOfSalesOutstanding 
# 
# Profitability Indicator Ratios: grossProfitMargin, operatingProfitMargin, pretaxProfitMargin, netProfitMargin, effectiveTaxRate, returnOnAssets, returnOnEquity, returnOnCapitalEmployed
# 
# Debt Ratios: debtRatio, debtEquityRatio
# 
# Operating Performance Ratios:`assetTurnover
# 
# Cash Flow Indicator Ratios: operatingCashFlowPerShare, freeCashFlowPerShare, cashPerShare, operatingCashFlowSalesRatio, freeCashFlowOperatingCashFlowRatio
# 

# In[20]:


correlation_matrix=df.corr()
plt.figure(figsize=(20, 12))

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Add a title to the heatmap
plt.title('Correlation Matrix Heatmap')

# Display the heatmap
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





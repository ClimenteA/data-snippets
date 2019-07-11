#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
from docx.api import Document


# In[2]:


def convertTabletoDf(table):
    data = []
    keys = None
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)

        if i == 0:
            keys = tuple(text)
            continue
        row_data = dict(zip(keys, text))
        data.append(row_data)

    df = pd.DataFrame(data)
    return df


# In[3]:


folder = "LCS softcopy docx"
docxfiles = os.listdir(folder)
docxfilespath = [os.path.join(folder, docx) for docx in docxfiles]
docxfilespath[0:3]


# In[4]:


try:
    os.mkdir("XLSX")
except:
    pass


# In[7]:


for docname, docpath in zip(docxfiles, docxfilespath):
    document = Document(docpath)
    tables = document.tables
    for i, table in enumerate(tables):
        try:
            df = convertTabletoDf(table)
            xlname = "XLSX/{}".format(docname[0:-4] + "_" + str(i+1) + ".xlsx")
            df.to_excel(xlname, index=False)
        except Exception as e:
            print(xlname, e)


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





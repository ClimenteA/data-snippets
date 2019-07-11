#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Move the docx files from step one to DOCX folder


# In[2]:


import os


# In[3]:


try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile


# In[4]:


"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)


# In[5]:


def getAMSli(text):
    """Get a list of AMS from the text string given"""
    
    pattern = "(?s)(?<=AMS).*?(?=[])"
    raw_amsli = re.findall(pattern, text)

    all_amsli = []
    for raw_ams in raw_amsli:
        amsli = cleanAMS(raw_ams)
        all_amsli.append(amsli)

    all_amsli = list(set(itertools.chain(*all_amsli)))

    amsli = removeWords(all_amsli)
    return amsli


# In[6]:


files = os.listdir("DOCX")
files_path = [os.path.join("DOCX", f) for f in files]


# In[7]:


#Convert docx to txt
for i, fpath in enumerate(files_path):
    raw_text = get_docx_text(fpath)
    text = raw_text.encode(encoding='UTF-8',errors='strict')
    txtf = open('{}.txt'.format(fpath), 'w')
    with txtf:
        txtf.write(str(text))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





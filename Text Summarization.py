#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install PyPDF2 spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[1]:


import PyPDF2
import spacy


# In[2]:


pdf_file_path = "C:/Users/HP/Downloads/Operations Management.pdf"
pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

extracted_text = ""
for page in pdf_reader.pages:
    extracted_text += page.extract_text()

pdf_file.close()


# In[3]:


nlp = spacy.load('en_core_web_sm')


# In[4]:


doc = nlp(extracted_text)


# In[5]:


sentences = [sent.text for sent in doc.sents]


# In[6]:


desired_summary_length = 500
total_words = 0
summary_sentences = []


# In[7]:


for sentence in sentences:
    if total_words < desired_summary_length:
        summary_sentences.append(sentence)
        total_words += len(sentence.split())


# In[8]:


summary = ' '.join(summary_sentences)
print("Summary:\n")
print(summary)


# In[9]:


if summary:
    print("Summary:")
    print(summary)
else:
    print("No summary could be generated.")


# In[ ]:





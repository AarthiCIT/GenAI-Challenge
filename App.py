#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install langchain')


# In[4]:


get_ipython().system('pip install -U langchain-community')


# In[5]:


get_ipython().system('pip install numpy')


# In[7]:


from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS


# In[8]:


import pdfplumber



# In[9]:


get_ipython().system('pip install pdfplumber')


# In[12]:


import pdfplumber
import os

def read_pdfs(pdf_paths):
    full_text = ""
    for path in pdf_paths:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
    return full_text

pdf_files=[
    "Acko-Group-Health-Insurance.pdf",
    "Introduction to Law ( PDFDrive ).pdf",
    "Q1-FY24-Financial-results-presentation-Final-2.pdf"
]

document_text = read_pdfs(pdf_files)


# In[15]:


text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(Acko-Group-Health-Insurance.pdf)


# In[49]:


CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)


# In[17]:


import pdfplumber

with pdfplumber.open("Acko-Group-Health-Insurance.pdf") as pdf, open("output.txt", "w", encoding="utf-8") as f:
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            f.write(t + '\n')


# In[18]:


import pypdf   

reader = pypdf.PdfReader(source_filename)
writer = pypdf.PdfWriter()

page = reader.pages[0]  
new_page = pypdf.PageObject.create_blank_page( None, width = page.mediabox.width, height = page.mediabox.height ) 
page.mediabox.bottom = ( page.mediabox.top - page.mediabox.bottom ) / 2 + page.mediabox.bottom 
new_page.merge_page( page )

writer.add_page(new_page)
with open(output_file, "wb") as fp:
    writer.write(fp)


# In[19]:


get_ipython().system('pip install pypdf')


# In[26]:


import pypdf
reader = pypdf.PdfReader(Acko-Group-Health-Insurance.pdf)
writer = pypdf.PdfWriter()

page = reader.pages[0]  
new_page = pypdf.PageObject.create_blank_page( None, width = page.mediabox.width, height = page.mediabox.height ) 
page.mediabox.bottom = ( page.mediabox.top - page.mediabox.bottom ) / 2 + page.mediabox.bottom 
new_page.merge_page( page )

writer.add_page(new_page)
with open(App.py, "wb") as fp:
    writer.write(fp)


# In[27]:


import pdfplumber

def read_pdf(file_path):
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text

document_text = read_pdf("Acko-Group-Health-Insurance.pdf")


# In[29]:


get_ipython().system('pip install PyPDF2')


# In[34]:


from PyPDF2 import PdfReader
pdf_path = C:\Users\aarth\Downloads\Introduction to Law ( PDFDrive ).pdf
reader = PdfReader(pdf_path)


# In[35]:


from pypdf import PdfReader

reader = PdfReader('Introduction to Law ( PDFDrive ).pdf')

print(len(reader.pages))

page = reader.pages[0]

text = page.extract_text()
print(text)


# In[37]:


def split_into_chunks(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

chunks = split_into_chunks('Introduction to Law ( PDFDrive ).pdf')


# In[41]:


import pdfplumber
def read_multiple_pdfs(pdf_paths):
    text = ""
    for path in pdf_paths:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
    return text
pdf_files = ["Introduction to Law ( PDFDrive ).pdf", "Acko-Group-Health-Insurance.pdf", "Q1-FY24-Financial-results-presentation-Final-2.pdf"]
document_text = read_multiple_pdfs(pdf_files)



# In[48]:


CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)


# In[50]:


os.environ["OPENAI_API_KEY"] = "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"



# In[51]:


from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter


# In[54]:


CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents("Introduction to Law ( PDFDrive ).pdf")


# In[ ]:





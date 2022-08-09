#!/usr/bin/env python
# coding: utf-8

# In[82]:


#Importing tools for converiting PDFs to TXTs

from subprocess import Popen, PIPE
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os


# In[84]:


#Converte Cartella di PDF files in TXT 

def convert_pdf_to_txt(path):

    filelist=os.listdir(path)
    documentcollection=[]
    for files in filelist:
        files=os.path.join(path,files)
        documentcollection.append(files)
    for ifiles in documentcollection:
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)    
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        ifilesid=open(ifiles,"rb")
        for page in PDFPage.get_pages(ifilesid, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()

        filename, file_extension=os.path.splitext(ifiles)
        splitted,files=os.path.split(filename)
        splittedd,pathd=os.path.split(splitted)
        yy=splittedd+ files+'.'+'txt'
        zz=splittedd+ files+'.'+'html'
        txtfileo=open(yy,'w',encoding="utf-8")
        txtfileo.write(text)
        txtfileo.close()
        txtfileo1=open(zz,'w',encoding="utf-8")
        txtfileo1.write(text)
        txtfileo1.close()
       
        
    ifilesid.close()

    retstr.close()
    device.close()
    return text

print(convert_pdf_to_txt('File Sample PDF'))


# In[226]:


#Importing text mining tools
import gensim
from gensim import corpora

from smart_open import smart_open
from pprint import pprint
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.corpora.dictionary import Dictionary

from gensim.parsing.preprocessing import preprocess_documents, strip_short, strip_tags

from gensim.models import LdaModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords


# In[243]:


#Opening TXT files and creating a Gensim Dictionary

class ReadTxtFiles(object):
    def __init__(self, dirname):
        self.dirname = dirname
        
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname), encoding='utf-8'):
                #CUSTOM_FILTERS=[lambda x: x.lower(), strip_short]
                yield preprocess_string(line)


# In[244]:


path_to_text_directory = "File Sample Conv"
mydict = corpora.Dictionary(ReadTxtFiles(path_to_text_directory))


# In[236]:



my_corpus = [mydict.doc2bow(text, allow_update=True) for text in (ReadTxtFiles(path_to_text_directory))]


# In[ ]:





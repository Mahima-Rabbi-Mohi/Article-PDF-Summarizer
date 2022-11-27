# Import Libraries

import tkinter as tk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import PyPDF2 as p
from rsa import PublicKey

import nltk
from textblob import TextBlob
from newspaper import Article
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import summary_help


nltk.download('punkt') # for sentiment analysis
nltk.download('stopwords') # for initializing stopwords

stopwords = set (stopwords.words("english"))

# Open Main window

root= tk.Tk()
root.title("PDF Generator | Summarizer")
root.iconbitmap(r'C:\Users\User\Desktop\prep\cv_projects\Project\Article-PDF-Summarizer\favicon.ico')
root.geometry('300x300')
root.configure(bg='#192c3a')

pdf_text=''
enc_output = p.PdfFileWriter()


## Article (URL) Summarization 

def open_url(): # Read URL to get the Article for Summarization

    root.title("Article Summarizer")
    root.geometry('1200x750')

    utlabel= tk.Label(root, text="Article Summarizer", bg='#192c3a', fg="#aeaeb0", font=("Arial, 16"))
    utlabel.pack()

    tlabel.pack()
    title.pack()
    alabel.pack()
    author.pack()
    plabel.pack()
    p_date.pack()
    slabel.pack()
    summary.pack()
    sent_label.pack()
    sent_analysis.pack()
    ulabel.pack()
    utext.pack()

    url_sum_btn= tk.Button(root, text="Summarize", bg='#192c3a', fg="#aeaeb0", command=summarize_url).pack()
    

def summarize_url(): # Displaying all the data generated from URL

    url= utext.get('1.0', "end").strip()

    article = Article(url)

    article.download() # to get it into the script
    article.parse() # to make it readable to get all the HTML out of it
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    p_date.config(state='normal')
    summary.config(state='normal')
    sent_analysis.config(state='normal')

    # print title
    title.delete('1.0','end')
    title.insert('1.0', article.title)

    # print author name
    author.delete('1.0','end')
    author.insert('1.0', article.authors or 'Not mentioned')

    # print publication_date
    p_date.delete('1.0','end')
    p_date.insert('1.0', article.publish_date or 'Hidden')

    # print summary
    summary.delete('1.0','end')
    summary.insert('1.0', article.summary or 'None')

    # print sentiment_analysis
    analysis= TextBlob(article.text)
    sent_analysis.delete('1.0','end')
    sent_analysis.insert('1.0', f'{"Positive" if analysis.polarity>0 else "Negative" if analysis.polarity<0 else "Neutral"}             (Polarity Score : {analysis.polarity} )')

    title.config(state='disabled')
    author.config(state='disabled')
    p_date.config(state='disabled')
    summary.config(state='disabled')
    sent_analysis.config(state='disabled')


    btn= tk.Button(root, text="Full Article", bg='#192c3a', fg="#aeaeb0", command=show_full_text_url)
    btn.pack()
    
    
def show_full_text_url(): # To show Full-Text from the Article

    root.geometry('1200x950')

    url= utext.get('1.0', "end").strip()

    article = Article(url)

    article.download() # to get it into the script
    article.parse() # to make it readable to get all the HTML out of it
    article.nlp()

    full_article = tk.Text(root, height=16, width=140)
    full_article.config(state='disable', bg='#ffefed')
    full_article.pack()

    full_article.config(state='normal')

    full_article.delete('1.0','end')
    full_article.insert('1.0', article.text or 'None')

    full_article.config(state='disabled')
    

## PDF Summarization 

def open_pdf(): # Read PDF file for Summarization
    root.title("PDF Summarizer")
    pdf_btn= tk.Button(root, text="Upload PDF", bg='#192c3a', fg="#aeaeb0", command=browseFiles).pack()


def browseFiles(): # Read PDF file for Summarization
    
    file = filedialog.askopenfilename(initialdir=r"C:\Users\User\Desktop\prep\cv_projects\Project\p1\Documents", title='Select a PDF File', filetypes=(("pdf","*.pdf"),("all","*.*")))
    proot= tk.Tk()
    proot.title("PDF Summarizer")
    proot.iconbitmap(r'C:\Users\User\Desktop\prep\cv_projects\Project\Article-PDF-Summarizer\favicon.ico')
    proot.configure(bg='#192c3a')
    proot.geometry('900x700')

    if file:
        
        text = extract_text(file)

#         pdf_summary= summarize_pdf(text)

        pdf_summary= summary_help.summary_main(text)

        ptlabel= tk.Label(proot, text="PDF Summarizer", bg='#192c3a', fg="#aeaeb0", font=("Arial, 16"))
        ptlabel.pack()

        ftlabel= tk.Label(proot, text="Full PDF", bg='#192c3a', fg="#aeaeb0")
        ftlabel.pack()
        full_text = tk.Text(proot, height=25, width=100)
        full_text.config(state='disable', bg='#ffefed')
        full_text.pack()

        full_text.config(state='normal')

        full_text.delete('1.0','end')
        full_text.insert('1.0', text or 'None')

        full_text.config(state='disabled')

        slabel= tk.Label(proot, text="Summary", bg='#192c3a', fg="#aeaeb0")
        slabel.pack()

        summary = tk.Text(proot, height=10, width=100)
        summary.config(state='disable', bg='#ffefed')
        summary.pack()

        summary.config(state='normal')

        summary.delete('1.0','end')
        summary.insert('1.0', pdf_summary or 'None')
    
    
## Password Protected PDF Generation

def open_enc_pdf(): # Read PDF file and create new one for Encryption
    root.title("Password Protected PDF Generator")
    pdf_btn= tk.Button(root, text="Upload PDF File", bg='#192c3a', fg="#aeaeb0", command=enc_browseFiles).pack()

def enc_browseFiles(): # Generate another PDF file for encryption
    
    # Get input PDF for encyption
     
    enc_input_file = filedialog.askopenfilename(initialdir=r"C:\Users\User\Desktop\prep\cv_projects\Project\p1\Documents", title='Select a PDF File', filetypes=(("pdf","*.pdf"),("all","*.*")))

    
    input_stream = p.PdfFileReader(enc_input_file)
    

    if input_stream:

        # Extracting Pages

        for i in range(0,input_stream.getNumPages()):
            enc_output.addPage(input_stream.getPage(i))

        PublicKey.output_steam = open("ProtectedPDF.pdf" , "wb")

        # Encrypt Output File

        pwlabel.pack()
        pwtext.pack()

        en_gen_btn= tk.Button(root, text="Download as 'ProtectedPDF.pdf' file ", bg='#192c3a', fg="#aeaeb0", command=enc_pdf).pack()


def enc_pdf(): # Encrypt new PDF file with password
            
        password_input= pwtext.get('1.0', "end").strip()
        print(password_input)

        pwtext.delete('1.0','end')
        pwtext.insert('1.0', password_input or '*****')


        enc_output.encrypt(password_input, use_128bit=True)
        pwtext.delete('1.0','end')
        pwtext.config(state='disabled')
        enc_output.write(PublicKey.output_steam)
        PublicKey.output_steam.close()
        

# ## Alternative way for Summarization
        
# def summarize_pdf(text): # Method to Generate Summary from PDF text
    
#     words = word_tokenize(text)
#     freqTable = dict()

#     for word in words:
#         word=word.lower()
#         if word in stopwords:
#             continue
#         if word in freqTable:
#             freqTable[word]+=1
#         else:
#             freqTable[word]=1
        
#     sentences = sent_tokenize(text)
#     sentenceValue = dict()

#     for sentence in sentences:
#         for word,freq in freqTable.items():
#             if word in sentence.lower():
#                 if sentence in sentenceValue:
#                     sentenceValue[sentence]+=1
#                 else:
#                     sentenceValue[sentence]= freq


#     sumValues = 0
#     for sentence in sentenceValue:
#         sumValues += sentenceValue[sentence]

#     average = int(sumValues / len(sentenceValue))

#     summary= ''

#     for sentence in sentences:
#         if (sentence in sentenceValue) and (sentenceValue[sentence]> (1.2 * average)):
#             summary+= " "+ sentence

#     return summary


blabel= tk.Label(root, text="Which one would you like to choose ?", bg='#192c3a', fg="#aeaeb0")
blabel.pack()

#Add button label and text box

tlabel= tk.Label(root, text="Title", bg='#192c3a', fg="#aeaeb0")
title = tk.Text(root, height=1, width=140)
title.config(state='disable', bg='#ffefed')


alabel= tk.Label(root, text="Author", bg='#192c3a', fg="#aeaeb0")
author = tk.Text(root, height=1, width=140)
author.config(state='disable', bg='#ffefed')


plabel= tk.Label(root, text="Publication Date", bg='#192c3a', fg="#aeaeb0")
p_date = tk.Text(root, height=1, width=140)
p_date.config(state='disable', bg='#ffefed')


slabel= tk.Label(root, text="Summary", bg='#192c3a', fg="#aeaeb0")
summary = tk.Text(root, height=8, width=140)
summary.config(state='disable', bg='#ffefed')


sent_label= tk.Label(root, text="Sentiment Analysis", bg='#192c3a', fg="#aeaeb0")
sent_analysis = tk.Text(root, height=1, width=140)
sent_analysis.config(state='disable', bg='#ffefed')


ulabel= tk.Label(root, text="URL", bg='#192c3a', fg="#aeaeb0")
utext = tk.Text(root, height=1, width=140)
utext.config(bg='#ffefed') # state!='disable because it can take input form user

pwlabel= tk.Label(root, text="Enter password for PDF file", bg='#192c3a', fg="#aeaeb0")
pwtext = tk.Text(root, height=1, width=15)
pwtext.config(bg='#ffefed') # state!='disable because it can take input form user

# Features

def sum_options():
    top_button = tk.Button(root, text= "Article Summarization", bg='#192c3a', fg="#aeaeb0", command=open_url).pack()
    top_button = tk.Button(root, text= "PDF Summarization", bg='#192c3a', fg="#aeaeb0", command=open_pdf).pack()


top_button = tk.Button(root, text= "Generate Password Protected PDF", bg='#192c3a', fg="#aeaeb0", command=open_enc_pdf).pack()
top_button = tk.Button(root, text= "Summarize PDF / Article", bg='#192c3a', fg="#aeaeb0", command=sum_options).pack()

root.mainloop()

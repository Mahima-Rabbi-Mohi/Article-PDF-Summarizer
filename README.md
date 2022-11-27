# Password Protected PDF Generator and Summarizer

To ensure data privacy, this project has made it easier and inexpensive to generate and encrypt PDF files. It can initially provide a summary of an article from a Webpage or PDF. However, PDFs can also be downloaded utilizing encryption. Before a PDF document can be viewed in Adobe Reader or Adobe Acrobat, the user must provide the accessible password when it has been encrypted.

Encrypted PDF file : A PDF that has been encrypted is one that is unreadable and protected of all access. Using the right password, an authorized user can decrypt the document and access its contents.

Tkinter is the standard GUI library for Python. To know more about this, please visit https://docs.python.org/3/library/tk.html

# Workflow

* Created GUI (Graphical User Interface) using Tkinter
* Used Python libraries TextBlob and Newspaper3k for processing textual data and Web Scraping articles
* Generated title, author, publication date, summary, and sentiment analysis polarity score from an URL
* Extracted information from uploaded PDF documents using PDFMiner and summarized it
* A summary of any given text can be generated with a pre-trained T5 model


# Demo video :

https://user-images.githubusercontent.com/104271917/197367019-0daa82e7-79ee-4c24-a422-3005be9549d6.mp4

# Features :

With the help of this python project, any one can easily generate a summary from any PDF file or URL. 

* Upload a pdf file and get the extracted texts and their' summary.
* Give an URL and get its' summary with title, author name, and publication date. 
* Download the updated PDF and Encrypted PDF (Password Protected File) as per your requirements.

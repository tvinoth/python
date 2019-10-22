# get_doc_info.py
 
from PyPDF2 import PdfFileReader
 
 
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
 
    print(info)
    print(number_of_pages)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

    print(author,creator,subject,title)

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
 
        # get the first page
        number_of_pages = pdf.getNumPages()
        for i in range(number_of_pages):
            page = pdf.getPage(i)
            print(page)
            print('Page type: {}'.format(str(type(page))))
 
            text = page.extractText()
            print(text)
 
 
if __name__ == '__main__':
    path = 'sample.pdf'
    text_extractor(path)
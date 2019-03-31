from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal
import re
# encoding=utf8
import sys
fp = open(u'./jlpea-04-00214.pdf', 'rb')

parser = PDFParser(fp)

document = PDFDocument(parser)

rsrcmgr = PDFResourceManager(caching = False)

laparams = LAParams()

device = PDFPageAggregator(rsrcmgr, laparams = laparams)

interpreter = PDFPageInterpreter(rsrcmgr, device)

replace = re.compile(r's+')

for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for x in layout:
        if(isinstance(x,LTTextBoxHorizontal)):
            text = re.sub(replace,'',x.get_text())
            if len(text) != 0:
                print text
# 利用python将图片pdf转变为文字pdf：https://www.jb51.net/article/160621.htm

import os
import ghostscript
from PyPDF2 import PdfFileReader, PdfFileWriter
from PythonMagick import Image
from aip import AipOcr
import pdfkit

path='??'
pdfname='??'
DPI='85'
APP_ID='??'
API_KEY='??'
SECRET_KEY='??'
path_wk=r'pdfkit安装位置设置'
pdfkit_config=pdfkit.configuration(wkhtmltopdf=path_wk)
pdfkit_options={'encoding':'UTF-8',}

os.chdir(path)
pdf_input=PdfFileReader(open(pdfname, 'rb'))
page_count=pdf_input.getNumPages()
page_range=range(page_count)

for page_num in page_range:
	im=Image()
	im.density(DPI)
	im.read(pdfname + '[' + str(page_num) +']')
	im.write(str(page_num)+ '.jpg')

client=AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()

options={}
options["language_type"]="CHN_ENG"
options["detect_direction"]="false"
options["detect_language"]="false"
options["probability"]="false"
allteststr=[]
for page_num in page_range:
	image=get_file_content(r'%s\%s.jpg' % (path, page_num))
	testjson=client.basicGenral(image, options)
	teststr=''
	for x in testjson['words_result']:
		teststr=teststr+x['words']+'</br>'
	allteststr.append(teststr)

for page_num in page_range:
	padfkit.from_string((allteststr[page_num]), '%s.pdf' % (str(page_num)),configuration=pdfkit_config, options=pdfkit_options)

pdf_output=PdfFileWriter()
for page_num in page_range:
	os.chdir(path)
	pdf_input=PdfFlieReader(open('%s.pdf' % (str(page_num)), 'rb'))
	page=pdf_input.getPage(0)
	pdf_output.addPage(page)
	pdf_output.write(open('newpdf.pdf', 'wb'))
# importing required modules
import PyPDF2


def PDFmerge(pdfs, output):
	# creating pdf file merger object
	pdfMerger = PyPDF2.PdfFileMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		pdfMerger.append(pdf)

	# writing combined pdf to output pdf file
	with open(output, 'wb') as f:
		pdfMerger.write(f)


def main():
	# pdf files to merge
	pdfs = ['file1.pdf', 'file2.pdf']

	# output pdf file name
	output = 'mergedfiles.pdf'

	# calling pdf merge function
	PDFmerge(pdfs=pdfs, output=output)

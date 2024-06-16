import PyPDF2

class PDFProcessing():
    def __init__(self):
        self.__file = ""

    def set_file(self, file):
        self.__file = file

    def get_text(self):
        pdf_reader = PyPDF2.PdfReader(self.__file)

        extracted_text = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

        return extracted_text
    

    
import PyPDF2
from docx import Document
class Reader():
    def __init__(self) -> None:
        pass

    def read_document(self,file_path):
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                text = ''
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text += page.extractText()

        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        elif file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            raise ValueError("Unsupported file format")
        return text
    
    def create_chunks(self, text, chunk_size):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
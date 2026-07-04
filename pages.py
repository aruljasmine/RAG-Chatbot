from pypdf import PdfReader

reader = PdfReader("Data/tasks.pdf")
print(len(reader.pages))
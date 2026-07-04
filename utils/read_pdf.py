from pypdf import PdfReader


def load_pdf(pdf_file):
    """
    Reads a PDF and returns:
    - text
    - number of pages
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text, len(reader.pages)
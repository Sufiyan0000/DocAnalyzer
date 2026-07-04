from pathlib import Path

from langchain_core.documents import Document
from pypdf import PdfReader


def load_pdf(file_path):
    file_path = Path(file_path)

    reader = PdfReader(file_path)

    documents = [
        Document(
            page_content=page.extract_text() or "",
            metadata={
                "source": file_path.name,
                "page": page_number,
            },
        )
        for page_number, page in enumerate(reader.pages)
    ]

    return documents
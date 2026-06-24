from pathlib import Path
import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


RAW_BOOK_DIR = Path("data/raw_books")


splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)


def extract_pdf_text(pdf_path: Path):
    document = fitz.open(pdf_path)

    pages = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()

        if text.strip():
            pages.append(
                {
                    "page": page_num + 1,
                    "text": text
                }
            )

    return pages


def chunk_single_pdf(pdf_path: Path):
    page_data = extract_pdf_text(pdf_path)

    chunks = []

    for page_info in page_data:

        page_chunks = splitter.split_text(page_info["text"])

        for chunk in page_chunks:
            chunks.append(
                {
                    "source": pdf_path.name,
                    "page": page_info["page"],
                    "text": chunk
                }
            )

    return chunks


def chunk_all_books():

    all_chunks = []

    pdf_files = list(RAW_BOOK_DIR.glob("*.pdf"))

    for pdf_file in pdf_files:

        print(f"Processing {pdf_file.name}")

        chunks = chunk_single_pdf(pdf_file)

        all_chunks.extend(chunks)

    print(f"\nTotal chunks created: {len(all_chunks)}")

    return all_chunks


if __name__ == "__main__":

    chunks = chunk_all_books()

    print("\nExample chunk:\n")
    print(chunks[0])

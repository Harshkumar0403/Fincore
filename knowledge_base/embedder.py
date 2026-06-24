from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL
from knowledge_base.chunker import chunk_all_books


# Load model once
model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embeddings():

    chunks = chunk_all_books()

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    embedded_chunks = []

    for chunk, embedding in zip(chunks, embeddings):

        embedded_chunks.append(
            {
                "source": chunk["source"],
                "page": chunk["page"],
                "text": chunk["text"],
                "embedding": embedding.tolist()
            }
        )

    return embedded_chunks


if __name__ == "__main__":

    embedded_chunks = generate_embeddings()

    print("\nExample Embedded Chunk:\n")

    print({
        "source": embedded_chunks[0]["source"],
        "page": embedded_chunks[0]["page"],
        "embedding_dimension": len(embedded_chunks[0]["embedding"])
    })

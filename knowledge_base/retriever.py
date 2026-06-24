import duckdb
from sentence_transformers import SentenceTransformer
import numpy as np
from config.settings import (
    EMBEDDING_MODEL,
    DUCKDB_PATH,
    TOP_K
)


model = SentenceTransformer(EMBEDDING_MODEL)


def retrieve(query: str):

    query_embedding = (
        model.encode(query)
        .astype(np.float32)
        .tolist()
    )

    conn = duckdb.connect(DUCKDB_PATH)

    results = conn.execute(
        """
        SELECT
            source,
            page,
            text,
            array_cosine_similarity(
                embedding,
                CAST(? AS FLOAT[384])
            ) AS similarity
        FROM documents
        ORDER BY similarity DESC
        LIMIT ?
        """,
        [query_embedding, TOP_K]
    ).fetchall()

    conn.close()

    retrieved_chunks = []

    for source, page, text, similarity in results:

        retrieved_chunks.append(
            {
                "source": source,
                "page": page,
                "similarity": float(similarity),
                "text": text
            }
        )

    return retrieved_chunks


if __name__ == "__main__":

    results = retrieve(
        "What is depreciation in accounting?"
    )

    for chunk in results:

        print("\n--------------------")
        print("Source:", chunk["source"])
        print("Page:", chunk["page"])
        print("Similarity:", round(chunk["similarity"], 4))
        print(chunk["text"][:500])

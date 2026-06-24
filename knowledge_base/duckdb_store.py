from pathlib import Path
import duckdb

from config.settings import DUCKDB_PATH
from knowledge_base.embedder import generate_embeddings


def build_vector_database():

    embedded_chunks = generate_embeddings()

    Path(DUCKDB_PATH).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    conn = duckdb.connect(DUCKDB_PATH)

    # Remove old table during development
    conn.execute("DROP TABLE IF EXISTS documents")

    conn.execute("""
    CREATE TABLE documents (
        id INTEGER,
        source TEXT,
        page INTEGER,
        text TEXT,
        embedding FLOAT[384]
    )
    """)

    rows = []

    for idx, chunk in enumerate(embedded_chunks):

        rows.append(
            (
                idx,
                chunk["source"],
                chunk["page"],
                chunk["text"],
                chunk["embedding"]
            )
        )

    conn.executemany(
        """
        INSERT INTO documents
        VALUES (?, ?, ?, ?, ?)
        """,
        rows
    )

    conn.close()

    print(f"Inserted {len(rows)} chunks into DuckDB")


if __name__ == "__main__":
    build_vector_database()

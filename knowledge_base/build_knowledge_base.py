from pathlib import Path

from config.settings import DUCKDB_PATH
from knowledge_base.duckdb_store import build_vector_database


def initialize_knowledge_base():

    db_path = Path(DUCKDB_PATH)

    if db_path.exists():

        print("✓ Knowledge base already exists.")
        return

    print("Building knowledge base...")

    build_vector_database()

    print("✓ Knowledge base built successfully.")


if __name__ == "__main__":
    initialize_knowledge_base()

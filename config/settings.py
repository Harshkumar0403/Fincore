from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MAIN_MODEL = "openai/gpt-oss-120b"

JUDGE_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

DUCKDB_PATH = "data/processed/finance.db"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

TOP_K = 5

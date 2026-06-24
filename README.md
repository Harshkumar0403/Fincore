# FinCore AI: Agentic Financial Research Assistant

FinCore AI is a modular multi-agent financial assistant built using Agno, Groq LLMs, Retrieval-Augmented Generation (RAG), and real-time financial tools.

The system combines financial knowledge from books, live market information, web search, and numerical calculations to answer finance and accounting queries in a reliable and structured manner.

link : https://fincore-production-7bfa.up.railway.app/docs

---

## Features

### Multi-Agent Architecture

FinCore AI consists of four specialized agents:

* Coordinator Agent
* Research Agent
* Analysis Agent
* Judge Agent

Each agent performs a single responsibility, making the system modular, explainable, and easy to extend.

---

## Supported Capabilities

### Knowledge Base (RAG)

The system retrieves information from finance and accounting books using:

* PDF ingestion from URLs
* Semantic chunking
* Sentence Transformers embeddings
* DuckDB vector database

### Live Market Data

Using yfinance, the assistant can provide:

* Current stock prices
* P/E ratios
* Market capitalization
* Dividend yield
* 52-week high and low
* Trading volume
* Historical prices

### Web Search

DuckDuckGo Search (DDGS) provides:

* Recent financial news
* Earnings announcements
* External information not present in the knowledge base

### Calculator Tool

Supports:

* Percentage change
* Average
* Median
* Maximum
* Minimum

### LLM-as-a-Judge

Responses are automatically evaluated for:

* Factual accuracy
* Grammar quality
* Relevance

---

# Architecture

User Query

↓

Coordinator Agent

↓

Tool Selection

↓

RAG / DDGS / yFinance / Calculator

↓

Research Agent

↓

Analysis Agent

↓

Judge Agent

↓

Structured JSON Response

---

## Multi-Agent Workflow

### 1. Coordinator Agent

Determines which tools are required for the query.

Examples:

* Finance concepts → RAG
* Market data → yFinance
* News → DDGS
* Numerical operations → Calculator

### 2. Research Agent

Collects and organizes information from tools.

Responsibilities:

* Gather evidence
* Preserve sources
* Avoid hallucinations

### 3. Analysis Agent

Produces the final user-facing answer using only the research findings.

### 4. Judge Agent

Evaluates the answer and assigns quality scores.

---

# Tech Stack

## LLMs

Main Model:

openai/gpt-oss-120b

Judge / Coordinator Model:

meta-llama/llama-4-scout-17b-16e-instruct

Provider:

Groq

---

## Vector Database

DuckDB

---

## Embedding Model

sentence-transformers/all-MiniLM-L6-v2

---

## Libraries

* Agno
* Groq
* DuckDB
* Sentence Transformers
* yfinance
* DDGS
* Pydantic

---

# Project Structure

```text
Fincore/

agents/
    coordinator_agent.py
    research_agent.py
    analysis_agent.py
    judge_agent.py

knowledge_base/
    download_books.py
    chunker.py
    embedder.py
    duckdb_store.py
    retriever.py

tools/
    rag_tool.py
    ddgs_tool.py
    yfinance_tool.py
    calculator_tool.py

utils/
    ticker_extractor.py

schemas/
    response_schema.py
    judge_schema.py

prompts/
    coordinator_prompt.txt
    research_prompt.txt
    analysis_prompt.txt
    judge_prompt.txt

config/
    settings.py
    models.py

app.py
requirements.txt
```

---

# Knowledge Sources

The knowledge base is built from finance and accounting textbooks including:

* Financial Accounting
* Foundations of Accounting and Finance
* Accounting Fundamentals
* BSCIT Financial Accounting material

PDFs are downloaded automatically from public URLs and indexed into DuckDB.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd Fincore
```

Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key

MAIN_MODEL=openai/gpt-oss-120b
JUDGE_MODEL=meta-llama/llama-4-scout-17b-16e-instruct
```

---

# Build Knowledge Base

Download books:

```bash
python -m knowledge_base.download_books
```

Create chunks:

```bash
python -m knowledge_base.chunker
```

Generate embeddings:

```bash
python -m knowledge_base.embedder
```

Build DuckDB:

```bash
python -m knowledge_base.duckdb_store
```

---

# Usage

Example:

```bash
python app.py --query "What is working capital?"
```

Example:

```bash
python app.py --query "Current PE ratio of NVDA"
```

Example:

```bash
python app.py --query "What is the percentage change of NVDA price from previous week?"
```

---

# Example Output

```json
{
  "query": "...",
  "tools_used": ["yfinance", "calculator"],
  "research_summary": "...",
  "final_answer": "...",
  "judge_feedback": {
    "factual_accuracy": 10,
    "grammar_quality": 10,
    "relevance": 10
  },
  "processing_time": 11.7
}
```

---

# Future Improvements

* Agno UI integration
* FastAPI deployment
* Streamlit interface
* Docker support
* Memory and conversation history
* Options chain analysis
* GraphRAG
* Portfolio analytics

---

# Motivation

FinCore AI was designed to demonstrate how agentic AI systems can combine:

* RAG
* Tool calling
* Real-time market data
* Multi-agent collaboration
* Automated evaluation

to create reliable financial assistants.

---

## Version

Current Release:

v1.0


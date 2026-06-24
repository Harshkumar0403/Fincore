from knowledge_base.retriever import retrieve


from knowledge_base.retriever import retrieve


def rag_search(query: str):

    results = retrieve(query)

    clean_results = []

    for chunk in results:

        clean_results.append(
            {
                "source": chunk["source"],
                "page": chunk["page"],
                "text": chunk["text"]
            }
        )

    return clean_results

if __name__ == "__main__":

    output = rag_search(
        "What is depreciation?"
    )

    print(output)

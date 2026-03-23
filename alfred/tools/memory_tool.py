from smolagents import tool
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    Settings,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
import os

# FORCE LOCAL: Use a tiny local embedder (runs on your 4070 Super)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
# We use a Mock or local LLM setting so LlamaIndex doesn't try to call OpenAI for synthesis
Settings.llm = None


@tool
def search_archives(query: str) -> str:
    """
    Searches the Batcave archives (local files) for past project details or notes.
    Args:
        query: The specific topic or detail to look for in past reports.
    """
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_path, "batcave_logs")
    persist_dir = os.path.join(base_path, "storage")

    if not os.path.exists(log_dir):
        return f"Error: Log directory not found at {log_dir}."

    # Indexing with local BGE embeddings
    if not os.path.exists(persist_dir):
        documents = SimpleDirectoryReader(log_dir).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)

    # We use 'retriever' mode to just get the text chunks without needing an LLM synthesis
    retriever = index.as_retriever(similarity_top_k=2)
    nodes = retriever.retrieve(query)

    if not nodes:
        return "No relevant architectural notes found in archives."

    return "\n".join([n.get_content() for n in nodes])

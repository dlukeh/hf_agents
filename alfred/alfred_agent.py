# --- 1. CORE IMPORTS & CONFIGURATION ---
# We use nest_asyncio to allow LlamaIndex's async loops to run in interactive terminals.
import asyncio
import nest_asyncio
from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool

nest_asyncio.apply()

# Setup the Brain (LLM) and the Memory (Embedding)
Settings.llm = Ollama(model="gemma3:12b", request_timeout=120.0)
# Using BGE-Small for fast, local vector searches on the 4070 Super
Settings.embed_model = "local:BAAI/bge-small-en-v1.5"

# --- 2. TOOL DEFINITIONS ---
# These functions are the "hands" of the agent.
# The docstrings act as the instruction manual for the LLM.


def web_search(query: str) -> str:
    """Performs a live DuckDuckGo search for current news and facts."""
    from ddgs import DDGS

    with DDGS() as ddgs:
        results = [r["body"] for r in ddgs.text(query, max_results=3)]
        return "\n".join(results) or "No results found."


def run_shell(command: str) -> str:
    """Executes Linux shell commands locally. Use with extreme caution."""
    import subprocess

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error: {str(e)}"


# --- 3. AGENT INITIALIZATION ---
# We wrap our functions into LlamaIndex tools and initialize the ReAct loop.
tools = [
    FunctionTool.from_defaults(fn=web_search, name="web_search"),
    FunctionTool.from_defaults(fn=run_shell, name="terminal"),
]

agent = ReActAgent(tools=tools, llm=Settings.llm)


# --- 4. EXECUTION LOOP ---
async def main():
    print("--- 🤖 The Beast is Online ---")
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # max_iterations=50 prevents the agent from giving up too early on hard tasks
        response = await agent.run(user_input, max_iterations=50)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    asyncio.run(main())

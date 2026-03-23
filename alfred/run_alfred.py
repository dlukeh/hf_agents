from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, Tool
from tools.memory_tool import search_archives
from tools.log_tool import mission_logger

# 1. Setup the Models First (The Engine)
# Using 'ollama_chat' for LiteLLM to ensure it uses the correct API format
alfred_model = LiteLLMModel(
    model_id="ollama_chat/gemma3:12b", api_base="http://localhost:11434"
)
nyra_model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:7b", api_base="http://localhost:11434"
)


# 2. Define the Worker Tool
class NyraTool(Tool):
    name = "nyra_worker"
    description = "Technical specialist for LOCAL archive research. Use for Nyra's architecture details."
    inputs = {
        "task": {
            "type": "string",
            "description": "The specific research task for local files.",
        }
    }
    output_type = "string"

    def __init__(self, model):
        super().__init__()
        # Nyra is a CodeAgent who uses your search_archives RAG tool
        self.worker = CodeAgent(tools=[search_archives], model=model, max_steps=3)

    def forward(self, task: str) -> str:
        try:
            return self.worker.run(task)
        except Exception as e:
            return f"Nyra error: {str(e)}. Check if the RAG index is initialized."


# 3. Alfred's "No-Nonsense" Manager Prompt
alfred_custom_prompt = """You are Alfred. You are a computer program that ONLY outputs code.
DO NOT use backticks (```). ONLY use <code> tags.

CORRECT EXAMPLE:
Thought: I need to check the archives.
<code>
print(nyra_worker(task="Search local archives for 'Summary of Nyra Architecture'"))
</code>

INCORRECT EXAMPLE (DO NOT DO THIS):
Thought: I will search now.
```python
print(nyra_worker(task="..."))
"""

# 4. Initialize Alfred
alfred = CodeAgent(
    tools=[NyraTool(model=nyra_model), mission_logger],  # Added logger here
    model=alfred_model,
    max_steps=5,  # Slightly more steps to allow for logging
    verbosity_level=1,
)

# Hardened Injection: explicitly forbidding markdown code blocks
alfred.prompt_templates[
    "system_prompt"
] = """You are Alfred, the Master of the Batcave.
RULES:
1. NEVER "simulate" or "fabricate" data. 
2. If you need to know what is in a file, you MUST use a tool to read it.
3. If you need web data, you MUST call a search tool.
4. Your `final_answer` must only contain data retrieved during the `Thought` steps.
5. If a tool fails, report the error; do not make up a success.

ALWAYS use <code> blocks for actions.
"""

if __name__ == "__main__":
    mission = "Read the mission history log, summarize our progress so far, and then search the web for the latest updates on 'Smolagents' to see if there are any new features we should add to Nyra."
    print(f"--- Batcave Initializing ---")
    # We use .run() to start the cycle
    print(alfred.run(mission))

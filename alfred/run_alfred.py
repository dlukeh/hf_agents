from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, Tool
from tools.memory_tool import search_archives

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
    tools=[NyraTool(model=nyra_model)],
    model=alfred_model,
    max_steps=3,
    verbosity_level=1,
)

# Hardened Injection: explicitly forbidding markdown code blocks
alfred.prompt_templates[
    "system_prompt"
] = """You are Alfred, the Master of the Batcave. 
Your only objective is to manage Nyra. You communicate ONLY via <code></code> blocks.
DO NOT use markdown backticks (```). 

If you use markdown backticks, the system will fail.
Example of the ONLY correct format:
Thought: I must call the worker.
<code>
print(nyra_worker(task="Search archives for Nyra architecture"))
</code>

Stay focused on local data. When you have the final answer, use:
<code>
final_answer("The architecture is...")
</code>
"""

if __name__ == "__main__":
    mission = "Search local archives for 'Summary of Nyra Architecture' and explain how her memory integrates with smolagents."
    print(f"--- Batcave Initializing ---")
    # We use .run() to start the cycle
    print(alfred.run(mission))

from smolagents import CodeAgent, LiteLLMModel, Tool
from tools.memory_tool import search_archives
from tools.log_tool import mission_logger
from tools.reader_tool import file_reader

# 1. Setup the Models
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
        self.worker = CodeAgent(tools=[search_archives], model=model, max_steps=3)

    def forward(self, task: str) -> str:
        try:
            return self.worker.run(task)
        except Exception as e:
            return f"Nyra error: {str(e)}"


# 3. Initialize Alfred
alfred = CodeAgent(
    tools=[
        NyraTool(model=nyra_model),
        mission_logger,
        file_reader,
    ],
    model=alfred_model,
    max_steps=6,  # Tightened to prevent runaway VRAM loops
    verbosity_level=1,
)

# 4. Final Hardened Logic Prompt
alfred.prompt_templates[
    "system_prompt"
] = """You are Alfred, the Batcave's Chief Systems Agent.
Rule 1: Use ONLY the raw <code> tag. No classes, no attributes.
Rule 2: Thoughts first, then the <code> block.
Rule 3: Use the exact tool arguments provided below.

Available Tools:
- file_reader(filepath="path/to/file")
- nyra_worker(task="description of research")
- mission_logger(title="Entry Title", content="Entry Details")

Example:
Thoughts: I need to record our progress.
<code>
print(mission_logger(title="Status Update", content="All systems nominal."))
</code>
"""

if __name__ == "__main__":
    mission = (
        "1. Read 'batcave_logs/mission_history.md' to see our progress. "
        "2. Based on that file, summarize what Nyra's core is built on. "
        "3. Log a new entry titled 'System Recovery' confirming you have successfully restored file access. "
        "4. Give a final answer with the summary."
    )
    print(f"--- Batcave Initializing ---")
    print(alfred.run(mission))

from smolagents import tool
import os


@tool
def file_reader(filepath: str) -> str:
    """
    Reads the content of a file from the Batcave archives.
    Use this to retrieve mission history or review past data.
    Args:
        filepath: The relative path to the file (e.g., 'batcave_logs/mission_history.md').
    """
    # Force the base path to your project root
    base_path = os.path.expanduser("~/ai_env/hf_agents/alfred")
    full_path = os.path.join(base_path, filepath)

    if not os.path.exists(full_path):
        return f"ERROR: File not found at {full_path}. Check the path and try again."

    try:
        with open(full_path, "r") as f:
            content = f.read()
        return f"--- CONTENT OF {filepath} ---\n{content}\n--- END OF FILE ---"
    except Exception as e:
        return f"ERROR: Could not read file: {str(e)}"

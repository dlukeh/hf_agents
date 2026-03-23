from smolagents import tool
import os
from datetime import datetime


@tool
def mission_logger(content: str) -> str:
    """
    Logs the outcome of a mission to the Batcave archives.
    Args:
        content: The summary or data to be recorded for future reference.
    """
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(base_path, "batcave_logs", "mission_history.md")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## Mission Log: {timestamp}\n{content}\n---\n"

    try:
        with open(log_file, "a") as f:
            f.write(entry)
        return f"Mission successfully logged to {log_file}."
    except Exception as e:
        return f"Failed to log mission: {str(e)}"

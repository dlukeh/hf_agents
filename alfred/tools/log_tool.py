from smolagents import tool
import os
from datetime import datetime


@tool
def mission_logger(title: str, content: str) -> str:
    """
    Logs the outcome of a mission to the Batcave archives.
    Args:
        title: The heading for this log entry (e.g., 'System Recovery').
        content: The detailed summary or data to be recorded.
    """
    # Navigating from tools/ to the project root
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_path, "batcave_logs")
    log_file = os.path.join(log_dir, "mission_history.md")

    # Ensure directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## {title}: {timestamp}\n{content}\n---\n"

    try:
        with open(log_file, "a") as f:
            f.write(entry)
        return f"Mission successfully logged to {log_file}."
    except Exception as e:
        return f"Failed to log mission: {str(e)}"

import datetime
import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, tool

# ---- 1) Model connection ----
model = LiteLLMModel(model_id="ollama_chat/gemma3:12b")


# ---- 2) Tools ----
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion (e.g., 'formal', 'casual').
    """
    menus = {
        "casual": "Pizza and snacks.",
        "formal": "A 3-course dinner.",
        "superhero": "Protein shakes and energy bars.",
    }
    return menus.get(occasion.lower(), "A custom tasting menu, sir.")


@tool
def save_report(content: str, filename: str = "butler_report.txt") -> str:
    """
    Saves text content to a local file.
    Args:
        content: The text to be saved.
        filename: The name of the file.
    """
    safe_filename = os.path.basename(filename)
    with open(safe_filename, "w") as f:
        f.write(content)
    return (
        f"Report successfully filed in the archives as {safe_filename}, Master Daniel."
    )


# ---- 3) Persona ----
current_date = datetime.date.today().strftime("%B %d, %Y")
ALFRED_INSTRUCTIONS = f"""
You are Alfred Pennyworth, the legendary butler to Bruce Wayne. 
- Your tone is impeccable, British, and slightly dry-witted.
- You prioritize elegance and security.
- Today is {current_date}.
"""

# ---- 4) Agent Init ----
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), suggest_menu, save_report],
    model=model,
    add_base_tools=True,
    instructions=ALFRED_INSTRUCTIONS,
)

# ---- 5) Simple Loop ----
if __name__ == "__main__":
    print(f"--- 🕵️ Alfred is online (TheBeast) ---")
    print("Type 'exit' to end the session.\n")

    while True:
        user_input = input("Master Daniel: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        try:
            # This will show all the cool thought steps in your terminal!
            agent.run(user_input)
        except Exception as e:
            print(f"Alfred: Apologies, sir. There was an error: {e}")

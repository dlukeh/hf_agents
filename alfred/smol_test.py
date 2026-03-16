from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# 'ollama_chat/' is the magic prefix for LiteLLM to find your local Gemma
model = LiteLLMModel(model_id="ollama_chat/gemma3:12b")

# Give it eyes (Search) and a brain
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# Run a test
agent.run("What is the current price of a 1950s retro toaster on eBay?")

🤖 HF Agents Workspace: The Batcave

Project: hf_agents

Frameworks: smolagents, LiteLLM, LlamaIndex

Core Agents: Alfred (Orchestrator) & Nyra (Technical Specialist)

---
🌌 Project Overview

This repository serves as my primary development environment for the Hugging Face AI Agents Course. It features a local-first architecture designed to explore:

    Tool-Calling Loops: High-precision code execution and task delegation.

    Multi-Agent Systems: Supervisor/Worker patterns using Gemma 3 and Qwen 2.5.

    Local RAG: Private document indexing and retrieval via LlamaIndex.
---

---

⚡ The Beast: Local Compute Environment

All agent inference and code execution are performed locally on The Beast, an HP Omen 35L optimized for Large Language Model (LLM) workloads.

| Component | Specification | AI Impact |
| :--- | :--- | :--- |
| Processor | Intel i7-14700F (20 Cores) | Rapid pre-processing and script execution. |
| GPU | NVIDIA RTX 4070 Super (12GB) | Local 4-bit/8-bit quantization support. |
| RAM | 64GB DDR5 | High-capacity context window and RAG. |

📈 Performance Benchmarks

    Stable VRAM Ceiling: ~10.1 GB (Alfred + Nyra + Vector Store).

    Quantization: Optimized for GGUF and EXL2 formats via Ollama and LiteLLM.

    Inference Speed: Average 40-60 tokens/sec on 7B-12B parameter models.
---
---

## 🚀 Purpose

This workspace documents my journey through the Hugging Face Agents ecosystem.  
It includes:

- **Alfred** — a smolagents‑based autonomous agent  
- **Tool‑calling experiments**  
- **Code execution workflows**  
- **ReAct‑style reasoning traces**  
- **Course exercises and notebooks**  

Where `gemma_agent` is my *custom* agent built from scratch,  
`hf_agents` is my *framework‑based* exploration of modern agent tooling.

Together, they form a complete picture of my AI engineering practice.

---

## 🧩 Workspace Structure

The repository follows a clean, modular layout:

```text

├── alfred
│   ├── alfred_agent.py
│   ├── batcave_logs
│   │   ├── batcave_intrusion_report.txt
│   │   ├── gpu_telemetry.csv
│   │   ├── mission_history.md
│   │   └── nyra_architecture_summary.txt
│   ├── models
│   ├── run_alfred.py
│   ├── smol_alfred.py
│   ├── smol_test.py
│   ├── storage
│   │   ├── default__vector_store.json
│   │   ├── docstore.json
│   │   ├── graph_store.json
│   │   ├── image__vector_store.json
│   │   └── index_store.json
│   └── tools
│       ├── log_tool.py
│       ├── memory_tool.py
│       ├── __pycache__
│       │   ├── log_tool.cpython-312.pyc
│       │   ├── memory_tool.cpython-312.pyc
│       │   └── reader_tool.cpython-312.pyc
│       └── reader_tool.py
├── exercises
├── notebooks
└── README.md

```


---

## 🛠️ Key Components

### **🤖 Alfred (smolagents Agent)**
A fully functional agent built using:

- `ToolCallingAgent`
- `CodeAgent`
- `LiteLLMModel` (local or HF-hosted models)
- smolagents tool abstractions

Alfred demonstrates:

- multi‑step reasoning  
- tool selection  
- code execution  
- safe tool calling  
- structured output  

---

### **🧪 Course Exercises**
The `exercises/` folder contains:

- tool‑building practice  
- agent loop experiments  
- reasoning trace analysis  
- code‑interpreter workflows  

These files reflect hands‑on learning and experimentation.

---

### **📓 Notebooks**
The `notebooks/` directory includes:

- exploratory agent runs  
- tool‑calling prototypes  
- debugging sessions  
- architecture notes  

These notebooks show the iterative, experimental side of agent engineering.

---

## ▶️ Running Alfred

From inside `hf_agents/alfred`:

```
python3 smol_test.py
```

This will:

1. Load Alfred  
2. Initialize the smolagents runtime  
3. Execute a reasoning loop  
4. Call tools as needed  
5. Produce a final answer  

---

## 🎓 Background & Motivation

This workspace is part of my broader AI engineering journey, which includes:

- **Harvard CS50P** — Python fundamentals  
- **Harvard CS50AI** — classical AI, search, logic  
- **Hugging Face Agents Course** — smolagents, tool use, agent frameworks  

`hf_agents` represents the framework‑driven side of my agent engineering practice.

---

## 🏷️ Tags

- smolagents  
- huggingface  
- ai-agent  
- tool-calling  
- code-interpreter  
- python  
- autonomous-agents  
- agent-framework  
- llm-tools  

---

## 📄 License

MIT License.

---

## 🌐 About

This repository documents my exploration of Hugging Face’s agent ecosystem — from tool creation to agent loops to code execution.  
It complements my custom agent project (`gemma_agent`) and forms part of my ongoing work in practical AI engineering.
```




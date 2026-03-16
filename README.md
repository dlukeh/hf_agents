# 🤖 HF Agents Workspace  
**Project:** hf_agents  
**Frameworks:** smolagents, LiteLLMModel  
**Focus:** Tool‑using agents, code execution, and Hugging Face’s agent architecture  

This repository contains my full workspace for the Hugging Face Agents Course — including Alfred, my smolagents‑powered agent, along with exercises, experiments, and notebooks that explore tool calling, agent loops, and code‑interpreter workflows.

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
hf_agents/
│
├── alfred/
│   ├── alfred_agent.py        # Main smolagents-based agent
│   ├── smol_alfred.py         # Unit 2.1 experiment (HF course)
│   ├── smol_test.py           # Test harness for agent loop
│   └── batcave_intrusion_report.txt   # Example output artifact
│
├── exercises/                 # Course exercises and experiments
│
├── notebooks/                 # Jupyter notebooks for exploration
│
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




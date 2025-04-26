# One-Year AI Product Management Mastery: Automotive Voice and Embedded LLMs

---

## 👤 About Me

**Name:** Ray Wong

**Career Background:**
- 🛰️ **2015.07 – 2018.05** | IoT Product Manager at a Telecom Operator
- 🚗 **2018.05 – 2022.02** | Big Data DRE (Data-Related Engineering) at Chery Automobile
- 🛫 **2022.02 – 2024.07** | Product Manager at a Startup (Intelligent Cockpit, HUD direction)
- 🔊 **2024.07 – Present** | Senior Multilingual Product Manager at iFLYTEK Automotive Division

Over nearly a decade, I have dedicated myself to the intersection of automotive technology, voice interaction, and intelligent systems.  
From IoT to Big Data, from HUDs to full-stack intelligent cockpits — I’ve always believed that **mobility intelligence is the future of human-machine symbiosis**.

---

## 🛣 Purpose of This Repository

Let's be honest:  
This GitHub repo is not just a study project — it's **a public trial of my own perseverance**.

I aim to transform myself from a "traditional" automotive voice product manager into **an elite AI/LLM-centric Product Leader** in the next era of embedded intelligence, over 52 relentless weeks.

Will I make it?  
Maybe.  
Maybe not.  
But this repo will bear witness to every step of the journey — the sweat, the breakthroughs, the failures, and hopefully, the transformation.

---

## 🎯 End Goals

- Architect intelligent cockpit systems powered by embedded LLMs
- Design multilingual, multimodal, truly natural voice-first experiences
- Master the technologies behind RAG, prompt engineering, agent frameworks, and fine-tuning
- Become a true "voice AI × mobility" domain expert capable of leading future-defining products

---

## 📅 Week 1 — Kickoff: LLM Basics and Foundations

### 🎯 Week 1 Learning Goals

- ✅ Understand LLM API ecosystems (OpenAI, Anthropic, Hugging Face Inference)
- ✅ Build a unified API wrapper for cloud-based and local models
- ✅ Practice prompt engineering fundamentals (few-shot, CoT, JSON, role-playing)
- ✅ Set up the project workspace with clean structure and CI habits
- ✅ Explore LangChain quick-start and connect first simple chains
- ✅ Deploy and run a local LLM (Mistral 7B Instruct GGUF via LM Studio)
- ✅ Produce a basic "Echo Chatbot" as a warm-up mini-project

---

### 🧩 Week 1 Task Breakdown

| Day | Task | Output |
|----|------|--------|
| Day 1 | Set up Python 3.11 / Conda / VSCode / Git | `setup_log.md`, environment.yml |
| Day 2 | Build a unified `ChatWrapper` class | `src/apis.py`, pytest test case |
| Day 3 | Reproduce 3 types of prompt engineering patterns | `notebooks/prompt_patterns.ipynb` |
| Day 4 | Curate 5 practical prompt patterns into Notion or Markdown | `prompt_cards/` directory |
| Day 5 | Build a simple LangChain chatbot with Streamlit | `streamlit_app/app.py` |
| Day 6 | Install LM Studio, run Mistral-7B local inference, benchmark latency | `local_inference_report.md` |
| Day 7 | Integrate APIs + Prompts + Local Model toggle into a "1-page voice concierge" | Mini demo video (.mp4 or .gif) |

---

## 📂 Repo Structure (Planned)

```plaintext
├── src/            # Core Python modules (API wrappers, agents, RAG)
├── notebooks/      # Jupyter Notebooks for experiments
├── projects/       # Weekly mini-projects and milestone demos
├── prompt_cards/   # Curated prompt engineering patterns
├── logs/           # Daily and weekly learning logs
├── assets/         # Images, gifs, demo videos
├── README.md       # This file
└── LICENSE         # MIT License

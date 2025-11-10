# 🔴 RedLLM — Offline Pentest Assistant

**RedLLM** is a beginner-friendly, offline **penetration testing assistant** powered by [Ollama](https://ollama.com).  
It helps students, exam takers, and professionals **learn and simulate security workflows** using local LLMs — safely and without an internet connection.

---

## 🧠 Why RedLLM?

Traditional AI tools require cloud connections and risk leaking data.  
RedLLM runs **completely offline**, using local LLMs (like Llama 3) via Ollama.  
It acts as a teaching partner — explaining pentest steps, suggesting commands, and logging results.

---

## ✨ Features

-  **Offline Operation** — no external API calls, no data leakage.  
-  **Teaching Mode** — beginner guidance for each tool and technique.  
-  **Session Logging** — keeps track of your pentest sessions for review.  
-  **Secure by Default** — `.env` ignored, secrets never exposed.  
-  **Model-Agnostic** — works with any Ollama-compatible LLM (e.g. Llama 3, Mistral, Phi 3).  

---

## Installation

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:samfrazerdutton/RedLLM.git
cd RedLLM
# in RedLLM directory
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt

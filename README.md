# ResearchMind 🧠✨

<img width="960" height="600" alt="Screenshot 2026-10-28 140452" src="https://github.com/user-attachments/assets/41ec8d77-90b7-4b82-8163-17a0e1330f20" />


> **Multi-Agent AI System** that automates deep web research, content scraping, synthesis, and critique to deliver polished research reports on any topic[span_0](start_span)[span_0](end_span).

---

## 🚀 Overview

**ResearchMind** is an advanced multi-agent framework designed to streamline the research process. By orchestrating four specialized AI agents, it transforms a simple query into a comprehensive, high-quality research report[span_1](start_span)[span_1](end_span). 

Whether you are tracking global events, studying new technologies, or conducting market research, ResearchMind automates the heavy lifting of gathering, analyzing, and refining data.

---

## 🤖 The Multi-Agent Pipeline

The system runs a structured, multi-step execution pipeline with four specialized agents:

1. **`01` Search Agent**[span_2](start_span)[span_2](end_span)
   * **Role:** Information Gathering[span_3](start_span)[span_3](end_span)
   * **Action:** Scours the web for recent, highly relevant information, articles, and data points based on your research topic.
2. **`02` Reader / Scraper Agent**[span_4](start_span)[span_4](end_span)
   * **Role:** Content Extraction[span_5](start_span)[span_5](end_span)
   * **Action:** Deep-dives into retrieved URLs, scrapes raw content, and extracts precise text and details.
3. **`03` Writer Chain**[span_6](start_span)[span_6](end_span)
   * **Role:** Content Synthesis[span_7](start_span)[span_7](end_span)
   * **Action:** Synthesizes scraped text, structures arguments, and drafts comprehensive reports.
4. **`04` Critic / Refinement Agent**[span_8](start_span)[span_8](end_span)
   * **Role:** Quality Assurance & Review[span_9](start_span)[span_9](end_span)
   * **Action:** Critiques the draft for accuracy, logical coherence, and depth to produce a polished final deliverable.

---

## ✨ Key Features

* **Multi-Agent Orchestration:** Seamlessly coordinates distinct roles for searching, scraping, writing, and critiquing[span_10](start_span)[span_10](end_span).
* **Interactive UI:** Built with Streamlit (`localhost:8501`)[span_11](start_span)[span_11](end_span) for a clean, futuristic dark-mode dashboard experience.
* **Real-time Pipeline Tracking:** Visually monitor the status (`DONE` / `IN PROGRESS`) of each agent in real-time.
* **Quick Prompts / Examples:** Includes pre-built suggestions (e.g., *"latest new on war and its impact towards inflation and in global trade"*, *"CRISPR gene editing"*)[span_12](start_span)[span_12](end_span) to test the pipeline instantly.

---

## 🛠️ Tech Stack

* **Frontend / UI:** Streamlit[span_13](start_span)[span_13](end_span)
* **Orchestration / Frameworks:** Python, LangChain / Custom Multi-Agent Architectures
* **Tools & APIs:** Web search tools, web scraping modules, and Large Language Models (LLMs)

---

## ⚙️ Getting Started

### Prerequisites
Make sure you have Python 3.10+ installed on your machine.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ResearchMind.git](https://github.com/your-username/ResearchMind.git)
   cd ResearchMind

  pip install -r requirements.txt


   Then, 
   configure environment Variables with api keys 

   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here

   Then launch it using :-

   #streamlit run app.py



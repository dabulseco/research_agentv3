# 🤖 AI Research Agent v3

A **fully local, privacy-first research and writing automation tool** built on CrewAI-orchestrated
AI agents, locally-running large language models (via Ollama), and a headless web browser (via
Selenium). Version 3 adds **six output formats**, **custom resource injection** (URLs and PDFs),
**DOCX export**, **configurable perspective and audience**, and an intelligent **dual-path writer**
that scales from a single page to 10+ pages — all from a simple browser-based interface.

> **No cloud API keys required. Your data never leaves your machine.**

---

## 📋 Table of Contents

- [What's New in v3](#whats-new-in-v3)
- [What This Does](#what-this-does)
- [The Full Workflow — 7 Stages](#the-full-workflow--7-stages)
- [Output Formats](#output-formats)
- [Key Features](#key-features)
- [Platform Support](#platform-support)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Using the App](#using-the-app)
- [Custom Resources — URLs and PDFs](#custom-resources--urls-and-pdfs)
- [Output Length and the Dual-Path Writer](#output-length-and-the-dual-path-writer)
- [Project Structure](#project-structure)
- [Configuration Reference](#configuration-reference)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## What's New in v3

| Feature | v2 | v3 |
|---------|----|----|
| Output formats | Blog post only | 6 formats (blog, paper, essay, brief, NSF proposal, explainer) |
| Export formats | `.md` + `.html` | `.md` + `.docx` (styled Word document) |
| Research context | None | Perspective + audience selection shapes every stage |
| Custom resources | None | Inject URLs and PDFs at any stage; agents treat them as primary sources |
| Writer intelligence | Single-pass only | Dual-path: single-pass (<5K words) or section-by-section (≥5K words) |
| Context window | Fixed | Configurable slider (8K–65K tokens); Ollama primed before each write |
| Web search | Always on | Toggle on/off; option to rely on local LLM only |
| Re-run controls | Not available | Jump back to any stage after adding new resources |
| Agent context awareness | None | All agents receive audience + perspective instructions |

---

## What This Does

You give the app a research topic and configure *who* the output is for and *what perspective* it
should take. The app then autonomously:

1. Creates a structured research plan tailored to your audience and perspective
2. Draws on the local AI model's existing knowledge for an initial report
3. Identifies exactly what information is still missing (gap analysis)
4. Searches the live web to fill those gaps (or skips web search if disabled)
5. Selects an output format and target length
6. Writes the complete document — handling long outputs section by section if needed
7. Exports the final document as a styled **Word `.docx`** file and/or Markdown

All AI processing runs through **Ollama** — nothing is sent to OpenAI, Anthropic, or any
external AI service.

---

## The Full Workflow — 7 Stages

The app follows a structured pipeline managed by [CrewAI](https://www.crewai.com/), which
coordinates multiple specialized AI agents. Each stage shows its results and waits for your
approval before continuing — giving you full control over the process.

```
Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4 → Stage 45 → Stage 5
Context   Plan +    Gap       Web       Output    Write &
Setup     Research  Analysis  Research  Format    Download
```

> Note: The internal stage numbering jumps from 4 to 45 before reaching 5. This is intentional —
> stage 45 is the output format selection screen that sits between web research and writing.

---

### Stage 0 — Research Context Setup

Before any research begins, you configure two key parameters that shape every subsequent step:

**Perspective / Voice** — how the research is framed. Options include:
- Neutral / Objective
- Skeptical Scientist
- Science Communicator
- Policy Advocate
- Industry Practitioner
- Educator / Teacher
- Investor / Business Strategist
- Custom (free text)

**Target Audience** — who will read the final output. Options include:
- General Public
- Graduate / Doctoral Students
- Domain Experts / Researchers
- Policymakers / Government Officials
- Funding Agencies (NSF / NIH / DOE)
- Industry Professionals
- Undergraduate Students
- Custom (free text)

**Framing Notes** — optional free-text instructions (e.g., *"Emphasise economic impacts over
technical details"* or *"Assume reader is sceptical of AI claims"*).

These settings are injected as a `CONTEXT CONFIGURATION` block into every agent's task
description throughout the entire workflow.

---

### Stage 1 — Research Plan + Initial Research

Two agents run in sequence:

**Research Request Interpreter** — reads your topic and context, then produces a structured
research plan in JSON format:
- 3–5 main research questions framed for your audience
- Key topics to investigate
- Suggested search queries
- Topics already covered by any uploaded resources (so later steps don't duplicate that work)

**Knowledge Researcher** — uses the local model's built-in knowledge to write a first-pass
research report covering all topics in the plan, pitched at the specified audience and framed
from the specified perspective.

You can review both outputs and either proceed or redo from this stage.

---

### Stage 2 — Gap Analysis

**Research Gap Analyst** — compares the research plan against the initial research report and
identifies:
- Information that is missing or unanswered
- Topics where data might be outdated
- Areas requiring recent statistics or web-sourced evidence
- Optimized search queries to fill each gap, with priority ratings (high/medium/low)

If custom resources were uploaded, the agent is explicitly instructed *not* to flag topics they
cover as gaps — only genuinely missing information is targeted.

---

### Stage 3 — Web Research

**Web Research Specialist** — performs targeted web searches using the queries from the gap
analysis. Supports two backends:

- **Selenium** (headless Chrome or Firefox) — searches Google first, falls back to Bing
- **DuckDuckGo API** — no browser required; may be rate-limited under heavy use

The agent focuses on 2–3 highest-priority gaps, documents any search failures, and compiles
all findings with source citations.

Web search can be **disabled entirely** in the sidebar — the workflow will skip this stage and
proceed using only the initial research and any uploaded resources.

---

### Stage 45 — Output Format & Length Selection

Before writing begins, you choose:

- **Output format** — one of six structured templates (see [Output Formats](#output-formats))
- **Target length** — from ~500 words (1 page) to ~5,000 words (10 pages), or a custom target

The app then routes automatically to the correct writing path based on the word count target.

---

### Stage 5 — Write & Download

The **writer agent** receives all research, context, resources, and format instructions, then
produces the complete document. The output is shown as a live preview in the app and available
for immediate download as:

- **`.docx`** — fully styled Word document (headings, bold, italics, lists, horizontal rules)
- **`.md`** — Markdown file for note-taking apps, GitHub, Obsidian, etc.

---

## Output Formats

Each format uses a dedicated agent role, goal, backstory, and structural guidance — producing
genuinely different outputs, not just the same content with a different heading.

| Format | Agent Role | Structure |
|--------|-----------|-----------|
| **Blog Post** | Science Communicator and Technical Writer | Hook intro → sections with headers → conclusion |
| **Research Paper** | Academic Research Writer | Abstract → Introduction → Background → Methods → Findings → Discussion → Conclusion → References |
| **Essay** | Essayist and Analytical Writer | Thesis → evidence-backed body → counter-arguments → strong conclusion |
| **Executive Summary / Briefing** | Policy Analyst and Strategic Communications Expert | Key Findings → Background → Analysis → Recommendations → Conclusion |
| **NSF-Style Grant Proposal** | Grant Writing Specialist | Project Summary → Introduction → Background → Objectives → Approach → Intellectual Merit → Broader Impacts → Timeline |
| **Explainer / Educational Article** | Science Educator and Explainer Writer | Big picture → core concepts → deep dive → examples → key takeaways |

---

## Key Features

- **Fully local AI** — runs any Ollama-compatible model (LLaMA, Gemma, Mistral, Qwen, etc.)
- **Six output formats** — from blog posts to NSF grant proposals, each with its own agent persona
- **Custom resource injection** — paste URLs or upload PDFs; agents treat them as authoritative primary sources
- **DOCX export** — styled Word document with headings, bold, italics, lists, and horizontal rules
- **Audience + perspective configuration** — shapes every agent's framing from plan to final draft
- **Dual-path writer** — single-pass for short documents; section-by-section for 5,000+ word outputs
- **Configurable context window** — slider from 8K to 65K tokens; Ollama is primed before each write call
- **Web search toggle** — disable entirely for offline/privacy use; agents fall back to LLM knowledge
- **Re-run controls** — after adding a resource mid-workflow, jump back to any prior stage to reincorporate it
- **Human-in-the-loop** — review and approve every stage before proceeding
- **MacOS Apple Silicon support** — M1/M2/M3 compatible with Chrome and Firefox headless modes
- **Cross-platform** — Windows 11 and MacOS tested; Linux should work with Chrome/Firefox installed

---

## Platform Support

| Platform | Status |
|----------|--------|
| Windows 11 | ✅ Tested |
| macOS Apple Silicon (M1/M2/M3) | ✅ Tested |
| macOS Intel | 🔄 Should work, not explicitly tested |
| Linux | 🔄 Should work with Chrome/Firefox installed |

---

## Technology Stack

| Component | Library / Tool | Purpose |
|-----------|---------------|---------|
| **AI Orchestration** | [CrewAI](https://www.crewai.com/) | Coordinates multiple AI agents into a structured workflow |
| **Local LLM** | [Ollama](https://ollama.ai/) | Runs AI language models locally on your hardware |
| **LLM Interface** | [LangChain + langchain-ollama](https://python.langchain.com/) | Connects CrewAI agents to local Ollama models |
| **Web UI** | [Streamlit](https://streamlit.io/) | Browser-based interface for the entire app |
| **Browser Automation** | [Selenium](https://selenium.dev/) | Drives headless Chrome/Firefox for web search |
| **Browser Management** | [webdriver-manager](https://pypi.org/project/webdriver-manager/) | Auto-installs the correct browser driver version |
| **Web Scraping** | [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) | Extracts clean article text from URLs |
| **PDF Extraction** | [pdfplumber](https://pypi.org/project/pdfplumber/) + [PyMuPDF](https://pypi.org/project/pymupdf/) | Extracts and chunks text from uploaded PDF files |
| **DOCX Generation** | [python-docx](https://python-docx.readthedocs.io/) | Converts Markdown output to styled Word documents |
| **Fallback Search** | [duckduckgo-search](https://pypi.org/project/duckduckgo-search/) | API-based search without requiring a browser |
| **HTTP Requests** | [requests](https://pypi.org/project/requests/) | Fetches web page content for resource injection |

---

## Prerequisites

You need the following installed before setting up this project:

### 1. Python 3.10 or higher
- **Check:** `python --version`
- **Download:** https://www.python.org/downloads/

### 2. Ollama (local AI model runner)
Ollama runs AI language models directly on your computer — no internet connection needed once
models are downloaded.

- **Install:** https://ollama.ai/download
- **Check it's running:** `ollama list`

After installing Ollama, pull at least one language model. Larger models produce better output
quality but require more RAM:

```bash
ollama pull llama3.2          # ~2 GB  — works on 8 GB RAM; good for testing
ollama pull gemma3:12b        # ~8 GB  — better quality; needs 16 GB RAM
ollama pull qwen2.5:14b       # ~9 GB  — excellent at structured output and long documents
ollama pull llama3.1:70b      # ~40 GB — high quality; requires 48+ GB RAM or GPU
```

> 💡 **For long documents (5,000+ words):** Use the largest model your hardware supports.
> The section-by-section writer can produce long outputs on smaller models, but quality
> improves significantly with larger models.

### 3. Google Chrome or Mozilla Firefox
Needed if you use Selenium-based web search. At least one must be installed.

- **Chrome:** https://www.google.com/chrome/ (use ARM version on Apple Silicon)
- **Firefox:** https://www.mozilla.org/firefox/

> Web search can be disabled in the sidebar if you prefer not to install a browser.

### 4. Git (to clone the repository)
- **Download:** https://git-scm.com/downloads

---

## Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/dabulseco/research_agentv3.git
cd research_agentv3
```

### Step 2 — Create a virtual environment (strongly recommended)

A virtual environment keeps this project's dependencies isolated from other Python projects.

```bash
# Create the virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS / Linux:
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt.

### Step 3 — Install Python dependencies

```bash
pip install -r requirements.txt
```

> This may take several minutes. If you see build errors on Windows, install the
> [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
> On macOS, run `xcode-select --install` if prompted.

### Step 4 — Verify Ollama is running

Open a **separate terminal** and start Ollama if it isn't already:

```bash
ollama serve
```

Confirm you have at least one model installed:

```bash
ollama list
```

---

## Running the Application

With your virtual environment activated and Ollama running:

```bash
streamlit run app.py
```

Your browser will open automatically to **http://localhost:8501**

If it doesn't open, navigate there manually.

---

## Using the App

### Sidebar Settings

Configure these before or during your research session:

| Setting | Options | Notes |
|---------|---------|-------|
| **AI Model** | Dropdown of installed Ollama models | Auto-detected from your local Ollama installation |
| **Writer Context Window** | 8K – 65K tokens (slider) | 32K works for most outputs; reduce to 16K if RAM-limited |
| **Enable Web Search** | On / Off | Disable for offline use or to rely on LLM knowledge only |
| **Search Method** | Selenium / DuckDuckGo | Selenium is more reliable; DuckDuckGo is faster |
| **Browser** | Chrome / Firefox | Visible only when Selenium is selected |

### Step-by-Step Workflow

**Stage 0 — Research Context**
1. Select your **Perspective** (e.g., Science Communicator, Policy Advocate)
2. Select your **Target Audience** (e.g., Funding Agencies, General Public)
3. Optionally add **Framing Notes** for specific guidance
4. Enter your **research topic** in the text box
5. Click **🚀 Start Research**

**Stage 1 — Review Research Plan and Initial Research**
- Read the research plan and initial LLM-based report
- Click **✅ Proceed to Gap Analysis** if satisfied, or **🔄 Redo** to regenerate

**Stage 2 — Review Gap Analysis**
- Read the identified gaps and proposed search queries
- Proceed or regenerate

**Stage 3 — Review Web Research** *(skipped if web search is disabled)*
- Read the findings from web searches
- Proceed or regenerate

**Stage 45 — Choose Output Format and Length**
- Select from 6 output formats (see [Output Formats](#output-formats))
- Choose a target length: 500 / 1,000 / 2,500 / 5,000 words, or custom
- Click **✅ Generate Output**

**Stage 5 — Download Your Document**
- Preview the complete output in the browser
- Download as **📥 DOCX** (styled Word file) or **📥 Markdown**
- Click **🔄 Redo Output** to regenerate with the same settings
- Click **🔙 Change Format / Length** to go back and try a different format

### Tips for Best Results

- **Be specific with your topic** — include years, domains, and specific questions
  - ✅ Good: *"Impact of AI tutoring on community college student outcomes Hawaii 2023–2025"*
  - ❌ Weak: *"AI in education"*
- **Choose your audience carefully** — it dramatically changes the depth and vocabulary of the output
- **For NSF proposals**, set Perspective to *"Grant Writing Specialist"* and Audience to *"Funding Agencies"*
- **For very long documents** (5,000+ words), use the largest model your hardware supports
- **Upload key papers as PDFs** before starting — agents will treat them as authoritative sources
- **The web search toggle** is useful when: researching offline, working with sensitive topics, or
  when your topic is well-covered by uploaded PDFs

---

## Custom Resources — URLs and PDFs

One of v3's most powerful features is the ability to inject your own source materials into the
research pipeline at any point.

### Adding a URL

In the sidebar **📎 Research Resources** panel:
1. Paste a URL into the text field
2. Click **➕ Add URL**
3. The app scrapes the page (up to ~4,000 words), removes navigation and boilerplate, and stores the clean article text

### Uploading a PDF

1. Click **Upload a PDF** in the sidebar
2. Select your PDF file
3. Click **➕ Add PDF**
4. Large PDFs are automatically chunked into ~1,000-word sections (up to ~20,000 words total)

### How Resources Are Used

Once added, all resources are formatted into a `CUSTOM RESOURCES` block and injected directly into
every agent's task description for all remaining stages. Agents are explicitly instructed to:
- Treat them as authoritative primary sources
- Cite them explicitly in the final output
- Not duplicate web searches for topics they already cover

### Adding Resources Mid-Workflow

You can add resources at any point — even after web research is complete. When you do, the sidebar
shows re-run buttons so you can reincorporate the new material:

| Button | What It Resets and Re-Runs |
|--------|---------------------------|
| **🔁 Re-run from Output Writing** | Regenerates the final document only |
| **🔁 Re-run from Web Research** | Reruns web research + output writing |
| **🔁 Re-run from Gap Analysis** | Reruns gap analysis, web research, and output writing |
| **🔁 Re-run from Initial Research** | Reruns everything from Stage 1 onward |

### Removing Resources

Each resource in the list has a **✕** button to remove it. Removing a resource does not
automatically re-run earlier stages — use the re-run buttons if needed.

---

## Output Length and the Dual-Path Writer

The app automatically chooses between two writing strategies based on your target word count:

### Single-Pass Writing (targets under 5,000 words)

One CrewAI crew call produces the entire document in a single pass. The agent receives all
research material at once and writes the complete output from start to finish.

Best for: blog posts, executive summaries, short explainers, and essays up to ~4,999 words.

### Section-by-Section Writing (targets 5,000 words and above)

For long documents, the app splits the output into sections (6–8 per format) and runs a
separate CrewAI crew call for each one. Each call:
- Receives a compressed summary of all research material (~7,000 tokens)
- Knows its position in the document (first / middle / last)
- Receives the last ~400 words of previous sections as a continuity anchor
- Is told exactly how many words to write for that section

This prevents context overflow and ensures each section is fully developed rather than
truncated. The sections are then joined into a single coherent document.

Best for: research papers, NSF proposals, comprehensive explainers, and any output over 10 pages.

### Context Window Configuration

The sidebar **Writer Context Window** slider sets how many tokens the writer agent can use
(input + output combined). The app primes Ollama with a direct REST call before each write
operation — this is necessary because CrewAI's internal routing silently drops context window
settings passed as parameters.

| Setting | Best For |
|---------|---------|
| 8K tokens | Very short outputs on RAM-limited hardware |
| 16K tokens | Short to medium outputs (up to ~2,500 words) |
| 32K tokens (default) | Most use cases; handles 5,000+ word outputs |
| 49K–65K tokens | Very long documents on hardware with 24+ GB VRAM |

---

## Project Structure

```
research_agentv3/
│
├── app.py              # The entire application — all agents, tools, UI, and utilities
├── requirements.txt    # All Python package dependencies
└── README.md           # This file
```

### Inside `app.py` — Major Sections

| Section / Class | What It Does |
|-----------------|-------------|
| **Environment setup** | Sets dummy OpenAI key (required by CrewAI even for local models), disables telemetry |
| **Session state init** | Initializes all Streamlit variables that persist between button clicks and page interactions |
| **`FORMAT_TEMPLATES` dict** | Defines agent role, goal, backstory, and structure guidance for each of the 6 output formats |
| **`TEMPLATE_SECTIONS` dict** | Defines the ordered list of section names used by the section-by-section writer for each format |
| **`build_context_block()`** | Assembles the perspective/audience/framing block injected into every agent task |
| **`build_resources_block()`** | Assembles all uploaded URL and PDF content into a formatted block for agent injection |
| **`scrape_url()`** | Fetches a URL, strips navigation/scripts/footers, returns clean article text (up to 4,000 words) |
| **`extract_pdf()`** | Extracts text from a PDF using pdfplumber; chunks large documents into ~1,000-word sections |
| **`render_resource_panel()`** | Renders the persistent sidebar resource manager (URL input, PDF uploader, resource list, re-run buttons) |
| **`get_installed_ollama_models()`** | Queries local Ollama installation and returns available model names for the dropdown |
| **`get_llm()`** | Initializes and caches the OllamaLLM object with 8K context and 2K prediction window |
| **`SeleniumSearcher` class** | Manages headless Chrome or Firefox; searches Google first, falls back to Bing |
| **`WebSearchTool` class** | CrewAI-compatible tool wrapping both Selenium and DuckDuckGo search backends |
| **`step1_interpret_and_plan()`** | CrewAI crew: Research Request Interpreter agent creates a structured research plan |
| **`step2_initial_research()`** | CrewAI crew: Knowledge Researcher agent writes initial report from LLM knowledge |
| **`step3_gap_analysis()`** | CrewAI crew: Research Gap Analyst identifies missing information and generates search queries |
| **`step4_web_research()`** | CrewAI crew: Web Research Specialist searches the web and compiles findings |
| **`_parse_target_word_count()`** | Parses the output length string into a numeric word count for routing decisions |
| **`_prime_ollama_context()`** | Sends a direct REST request to Ollama to pre-load the model with the desired context window size |
| **`_markdown_to_docx()`** | Converts Markdown text to a styled `.docx` file — handles headings, bold, italic, code, lists, and horizontal rules |
| **`step5_write_output()`** | Format-aware, length-aware writer: routes to single-pass or section-by-section depending on word count target |
| **`main()`** | Streamlit UI: sidebar, all 7 workflow stages, download buttons, and reset controls |

---

## Configuration Reference

All settings are managed through the app's sidebar UI. The following values are hardcoded in
`app.py` and can be changed directly in the source if needed:

| Location in `app.py` | Default Value | What It Controls |
|----------------------|---------------|-----------------|
| `get_llm()` — `num_ctx` | `8192` | Context window for non-writer agents (research, gap analysis) |
| `get_llm()` — `num_predict` | `2048` | Max tokens non-writer agents can generate per call |
| `get_llm()` — `temperature` | `0.7` | LLM creativity (0 = deterministic, 1 = very creative) |
| `get_llm()` — `base_url` | `http://localhost:11434` | Ollama server address; change if running on a different port |
| `scrape_url()` — word limit | `4000` words | Max words extracted from each URL |
| `extract_pdf()` — word limit | `20,000` words | Max words extracted from each PDF |
| `extract_pdf()` — chunk size | `1000` words | Size of each PDF chunk for large documents |
| `step4_web_research()` — `max_iter` | `10` | Max search iterations per web research run |
| Sectional writer threshold | `5000` words | Word count above which section-by-section writing activates |
| `TEMPLATE_SECTIONS` | 6–8 sections per format | Section names and count for the section-by-section writer |

---

## Troubleshooting

### "No Ollama models found" / Ollama errors

```bash
# Start the Ollama server
ollama serve

# Confirm models are installed
ollama list

# Pull a model if the list is empty
ollama pull llama3.2
```

### Chrome / Selenium fails to launch

- Try switching to **Firefox** in the sidebar
- On macOS Apple Silicon: install Chrome for ARM from https://www.google.com/chrome/
- Switch search method to **DuckDuckGo** (no browser required)
- Disable web search entirely and proceed with local LLM knowledge

### PDF upload not working

Make sure `pdfplumber` installed correctly:
```bash
pip install pdfplumber pymupdf
```
Scanned PDFs (images of text) will extract little or no text — they require OCR, which is not
currently included.

### Writer produces a short or incomplete document

This usually means the model's context window is too small for the amount of research material.
Try:
1. Increase the **Writer Context Window** slider in the sidebar (try 49K or 65K)
2. Switch to the **section-by-section** path by choosing a target of 5,000+ words
3. Use a larger model if your hardware allows

### "OPENAI_API_KEY" errors

This is expected and handled automatically. CrewAI requires the environment variable to exist
even when using Ollama. The app sets a dummy value at startup — no real OpenAI key is needed.

### pip install errors (build failures)

- **Windows:** Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **macOS:** Run `xcode-select --install`
- **All platforms:** Make sure you are running Python 3.10+

### Research is very slow

Normal — each CrewAI agent call can take 2–15 minutes depending on:
- Model size (larger = slower but better quality)
- Your hardware (CPU is much slower than GPU)
- Number of web searches performed
- Target output length

For faster iteration during testing, use `llama3.2` and set target length to ~500 words.

---

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software for any purpose, including commercial
use, as long as the original copyright notice is preserved.

---

*Built with CrewAI · Ollama · Streamlit · Selenium · python-docx · pdfplumber · Python*

*All AI processing is local — your research and your documents stay on your machine.*

# LangChain Runnable Patterns

A hands-on exploration of **5 essential Runnable patterns in LangChain LCEL (LangChain Expression Language)** using Python and Google Gemini.

This repository demonstrates how different Runnable components work individually and how they can be combined to build structured and flexible LLM workflows.

## 🚀 Overview

LangChain Runnables provide a flexible way to connect, organize, and execute different steps in an LLM application.

This repository covers five essential Runnable patterns:

## 📚 Concepts Covered

| Runnable | Description |
|---|---|
| **RunnableSequence** | Connects multiple steps sequentially, where the output of one step becomes the input of the next. |
| **RunnableParallel** | Executes multiple independent tasks simultaneously using the same input. |
| **RunnablePassthrough** | Passes input data forward without modifying it. |
| **RunnableLambda** | Integrates custom Python functions into an LCEL workflow. |
| **RunnableBranch** | Routes execution dynamically based on runtime conditions. |

## 📂 Project Structure

```text
LangChain-Runnable-Patterns/
│
├── 01_runnable_sequence.py
├── 02_runnable_parallel.py
├── 03_runnable_passthrough.py
├── 04_runnable_lambda.py
├── 05_runnable_branch.py
│
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain Expression Language (LCEL)
- Google Gemini
- Rich
- python-dotenv

## ⚙️ Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/JiyaSheikh06/langchain-runnable-patterns.git
cd LangChain-Runnable-Patterns
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

**5. Run the examples**

Execute each Python file individually:

```bash
python 01_runnable_sequence.py
python 02_runnable_parallel.py
python 03_runnable_passthrough.py
python 04_runnable_lambda.py
python 05_runnable_branch.py
```

## 💡 Key Learnings

- Understanding how LangChain Runnable components work.
- Building sequential and parallel workflows.
- Passing and preserving data between different steps.
- Integrating custom Python functions into LLM workflows.
- Implementing conditional execution and dynamic routing.
- Exploring the LCEL pipe operator (`|`) as a concise way to compose Runnable sequences.

## 🎯 Purpose

This repository is part of my hands-on learning journey with LangChain and Generative AI.

The goal is to understand how individual Runnable patterns work and how they can be combined to create more organized and flexible LLM workflows.

## 🤝 Feedback & Contributions

Suggestions, feedback, and discussions are always welcome!

If you find this repository useful, consider giving it a ⭐.

---

## 👩‍💻 Author

**Jiya Sheikh**

GitHub: [@JiyaSheikh06](https://github.com/JiyaSheikh06)
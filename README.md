# 🤖 DevHands

**DevHands** is your personal AI Software Engineer. It’s a fully autonomous CLI-based agent that can:

- 🔍 Analyze and refactor existing codebases using SOLID principles
- 🏗️ Build full application MVPs from a user-defined spec
- 🧠 Use LangChain to manage prompts, memory, tools, and agents
- 🧪 Debug, test, and package your project as a production-ready Docker container
- 📁 Suggest architecture improvements in diff format with minimal token cost

---

## ✨ Features

- ✅ Clean Architecture (SOLID)
- 🔧 LangChain-based agentic workflows
- 🗂️ Directory & file structure generation
- 🐳 Docker-ready output
- 🧪 Testing, CI/CD, and traceability built-in
- 🔐 Configurable, secure, and extensible
- 🧠 Optimized for large context and LangGraph memory

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-org/devhands.git
cd devhands
python create_devhands_structure.py
poetry install
poetry run python -m devhands.main
```

---

## 📦 Architecture Overview

```text
devhands/
├── devhands/           # App logic (core, domain, infrastructure, cli)
├── tests/              # Test modules
├── scripts/            # Helper scripts
├── ci/                 # CI/CD configs (GitHub Actions, etc.)
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── .env.example
├── .gitignore
└── README.md
```

---

## 👥 Contributing

We’re building an open and modular Agentic AI development toolkit. If you're passionate about:

- LangChain and AI workflows
- Clean, maintainable architecture
- Building with agents, not just prompts

...then **we want you!** 💙

### How to contribute

- Fork the repo
- Create a new branch (`git checkout -b feature/your-idea`)
- Add your code
- Submit a PR with clear intent and tests

We encourage contributions from developers, AI researchers, prompt engineers and all curious minds!

---

## 📄 License

MIT – use it, fork it, make magic with it.

---

## 🧠 Powered By

- [LangChain](https://www.langchain.com/)
- [LangGraph](https://www.langchain.com/langgraph)
- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/)

---

## ✉️ Stay in Touch

Follow the project and share your thoughts:

- GitHub Issues → Feature ideas & bug reports
- Discussions → Brainstorming & help
- PRs → New tools, workflows, or templates

Together, we’ll build tools that build tools.

**Let’s build DevHands into a real AI engineer.**


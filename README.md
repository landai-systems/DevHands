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

## 🚀 Getting Started (Locally)

```bash
git clone https://github.com/your-org/devhands.git
cd devhands
cp .env.example .env  # Add your OpenAI API key here
poetry install
poetry run python devhands/main.py
```

---
## 🐳 Getting Started (Docker)
### 📦 Build and run CLI interactively
```bash
docker-compose run --rm devhands
```
Make sure .env is set up and contains your OpenAI API key.

### 🧪 Run all tests inside container
```bash
docker-compose run --rm test
```

### 🧰 Dev shell (optional)
```bash
docker-compose run --rm devhands bash
```
You’ll find generated apps under generated_apps/ (volume-mounted on your host).

---

## 📦 Architecture Overview
```text
devhands/
├── devhands/           # App logic (core, domain, infrastructure, cli)
├── tests/              # Unit tests for all modules
├── scripts/            # Shell helpers for lint, test, format
├── ci/                 # GitHub Actions, CI configs
├── Dockerfile          # Container definition
├── docker-compose.yml  # Local development runner
├── pyproject.toml      # Poetry-based dependency management
├── .env.example        # Env variable template
├── .gitignore
└── README.md
```

---

## 🧑‍💻 How to contribute
```bash
# Fork and clone your fork
git clone https://github.com/your-username/devhands.git
cd devhands

# Create your feature branch
git checkout -b feature/your-idea

# Make changes and test
poetry run pytest

# Commit and push
git commit -m "Add awesome new feature"
git push origin feature/your-idea

# Open a Pull Request!
```
We encourage contributions from developers, AI researchers, prompt engineers and all curious minds!

---

## 📄 License
MIT – use it, fork it, make magic with it.

---

## ✉️ Stay in Touch
Follow the project and share your thoughts:

GitHub Issues → Feature ideas & bug reports

Discussions → Brainstorming & help

PRs → New tools, workflows, or templates

Together, we’ll build tools that build tools.

__Let’s build DevHands into a real AI engineer.__

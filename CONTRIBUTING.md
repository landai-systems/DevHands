# **Contributing to DevHands**

First off, thanks for taking the time to contribute!   
DevHands thrives on community support from developers, AI researchers, and curious minds like you.

---

##  Getting Started

1. **Fork the Repository**  
   Click “Fork” on the top right of [DevHands GitHub repo](https://github.com/landai-systems/devhands).

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/devhands.git
   cd devhands
   ```

3. **Install dependencies**
You'll need Python 3.10+ and Poetry.

   ```bash
   cp .env.example .env   # Add your OpenAI API key
   poetry install
   ```
4. **Run the App Locally**

   ```bash
   poetry run python devhands/main.py
   ```

5. **Run Tests**

   ```bash
   poetry run pytest
   ```
---
## Working with Docker (optional)
If you prefer containers:

* Run DevHands interactively

```bash
docker-compose run --rm devhands
```

* Run all tests

```bash
docker-compose run --rm test
```

* Dev shell

```bash
docker-compose run --rm devhands bash
```
---
## Making Changes
1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

2. Make Your Changes

Add your awesome code. Follow SOLID principles and prefer clean architecture.

3. Format & Lint (optional)

```bash
./scripts/lint.sh
./scripts/format.sh
```

4. Test Before Commit

```bash
poetry run pytest
```

5. Commit & Push

```bash
git add .
git commit -m "Your clear, concise commit message"
git push origin feature/your-feature-name
```
---
## Submitting a Pull Request
* Go to your fork on GitHub.
* Click “Compare & Pull Request.”
* Fill out the PR template (if available) and describe your changes.
* Submit the PR! 

#### We’ll review it, offer feedback if needed, and merge if everything looks good.
---
## Need Ideas?
* Open GitHub [Issues](https://github.com/landai-systems/devhands/issues)
* Join [Discussions](https://github.com/landai-systems/devhands/discussions)
---
## Contribution Areas
* AI Agent Workflows (LangChain, LangGraph)
* Prompt Engineering
* Code Refactoring Tools
* Testing and CI/CD
* Docker & Deployment
* UI/UX (CLI Enhancements)
* Docs & Tutorials
---
## Code of Conduct
> Be kind. Be constructive. Help us build an inclusive AI engineering toolset.
---
**HAPPY CODING**


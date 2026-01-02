# AI4DevOps: Multi-Agent LLMs for CI/CD Automation

## Project Overview
This project explores the use of multi-agent Large Language Models (LLMs) to automate collaborative DevOps workflows.  
Agents will handle tasks like managing JIRA tickets, creating/testing code in GitHub, and triggering Jenkins builds.

**Objective:**
- Build a proof-of-concept pipeline: GitHub → Jenkins → JIRA ticket updates.
- Introduce multi-agent collaboration (Issue Agent, Code Agent, Deployment Agent).
- Evaluate reliability, security, and workflow efficiency.

---

## Tools & Frameworks
- **Jenkins** – CI/CD automation  
- **GitHub** – Source code management  
- **JIRA** – Issue tracking  
- **Python** – Agent scripting & orchestration  
- **LangChain / AutoGen / CrewAI** – Multi-agent LLM frameworks  

---

## Repo Structure
```
ai4devops/
├── agents/             # AI agent scripts
│   ├── issue_agent.py  # Reads JIRA tickets and suggests tasks
│   ├── code_agent.py   # Generates/modifies GitHub code
│   ├── deploy_agent.py # Triggers Jenkins builds and deployments
│   ├── graphy.py       # LangGraph orchestration logic
│   ├── state.py        # Agent state definitions
│   └── jira_utils.py   # JIRA API utility functions
├── pipeline/           # Pipeline configuration
│   ├── Jenkinsfile     # Main pipeline file
│   └── pipeline_lib/   # Optional helper scripts for Jenkins
├── docs/               # Documentation and diagrams
│   ├── architecture.md # Architecture diagrams of pipeline and agents
│   ├── setup.md        # Step-by-step setup instructions
│   └── sprint_notes/   # Notes and deliverables per sprint
├── tests/              # Sample tests for pipeline or agents
│   ├── test_agent.py   # Unit tests for agent scripts
│   └── test_pipeline.sh# Shell scripts for Jenkins test runs
├── research/           # Research & learning materials
│   └── jira_test.py    # JIRA integration test script
├── README.md           # Project overview and instructions
├── LICENSE             # License file
├── requirements.txt    # Python dependencies for agents
├── .env                # Environment variables for agents (Not committed)
└── .gitignore          # Git ignore file
```

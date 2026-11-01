# Welcome to DE agentic AI harness
DE Agentic is an AI harness comprising agents and skills useful in data engineering.

# Agents
## Agents as building blocks for your harness
The suggested agents are general-purpose. I recommend customizing their instructions to fit your project. If you have several projects, create branches in your local copy of this repository.

## Meet the agents
### Data Analyst
Data Analyst is a human-persona agent that supports data analysis and modeling tasks that lay the groundwork for further data engineering work. The `iterate-table` skill was created to work with this agent.

### AI Engineer
AI Engineer is a human-persona agent that helps define other agents, skills, and workflows, as well as keep the repository tidy and readable for the AI harness.

### Streamliner
Streamliner’s sole purpose is to streamline the harness elements and prompts, reducing token usage and making sessions more efficient. The `streamline` skill was created to work with this agent.

# Skills
The skills listed here are ones I created or modified (e.g., `handoff-ws`, based on Matt Pocock’s work: https://www.aihero.dev/). They don’t represent the entire effective harness, but I’d rather avoid plagiarism than include others’ work just to make this offering complete.

# Kilo and GitHub
For now, I’m testing my harness in these two ecosystems, which is why I’ve defined it only for them. If you use another ecosystem (e.g., Claude), ask the main agent to adapt the AI Engineer for it, then use the AI Engineer to adapt the others. Feel free to fork this repository and contribute versions of the agents tailored to your ecosystem.
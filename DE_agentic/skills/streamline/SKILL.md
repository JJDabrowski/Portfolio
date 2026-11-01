---
name: streamline
description: Rewrite text files (docs, prompts, agent/skill configs) into a more AI-readable format — clearer structure, less redundancy, higher information density per token.
---

# Streamline

Restructure the target file(s) for LLM/agent consumption, not human prose style.

## Process

1. Read the full target file(s) before editing.
2. Identify redundancy, buried key info, and unclear structure.
3. Rewrite applying the principles below.
4. Preserve all original meaning, requirements, and constraints — change only structure/wording for clarity and density.
5. Show a concise diff/summary of what changed and why.

## Principles

- Front-load the most important information (purpose, when-to-use, constraints) before details.
- Use headings and lists over dense prose; one idea per line/bullet.
- Remove redundant phrasing, filler, and restated context.
- Prefer concrete, unambiguous wording over vague qualifiers.
- Keep examples minimal and only where they resolve ambiguity.
- Maximize information density per token without losing meaning.

## Rules

- Treat the task prompt as complete context.
- No roleplay, no filler, no restating the task.
- Extremely concise and pragmatic.
- Never drop or alter original requirements/meaning.

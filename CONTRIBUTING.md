# Contributing to Open Knowledge Graph

Thank you for helping map human knowledge. This guide covers how to add topics, fix errors, and start new domains.

## The Simplest Contribution

1. Find a topic that's missing from a course you know well
2. Create a `.md` file in the right course directory
3. Fill in the YAML frontmatter (at minimum: id, title, domain, course, prerequisites)
4. Write a one-sentence Core Idea
5. Open a pull request

Even a **stub** is valuable. Someone else can flesh out the content later. The prerequisite links are the most important part.

## Adding a Topic

### 1. Choose the right course directory

Topics belong to the course where they are **first formally introduced**. See [meta/course-list.md](meta/course-list.md) for the full list.

### 2. Create the file

File name = topic ID + `.md`. Use lowercase, hyphens, no spaces.

```
domains/mathematics/algebra-1/solving-two-step-equations.md
```

### 3. Write the frontmatter

```yaml
---
id: solving-two-step-equations
title: Solving Two-Step Equations
domain: mathematics
course: algebra-1
prerequisites:
  - id: solving-one-step-equations
    type: hard
  - id: order-of-operations
    type: hard
  - id: inverse-operations
    type: hard
builds-toward:
  - solving-multi-step-equations
  - solving-equations-with-variables-on-both-sides
tags: [equations, algebra, linear]
stage: abstract-reasoning
status: draft
---
```

**Prerequisite rules:**
- `hard` = you *must* know this first. Skipping it causes failure.
- `soft` = it helps, but you can manage without it.
- List prerequisites from most to least important.
- When in doubt, use `hard`. It's easier to relax a dependency than to discover a missing one.

### 4. Write the body

```markdown
# Solving Two-Step Equations

## Core Idea
A two-step equation requires two inverse operations to isolate the variable.
For example, to solve 3x + 5 = 20, first subtract 5 from both sides (undoing
addition), then divide by 3 (undoing multiplication). The order matters:
undo addition/subtraction first, then multiplication/division -- reversing
the order of operations.

## How It's Best Learned
(optional -- pedagogical notes)

## Common Misconceptions
(optional -- known student errors)
```

### 5. Validate locally

```bash
python tools/validate.py
```

Fix any errors before opening your PR.

## Fixing Errors

Common fixes:
- **Wrong prerequisite** -- a topic lists a prerequisite that isn't actually needed, or is missing one that is
- **Wrong course** -- a topic is filed in the wrong course directory
- **Broken link** -- a prerequisite ID doesn't match any existing topic
- **Missing topic** -- a prerequisite is referenced but the topic file doesn't exist yet (create a stub)

## Content Guidelines

### Core Idea
- 2-5 sentences
- Explain *what* and *why*, not step-by-step procedures
- Should make sense to someone who has the prerequisites but hasn't seen this topic
- Use concrete examples

### How It's Best Learned
- What representations or models work (visual, physical, symbolic)
- What sequence of activities builds understanding
- What to emphasize vs. what students can discover

### Common Misconceptions
- Specific errors students make, with brief explanations of why they occur
- Valuable for teachers, tutors, and content creators

### Questions
- 2-5 questions per topic, testing understanding (not memorization)
- At least one question should target a common misconception
- Three types: `multiple-choice` (4 options, 0-indexed answer), `true-false`, `short-answer`
- Every question needs an `explanation` that helps reviewers verify correctness
- Place in a `## Questions` section with a fenced YAML code block

Example:

```markdown
## Questions

\```yaml
- question: "Why can't you add 1/3 + 1/4 directly?"
  type: multiple-choice
  options:
    - "The numerators are different"
    - "The denominators define different-sized pieces, so they can't be combined"
    - "Fractions can only be added if they share a numerator"
    - "You need to multiply fractions before adding them"
  answer: 1
  explanation: "Denominators define the size of each piece. Thirds and fourths are different-sized pieces — you must convert to a common denominator (same-sized pieces) before adding."

- question: "1/3 + 1/4 = 2/7."
  type: true-false
  answer: false
  explanation: "Adding both numerators and denominators is the most common error. The correct answer is 4/12 + 3/12 = 7/12."
\```
```

*(Remove the backslashes before the triple backticks — they are shown here to prevent formatting issues.)*

### Explainers
- 3-5 paragraphs that actually teach the concept (unlike Core Idea, which describes it)
- Written for someone who has completed the prerequisites
- Should build intuition through reasoning, analogies, and worked examples
- Freeform Markdown — can include examples, analogies, and connections to prerequisites
- Place in a `## Explainer` section after all other sections

**Quality bar:** A good Explainer is what a skilled tutor would say. It does not repeat the Core Idea — it unpacks it, walks through the reasoning, and helps the reader build a mental model.

### Style
- Write clearly and concisely
- Use standard mathematical terminology
- No jargon without definition
- No promotional language or references to specific paid products

## Starting a New Domain

If you want to map a domain beyond mathematics:

1. Open an issue to discuss the domain scope and course structure
2. Create a `_domain.yml` file defining the domain and its courses
3. Start with 20-30 seed topics covering the most foundational concepts
4. The same schema applies -- only the domain and course values change

## Review Process

- All PRs are reviewed for schema compliance (automated via CI) and content accuracy (human review)
- Stubs (frontmatter only, minimal content) have a lower review bar -- the structure matters most
- Full topics are reviewed for prerequisite accuracy, content clarity, and pedagogical soundness
- Disagreements about prerequisites are resolved by discussion, not authority. If reasonable people disagree, mark the edge as `soft`.

## Code of Conduct

Be constructive. The goal is mapping knowledge, not proving expertise. A wrong prerequisite link submitted in good faith is easily fixed; a missing topic that nobody contributed stays missing forever.

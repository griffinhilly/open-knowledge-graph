# Topic Schema

Every topic in the Open Knowledge Graph is a Markdown file with YAML frontmatter. This document defines the required and optional fields.

## Frontmatter Fields

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier. Must match the filename (without `.md`). Lowercase, hyphenated. |
| `title` | string | Human-readable topic name. |
| `domain` | string | Top-level domain (e.g., `mathematics`, `physics`). Must match a domain in `domains/`. |
| `course` | string | Course-level grouping (e.g., `5th-grade`, `algebra-1`). Must match a subdirectory in the domain. |
| `prerequisites` | list | Topics that must be understood before this one. Each entry has `id` (string) and `type` (`hard` or `soft`). Empty list `[]` for root topics. |

### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `builds-toward` | list of strings | `[]` | Topic IDs that depend on this topic. Informational — the canonical direction is prerequisites pointing backward. Validation checks consistency. |
| `stage` | string | — | Developmental stage: `proto-formal`, `pre-formal`, `concrete-operations`, `abstract-reasoning`, `formal-systems`, `advanced`, `expert`. See `meta/developmental-stages.md`. |
| `kind` | string | `topic` | Node kind. Omit for normal taught topics (`topic`). `capacity` marks a developmental precursor node in the origin layer (`developmental-origins` meta-domain) — a private structural substrate excluded from pages, assessment, JSON-LD, sitemap, and headline counts. See `plans/origin-layer-spec.md`. |
| `tags` | list of strings | `[]` | Freeform tags for search/filtering (e.g., `[fractions, arithmetic]`). |
| `status` | string | `draft` | One of: `stub`, `draft`, `review`, `validated`, `reference`. (`reference` = a non-assessable `kind: capacity` node; the "all topics validated" invariant covers `kind: topic` only.) |
| `aliases` | list of strings | `[]` | Alternative names for this topic (e.g., `["LCD method", "common denominator addition"]`). |
| `external-refs` | list of objects | `[]` | Links to external resources. Each has `title` (string) and `url` (string). |

### Prerequisite Types

- **`hard`** — This topic *cannot* be meaningfully understood without the prerequisite. Skipping it will cause failure.
- **`soft`** — This topic is *enriched by* the prerequisite but can be attempted without it. Understanding will be partial but functional.

## Body Sections

The Markdown body after frontmatter should contain:

### Required

- **`## Core Idea`** — What this topic is and why it matters. 2-5 sentences. Should be understandable by someone who has the prerequisites but hasn't seen this topic yet.

### Optional

- **`## How It's Best Learned`** — Pedagogical notes: what representations work, what sequence of activities, what to emphasize. Valuable for curriculum designers and tutors.
- **`## Common Misconceptions`** — Known misunderstandings students encounter. Valuable for teachers and content creators.
- **`## Questions`** — Test questions for the topic, contained in a YAML code block. See format below.
- **`## Explainer`** — A mini-lesson (3-5 paragraphs) that teaches the concept to someone who has completed the prerequisites. Unlike Core Idea (which describes what the topic IS), the Explainer walks through reasoning, builds intuition, and includes examples. Think of it as what a good tutor would say. The Explainer is freeform Markdown and can include worked examples, analogies, diagrams described in text, and connections to prerequisite concepts.
- **`## Notes`** — Anything else: historical context, connections to other domains, open questions.

### Questions Format

The `## Questions` section contains a fenced YAML code block with 2-5 test questions. Three question types are supported:

```yaml
# Multiple-choice (4 options, 0-indexed answer)
- question: "Question text here?"
  type: multiple-choice
  options: ["Option A", "Option B", "Option C", "Option D"]
  answer: 1
  explanation: "Why Option B is the correct answer."

# True-false
- question: "Statement to evaluate."
  type: true-false
  answer: false
  explanation: "Why the statement is false."

# Short-answer
- question: "Open-ended question?"
  type: short-answer
  answer: "Expected answer text"
  explanation: "What makes this the right answer."
```

**Rules:**
- Each topic should have 2-5 questions when populated
- Questions should test understanding, not memorization
- At least one question should test a common misconception
- Explanations are required — they help reviewers verify accuracy
- For multiple-choice: 4 options, plausible distractors, one correct answer
- The Questions section is optional — topics work fine without it

## Naming Conventions

- **File names** = topic ID + `.md` (e.g., `adding-fractions-unlike-denominators.md`)
- **IDs** are globally unique across all domains. Prefix with domain if needed to disambiguate (e.g., `physics-vectors` vs `math-vectors`).
- Use lowercase and hyphens. No underscores, no spaces, no special characters.
- Be specific: `multiplying-two-digit-by-one-digit` not `multiplication-2`.
- Be consistent: use the most common textbook name for the topic.

## Example

```markdown
---
id: adding-fractions-unlike-denominators
title: Adding Fractions with Unlike Denominators
domain: mathematics
course: 5th-grade
prerequisites:
  - id: equivalent-fractions
    type: hard
  - id: adding-fractions-like-denominators
    type: hard
  - id: least-common-multiple
    type: soft
builds-toward:
  - subtracting-fractions-unlike-denominators
  - mixed-number-addition
tags: [fractions, arithmetic, number-sense]
stage: concrete-operations
status: draft
---

# Adding Fractions with Unlike Denominators

## Core Idea

To add fractions with different denominators, you must first rewrite them
as equivalent fractions with a common denominator, then add the numerators.
For example, 1/3 + 1/4 becomes 4/12 + 3/12 = 7/12. The key insight is that
you cannot add fractions directly unless they represent the same-sized pieces
-- the denominator defines the unit, and you can only combine like units.

## How It's Best Learned

Start with visual fraction models (fraction bars or area models) showing
why 1/3 + 1/4 can't be combined directly -- the pieces are different sizes.
Then show that rewriting both as twelfths makes the pieces the same size.
Connect to the concept of equivalent fractions before introducing the
algorithm. Use number lines as a second representation.

## Common Misconceptions

- Adding numerators AND denominators (1/3 + 1/4 = 2/7) -- the most common
  error. Address directly with visual models.
- Always using the product of denominators instead of the LCD -- works but
  produces unnecessarily large fractions. Teach LCD as an optimization, not
  a requirement.
```

## Validation Rules

The `tools/validate.py` script enforces:

1. Every `id` matches its filename
2. Every prerequisite `id` references an existing topic file
3. No cycles in the prerequisite graph
4. Required fields are present and correctly typed
5. `status` is one of the allowed values
6. `course` matches an existing subdirectory in the domain
7. `builds-toward` entries are consistent with other topics' prerequisites (warning, not error)
8. No duplicate IDs across the entire graph

## DAG as Pedagogical Simplification

The prerequisite graph is a directed acyclic graph (DAG). Real knowledge contains circular interdependencies (e.g., plate tectonics informs the rock cycle and vice versa); the DAG represents a pedagogically useful linearization, not a claim that knowledge is acyclic. Where topics mutually inform each other, the prerequisite direction reflects the most common introductory teaching sequence.

**What a prerequisite edge means.** An edge `A → B` means *B draws upon A* — you engage A on the way to B. It does **not** assert that A is encountered *earlier in time* than B. Chronology is a separate axis, carried by `stage`, not by edges: a prerequisite can be staged later than what it feeds (the ~8% "stage-inversion" edges are legitimate cases of this, not errors). This "draws-upon" reading is what lets the graph stay acyclic even where the underlying capacities are mutually reinforcing — the edge records the *dominant* direction of the dependency, and mutual reinforcement is never encoded as bidirectional edges. This matters most at the developmental origin layer (`kind: capacity`), where capacities bootstrap each other and strict chronological ordering breaks down; there, edges are read purely as "draws upon / sharpens."

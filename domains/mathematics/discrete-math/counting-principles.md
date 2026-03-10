---
id: counting-principles
title: 'Counting Principles: Addition and Multiplication Rules'
domain: mathematics
course: discrete-math
prerequisites:
- id: set-theory-basics
  type: hard
- id: combinations
  type: soft
builds-toward:
- pigeonhole-principle
- inclusion-exclusion-principle
- stars-and-bars
- derangements
tags:
- counting
- combinatorics
- addition-rule
- multiplication-rule
stage: formal-systems
status: draft
---

# Counting Principles: Addition and Multiplication Rules

## Core Idea
The addition rule states that if two tasks are mutually exclusive, they can be performed in m + n ways total. The multiplication rule states that if task A can be done in m ways and task B in n ways independently, both can be done in m × n ways. These two principles are the foundation of systematic counting in combinatorics. Together with permutations and combinations, they handle the vast majority of counting problems encountered in discrete mathematics.

## How It's Best Learned
Start with concrete examples: how many ways to travel from city A to C via B if there are 3 roads A→B and 4 roads B→C? Build intuition before formalizing. Have students categorize problems as 'OR situations' (addition) or 'AND sequences' (multiplication).

## Common Misconceptions
- Confusing when to add versus multiply — ask: are we choosing one task OR another? (add) versus completing task A AND then task B? (multiply).
- Forgetting that the multiplication rule requires independence between choices.
- Mixing up counting ordered sequences with unordered collections.

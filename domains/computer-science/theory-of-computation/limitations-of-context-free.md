---
id: limitations-of-context-free
title: Limitations of Context-Free Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: closure-properties-context-free
  type: hard
builds-toward:
- turing-machine-model
tags:
- context-free
- non-cfl
- hierarchy
stage: abstract-reasoning
status: draft
---

# Limitations of Context-Free Languages

## Core Idea
Context-free languages cannot recognize dependencies across three or more independently nested groups (e.g., {aⁿbⁿcⁿ}). The pumping lemma for CFLs establishes non-context-free languages. These limitations motivate even more powerful models like Turing machines.

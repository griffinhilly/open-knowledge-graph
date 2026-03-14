---
id: gradual-typing-systems
title: Gradual Typing and Mixed Static-Dynamic Types
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: type-inference-algorithms
  type: soft
tags:
- type-systems
- static
- dynamic
stage: advanced
status: draft
---

# Gradual Typing and Mixed Static-Dynamic Types

## Core Idea
Gradual typing blends static and dynamic typing, allowing programmers to omit type annotations where inference fails or dynamic behavior is needed. The compiler inserts runtime type checks where static types transition to 'any' or 'dynamic', enabling flexible development without abandoning static safety entirely.

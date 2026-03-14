---
id: interpreter-design-and-tradeoffs
title: Interpreter Design and Execution Models
domain: computer-science
course: compilers
prerequisites:
- id: tree-walking-interpreters
  type: hard
- id: compiler-phases-and-organization
  type: hard
tags:
- interpretation
- execution
- performance
stage: advanced
status: draft
---

# Interpreter Design and Execution Models

## Core Idea
Interpreters execute code directly without generating machine code, enabling portability and dynamic behavior but at the cost of speed. Design choices span tree-walking (simplest, slowest), bytecode (intermediate), and JIT (adaptive compilation), each balancing complexity, flexibility, and performance.

## How It's Best Learned
Implement a tree-walking interpreter for a simple language, add bytecode, then measure performance differences between them.

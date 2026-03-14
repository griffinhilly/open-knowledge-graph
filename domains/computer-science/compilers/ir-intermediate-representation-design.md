---
id: ir-intermediate-representation-design
title: Intermediate Representation Design and Tradeoffs
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: compiler-phases-and-organization
  type: hard
tags:
- IR
- design
- architecture
stage: advanced
status: draft
---

# Intermediate Representation Design and Tradeoffs

## Core Idea
Choosing an IR shape profoundly affects compiler modularity and performance: high-level IRs (close to source syntax) simplify semantic analysis but complicate code generation; low-level IRs (close to machine code) simplify backend work but require careful lowering. The choice shapes the entire compiler architecture.

---
id: assembly-code-generation
title: Assembly Code Generation from IR
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: assembly-language-basics
  type: hard
- id: instruction-selection-techniques
  type: hard
builds-toward:
- target-specific-code-generation
tags:
- code-generation
- assembly
- lowering
stage: advanced
status: draft
---

# Assembly Code Generation from IR

## Core Idea
Assembly code generation translates target-independent intermediate code into assembly language for the host CPU. It selects registers, chooses addressing modes, and generates instruction sequences respecting CPU constraints while preserving IR semantics—the bridge between high-level optimization and machine execution.

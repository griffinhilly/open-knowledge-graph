---
id: compiler-bootstrapping
title: Compiler Bootstrapping and Self-Hosting
domain: computer-science
course: compilers
prerequisites:
- id: compiler-phases-and-organization
  type: hard
- id: assembly-language-basics
  type: hard
tags:
- bootstrapping
- compilation
- self-hosting
stage: advanced
status: draft
---

# Compiler Bootstrapping and Self-Hosting

## Core Idea
A bootstrap compiler is a compiler written in its own language. Building one requires an initial compiler in another language to compile the bootstrapping version; the bootstrapped compiler then compiles itself, enabling improvements with each iteration and providing a reference implementation.

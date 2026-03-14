---
id: intermediate-code-representation
title: Intermediate Code Representation
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: abstract-syntax-trees
  type: hard
builds-toward:
- static-single-assignment-form
- code-optimization
tags:
- intermediate-representation
- ir
- compilation-phases
stage: advanced
status: draft
---

# Intermediate Code Representation

## Core Idea
Intermediate representation (IR) is an abstraction between source and target languages. Common forms include three-address code (TAC), register-transfer language (RTL), and bytecode. IR simplifies optimization and retargeting: optimize once on IR, then generate code for multiple targets. IR abstracts away source-language details and target-machine specifics, enabling machine-independent transformations.

---
id: turing-machine-completeness
title: Turing Machine Completeness
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: church-turing-thesis
  type: hard
builds-toward:
- oracle-turing-machines
tags:
- computability
- universality
- computation
stage: advanced
status: draft
---

# Turing Machine Completeness

## Core Idea
Turing completeness means a computational model can simulate any Turing machine and thus compute any effectively computable function. The Church-Turing thesis asserts all intuitive notions of 'computable' coincide with Turing computability. Remarkably, many superficially weak systems—cellular automata, lambda calculus, Post systems, even some game of life configurations—are Turing-complete, showing completeness is an intrinsic property of sufficient complexity rather than requiring explicit components.

---
id: universal-turing-machine
title: Universal Turing Machines and Computational Universality
domain: computer-science
course: theory-of-computation
prerequisites:
- id: multi-tape-turing-machines
  type: hard
- id: church-turing-thesis
  type: soft
builds-toward:
- halting-problem
- diagonalization-and-uncomputability
tags:
- universal-tm
- simulation
- encoding
- universality
- self-reference
stage: advanced
status: draft
---

# Universal Turing Machines and Computational Universality

## Core Idea
A universal Turing machine (UTM) simulates any other TM given its description as input. The existence of a UTM embodies computation as computable: all algorithms can run on a single programmable machine. This self-referential property—a TM processing descriptions of TMs—enables encoding TMs as strings, which is crucial for undecidability proofs like the halting problem.

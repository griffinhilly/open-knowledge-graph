---
id: complexity-class-np-definition
title: 'Complexity Class NP: Nondeterministic Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-p-definition
  type: hard
- id: multi-tape-turing-machines
  type: soft
builds-toward:
- np-completeness-and-hardness
tags:
- np-class
- nondeterminism
- verification
- certificate
- hard
stage: advanced
status: draft
---

# Complexity Class NP: Nondeterministic Polynomial Time

## Core Idea
NP contains languages decided by nondeterministic TMs in polynomial time. Equivalently, NP is languages where yes-instances admit polynomial-size certificates verifiable in polynomial time. Many practical hard problems (SAT, clique, TSP decision version) are NP. The P vs NP question asks: is guessing-and-checking as fast as deterministic solving? Most believe P ≠ NP, but it remains open.

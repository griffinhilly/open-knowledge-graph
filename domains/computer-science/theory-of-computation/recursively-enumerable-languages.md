---
id: recursively-enumerable-languages
title: Recursively Enumerable Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: decidability
  type: hard
builds-toward:
- recognizability-vs-decidability
- halting-problem
tags:
- computability
- formal-languages
- turing-completeness
stage: advanced
status: draft
---

# Recursively Enumerable Languages

## Core Idea
A language is recursively enumerable (RE) if a Turing machine exists that halts-and-accepts every string in the language; for strings outside the language, the machine may never halt. RE languages equal Type 0 languages in the Chomsky hierarchy. They represent the boundary of mechanical computation: problems whose solutions can be systematically generated (enumerated) but not necessarily verified in finite time characterize this class.

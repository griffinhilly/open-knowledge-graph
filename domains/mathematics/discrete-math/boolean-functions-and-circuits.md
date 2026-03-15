---
id: boolean-functions-and-circuits
title: Boolean Functions, Logic Gates, and Digital Circuits
domain: mathematics
course: discrete-math
prerequisites:
- id: boolean-algebra
  type: hard
builds-toward:
- algorithm-complexity-discrete
tags:
- Boolean-functions
- logic-gates
- circuits
- DNF-CNF
stage: formal-systems
status: draft
---

# Boolean Functions, Logic Gates, and Digital Circuits

## Core Idea
A Boolean function f: {0,1}ⁿ → {0,1} is computed by a logic circuit using AND, OR, NOT gates. Every Boolean function can be expressed in disjunctive normal form (DNF) or conjunctive normal form (CNF). Circuit complexity measures the minimum gates or depth needed.

## How It's Best Learned
Build truth tables for Boolean functions. Express functions in DNF (OR of ANDs) and CNF (AND of ORs). Apply Boolean algebra identities to simplify circuits. Design circuits for arithmetic (adders, multipliers).

## Common Misconceptions
DNF and CNF are normal forms, not canonical until further specified. A Boolean function can have multiple minimal representations. Circuit complexity depends on depth and gate count—it's not unique.

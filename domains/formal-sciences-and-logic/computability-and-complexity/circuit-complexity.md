---
id: circuit-complexity
title: Circuit Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: space-complexity-classes-formal
  type: soft
- id: logic-gates-and-circuits
  type: soft
- id: boolean-functions-and-circuits
  type: soft
builds-toward:
- descriptive-complexity
tags:
- complexity
- circuits
- non-uniform-computation
- P/poly
stage: formal-systems
status: draft
---

# Circuit Complexity

## Core Idea
Circuit complexity studies computation through families of Boolean circuits — directed acyclic graphs of AND, OR, and NOT gates — one circuit for each input length. Unlike Turing machines, circuits are a non-uniform model: a different circuit can be hardwired for each input size. The class P/poly contains problems solvable by polynomial-size circuit families, and P is in P/poly (any poly-time TM can be "unrolled" into circuits). The NC and AC hierarchies classify problems by circuit depth (parallel time) and fan-in: NC^k uses poly-size, O(log^k n)-depth circuits with bounded fan-in. Proving super-polynomial circuit lower bounds for explicit problems remains one of the central challenges in complexity theory.

## How It's Best Learned
Build small circuits by hand for functions like parity, majority, and addition. Then formalize the notion of circuit families and understand why non-uniformity matters (a circuit family can "know" an uncomputable function via hardwired advice). Study the Karp-Lipton theorem — if NP is in P/poly then the polynomial hierarchy collapses — to see why circuit lower bounds connect to P vs NP.

## Common Misconceptions
- P/poly is NOT a subset of P — it contains undecidable problems because the circuit for each input length can encode uncomputable information as advice.
- Small circuits do not mean fast algorithms — circuit size measures total work, while circuit depth measures parallel time.

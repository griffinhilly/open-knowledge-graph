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
stage: advanced
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

## Explainer

You already know from studying logic gates and Boolean functions that any Boolean function can be computed by a network of AND, OR, and NOT gates. **Circuit complexity** takes this observation and turns it into a model of computation: instead of asking "what can a Turing machine solve?", we ask "how many gates, and how deep a circuit, does this function require?"

The key conceptual shift is **non-uniformity**. A Turing machine uses a single program for all input lengths. A circuit, by contrast, can use a *different* circuit for each input size — the circuit for 10-bit inputs need not resemble the circuit for 1000-bit inputs. This extra flexibility is powerful: a circuit family can "hardwire" arbitrary finite information about each length into its structure, which means **P/poly** contains some problems that are undecidable by any Turing machine. The class P/poly contains exactly those problems solvable by polynomial-size circuit families. Since any polynomial-time Turing machine can be "unrolled" into circuits (each time step becomes a layer), P ⊆ P/poly — but the containment is strict.

Circuit complexity also gives a fine-grained way to measure **parallelism**. A circuit's *size* measures total work (number of gates), but its *depth* measures the critical path — the parallel time if all gates run simultaneously. The **NC hierarchy** classifies problems by depth: NC^k uses polynomial-size circuits with O(log^k n) depth and bounded fan-in. NC^1 captures what can be parallelized extremely well (e.g., evaluating Boolean formulas), while NC^1 ⊆ NC^2 ⊆ ... ⊆ P. Problems in P that are conjectured to be outside NC are called **P-complete** under NC reductions — solving them in parallel seems inherently sequential.

The central open question in circuit complexity is whether any explicit Boolean function requires super-polynomial circuits. If you could show some specific function in NP requires circuits of size 2^Ω(n), you would prove P ≠ NP. The **Karp-Lipton theorem** ties these together: if NP ⊆ P/poly, then the polynomial hierarchy collapses to its second level — a widely disbelieved consequence, giving indirect evidence that NP does not have polynomial-size circuits. Despite decades of effort, the best known lower bounds for general (unrestricted) circuits fall far short of what would resolve P vs NP, making circuit lower bounds one of the deepest open frontiers in theoretical computer science.

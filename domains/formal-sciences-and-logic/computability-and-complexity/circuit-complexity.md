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

## Questions

```yaml
- question: "A student argues: 'Any polynomial-time algorithm can be simulated by polynomial-size circuits, so P and P/poly must be the same complexity class.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct; P and P/poly are equivalent classes"
    - "P ⊆ P/poly holds, but the reverse fails: circuit families are non-uniform and can hardwire information for each input length, allowing them to solve some undecidable problems that no Turing machine can"
    - "Circuits cannot simulate Turing machines in general; the simulation only works for space-bounded computation"
    - "The simulation requires exponential-size circuits for polynomial-time algorithms"
  answer: 1
  explanation: "The student correctly identifies that P ⊆ P/poly — any poly-time TM can be unrolled into poly-size circuits. But the containment is strict. A circuit family is non-uniform: it can use a completely different circuit for each input length, hardwiring arbitrary finite information specific to that size. A Turing machine must use one finite program for all inputs. This non-uniformity lets circuit families 'solve' problems that no TM can, because the answer for inputs of length n can be baked into the circuit for length n without being computed."

- question: "What does circuit depth measure, and how does it differ from circuit size?"
  type: multiple-choice
  options:
    - "Circuit depth measures the total number of gates; circuit size measures the number of input wires"
    - "Circuit depth measures the length of the longest input-to-output path (parallel time); circuit size measures the total number of gates (total work)"
    - "Circuit depth measures the number of NOT gates; circuit size counts only AND and OR gates"
    - "Circuit depth and size always differ by at most a polynomial factor, making them essentially equivalent"
  answer: 1
  explanation: "Size and depth measure different computational resources. Size = total gates = total work, analogous to sequential time. Depth = longest path from any input to output = the critical path, representing parallel time if all gates run simultaneously. A sequential chain of n gates has size n and depth n. A balanced binary tree of n gates has size n and depth log n. Problems in NC have both polynomial size and polylogarithmic depth (highly parallelizable); P-complete problems are in P but believed to require polynomial depth, making them inherently sequential."

- question: "P/poly is a subset of P, because any problem solvable by polynomial-size circuits can also be solved by a polynomial-time Turing machine."
  type: true-false
  answer: false
  explanation: "This reverses the correct relationship. P ⊆ P/poly, not the other way around. P/poly is strictly larger: it contains some undecidable problems, because circuit families can hardwire answers specific to each input length without computing them from a finite program. A Turing machine cannot exploit non-uniformity in this way. The undecidable language that contains exactly the binary encodings of circuits that accept their own length is a classic example of something in P/poly but outside any decidable class."

- question: "Proving that some explicit Boolean function in NP requires super-polynomial circuit size would immediately prove P ≠ NP."
  type: true-false
  answer: false
  explanation: "More precisely: showing NP ⊄ P/poly would imply P ≠ NP (since P ⊆ P/poly, if P = NP then NP ⊆ P/poly). But proving a super-polynomial lower bound for an arbitrary Boolean function doesn't directly address P vs NP — most functions require large circuits by a counting argument, but those functions aren't necessarily in NP. The challenge is finding an *explicit* function in NP that requires large circuits. The Karp-Lipton theorem gives the connection: if NP ⊆ P/poly, the polynomial hierarchy collapses to its second level, a widely disbelieved consequence providing indirect evidence against it."

- question: "Explain why non-uniformity is both the power and the limitation of circuit complexity as a model of computation."
  type: short-answer
  answer: "Non-uniformity is the power because each input length can use a completely different circuit, hardwiring arbitrary finite information about inputs of that size. This lets circuit families solve problems that no Turing machine can — P/poly contains undecidable problems. It is also the limitation: a real computer program is uniform (one algorithm handles all input sizes), so circuit lower bounds in the non-uniform model don't directly translate to lower bounds for actual algorithms. If you want circuit lower bounds to imply P ≠ NP, you need to show that relevant NP functions lack efficient circuits even with full non-uniformity — which despite decades of effort has proved extremely difficult."
  explanation: "The tension is that non-uniformity seemingly restricts the model (circuits can't loop or recurse), which should make lower bounds easier to prove. But circuits are still enormously flexible — a different circuit per length is a powerful resource — and the best known lower bounds for general circuits fall far short of what would resolve P vs NP."
```

## Explainer

You already know from studying logic gates and Boolean functions that any Boolean function can be computed by a network of AND, OR, and NOT gates. **Circuit complexity** takes this observation and turns it into a model of computation: instead of asking "what can a Turing machine solve?", we ask "how many gates, and how deep a circuit, does this function require?"

The key conceptual shift is **non-uniformity**. A Turing machine uses a single program for all input lengths. A circuit, by contrast, can use a *different* circuit for each input size — the circuit for 10-bit inputs need not resemble the circuit for 1000-bit inputs. This extra flexibility is powerful: a circuit family can "hardwire" arbitrary finite information about each length into its structure, which means **P/poly** contains some problems that are undecidable by any Turing machine. The class P/poly contains exactly those problems solvable by polynomial-size circuit families. Since any polynomial-time Turing machine can be "unrolled" into circuits (each time step becomes a layer), P ⊆ P/poly — but the containment is strict.

Circuit complexity also gives a fine-grained way to measure **parallelism**. A circuit's *size* measures total work (number of gates), but its *depth* measures the critical path — the parallel time if all gates run simultaneously. The **NC hierarchy** classifies problems by depth: NC^k uses polynomial-size circuits with O(log^k n) depth and bounded fan-in. NC^1 captures what can be parallelized extremely well (e.g., evaluating Boolean formulas), while NC^1 ⊆ NC^2 ⊆ ... ⊆ P. Problems in P that are conjectured to be outside NC are called **P-complete** under NC reductions — solving them in parallel seems inherently sequential.

The central open question in circuit complexity is whether any explicit Boolean function requires super-polynomial circuits. If you could show some specific function in NP requires circuits of size 2^Ω(n), you would prove P ≠ NP. The **Karp-Lipton theorem** ties these together: if NP ⊆ P/poly, then the polynomial hierarchy collapses to its second level — a widely disbelieved consequence, giving indirect evidence that NP does not have polynomial-size circuits. Despite decades of effort, the best known lower bounds for general (unrestricted) circuits fall far short of what would resolve P vs NP, making circuit lower bounds one of the deepest open frontiers in theoretical computer science.

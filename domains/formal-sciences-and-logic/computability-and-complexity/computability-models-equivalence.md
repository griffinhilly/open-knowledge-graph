---
id: computability-models-equivalence
title: Equivalence of Computational Models
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: church-turing-thesis-formal
  type: hard
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- turing-computable-vs-church-computable
- general-recursive-functions
tags:
- computability
- models-of-computation
- church-turing
stage: formal-systems
status: validated
---

# Equivalence of Computational Models

## Core Idea
Turing machines, lambda calculus, and mu-recursive functions all define the same class of computable functions. This foundational result—the Church-Turing thesis—establishes that no reasonable model of computation can compute anything beyond what Turing machines compute, making computability a robust, model-independent notion.

## How It's Best Learned
Compare the definitions of computation across at least two models (e.g., Turing machines and lambda calculus), then study a concrete encoding of one model into another.

## Common Misconceptions
- Thinking Church-Turing thesis is a proven theorem (it is a thesis about the limits of formal computation).
- Confusing the thesis with the claim that all algorithms can be fast (computability is about existence, not efficiency).

## Questions

```yaml
- question: "A researcher proposes a new model called 'quantum-symbolic automata' (QSA) and proves: (1) any Turing machine computation can be simulated step-by-step by a QSA, and (2) any QSA computation can be simulated by a Turing machine. What follows from these two results?"
  type: multiple-choice
  options:
    - "QSA is a strictly stronger model than Turing machines because it uses quantum-inspired operations"
    - "QSA computes exactly the class of Turing-computable functions — the two models are computationally equivalent"
    - "This proves the Church-Turing thesis for quantum models, establishing QSA as the correct model of physical computation"
    - "QSA can solve the halting problem because quantum mechanics transcends classical computability limits"
  answer: 1
  explanation: "Computational equivalence requires exactly this bidirectional simulation: TM can simulate QSA and QSA can simulate TM. Both directions together mean both models compute the same class of functions. The quantum-inspired operations do not make QSA stronger (option 0) — no matter how exotic the operations, if TMs can simulate them, they add no new computational power. The Church-Turing thesis concerns the informal notion of 'effective procedure,' not formal model comparisons (option 2). The halting problem is undecidable for all models equivalent to TMs, including QSA (option 3)."

- question: "A function runs in O(n log n) time on a RAM (random-access memory) machine. Which statement best describes its status on a Turing machine?"
  type: multiple-choice
  options:
    - "The function is not Turing-computable because RAM machines are a fundamentally different computational model"
    - "The function is Turing-computable, but simulating random access on a tape may require significantly more time steps"
    - "The function runs in O(n log n) on a Turing machine too, because computationally equivalent models have identical efficiency"
    - "The Church-Turing thesis guarantees that equivalent models compute all functions in the same number of steps"
  answer: 1
  explanation: "Computability equivalence guarantees the existence of a Turing machine that computes the function — not that it runs in the same time. Simulating random access on a sequential tape incurs overhead: finding the right cell may require scanning the tape, turning O(1) RAM operations into O(n) tape operations. Computability and complexity are separate questions. Options 2 and 3 conflate them — the equivalence theorem says 'it can be computed,' not 'it can be computed efficiently.' Complexity theory (P, NP, etc.) studies the efficiency question separately."

- question: "The Church-Turing thesis has been proven as a mathematical theorem from the formal definitions of Turing machines, lambda calculus, and mu-recursive functions."
  type: true-false
  answer: false
  explanation: "The Church-Turing thesis is a thesis, not a theorem. What has been proven mathematically is that the formal models — Turing machines, lambda calculus, mu-recursive functions — are equivalent to each other (they compute the same class of functions). The thesis then asserts that these formal models correctly capture the informal concept of 'effective procedure' — any finite, deterministic, mechanical process. That claim involves an informal notion that cannot be formalized without already assuming something like the thesis. It is a philosophical assertion supported by overwhelming empirical evidence but not a mathematical proof."

- question: "The convergence of Turing machines, lambda calculus, and mu-recursive functions — three independently developed 1930s formalisms — on the same class of computable functions is the empirical core of the Church-Turing thesis."
  type: true-false
  answer: true
  explanation: "Turing proposed his machines in 1936; Church developed lambda calculus in 1932–1936; Gödel and Kleene developed recursive functions slightly later. They were proposed independently, look nothing alike, yet compute exactly the same class of functions — a remarkable convergence that was recognized almost immediately after Turing's 1936 paper. This historical convergence is the strongest evidence for the Church-Turing thesis: three very different approaches to formalizing computation all agree on what is computable, suggesting they have identified something real about the limits of effective computation."

- question: "Why is the Church-Turing thesis described as a 'thesis' rather than a 'theorem,' and what constitutes the evidence in its favor?"
  type: short-answer
  answer: "A theorem follows deductively from formal definitions. The Church-Turing thesis involves the informal concept of 'effective procedure' — a finite, deterministic, mechanical process that a person could in principle carry out. This concept cannot be formally defined without already assuming something like the thesis itself. What can be proven is that all the formal models ever written down are equivalent to each other — that is the theorem. The thesis then asserts that these formal models have correctly captured the informal intuition. The evidence is overwhelming: every model of computation ever proposed — register machines, cellular automata, Wang tiles, DNA computing, quantum circuits — has been shown to be computationally equivalent to Turing machines. No counterexample has ever been found."
  explanation: "The distinction between theorem and thesis is philosophically important: a theorem is certain within its axiom system; a thesis is a claim about the relationship between a formal system and an informal concept. The Church-Turing thesis is one of the most compelling theses in all of science — the empirical record is perfect — but it cannot be elevated to theorem status without resolving the philosophical question of what 'effective computation' means independent of formal definition."
```

## Explainer

You already know what a Turing machine is: a finite-state controller reading and writing symbols on an infinite tape, moving one cell at a time. You also know lambda calculus: a system of anonymous functions that compute by substitution and reduction. These look nothing alike — one is a physical machine metaphor, the other is pure symbol manipulation. The central result of this topic is that they are nonetheless **computationally equivalent**: every function computable by one is computable by the other.

The equivalence proof works by translation. To show Turing machines and lambda calculus are equivalent, you need two directions: (1) every Turing machine computation can be simulated by a lambda expression, and (2) every lambda calculus computation can be simulated by a Turing machine. For direction (1), you encode the tape contents, head position, and machine state as a lambda term, then show that each machine step corresponds to a reduction step. For direction (2), you implement beta-reduction as a Turing machine algorithm. Neither direction is trivial, but both can be made explicit — which is what makes equivalence a theorem rather than a guess.

This same argument extends to **mu-recursive functions** (the class of functions built from zero, successor, projection, composition, primitive recursion, and minimization). They too compute exactly the same class. All three formalisms were proposed independently in the 1930s — Turing's machines in 1936, Church's lambda calculus in 1932–1936, Gödel and Kleene's recursive functions slightly later — and their equivalence was recognized almost immediately. This convergence is the empirical core of the **Church-Turing thesis**: any function that can be computed by an "effective procedure" — any finite, deterministic, mechanical process — can be computed by a Turing machine.

The Church-Turing thesis is not a theorem and cannot be proven from the formal definitions alone, because "effective procedure" is an informal intuitive concept, not a mathematical object. What the theorem establishes is that all the *formal* models we can write down agree. The thesis then asserts that our formal models have correctly captured the informal concept. This is a philosophical claim supported by overwhelming evidence — every new model of computation ever proposed has turned out to be equivalent — but it remains a thesis, not a proof. Critically, the equivalence result says nothing about *efficiency*: a function computable in O(n log n) on a RAM machine might require exponential time on a Turing machine due to the cost of simulating random access. Computability and complexity are separate questions.

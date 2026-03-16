---
id: church-turing-thesis
title: Church-Turing Thesis and Computability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: universal-turing-machine
  type: hard
builds-toward:
- decidable-languages
- undecidable-problems
tags:
- church-turing-thesis
- computability
- foundations
stage: abstract-reasoning
status: draft
---

# Church-Turing Thesis and Computability

## Core Idea
The Church-Turing thesis states that the informal notion of 'computable by an algorithm' is equivalent to 'recognizable by a Turing machine'. Though unprovable, it is supported by the equivalence of multiple independent models (λ-calculus, recursive functions, Turing machines) and is widely accepted as true.

## Explainer

You have studied the universal Turing machine — a single machine that can simulate any other Turing machine given its description as input. This establishes Turing machines as remarkably powerful computational devices. But a fundamental question remains: are there algorithms that Turing machines *cannot* execute? Or conversely, does every conceivable algorithm correspond to some Turing machine? The **Church-Turing thesis** addresses this by asserting that the informal, intuitive notion of "what an algorithm can compute" is exactly captured by the formal notion of "what a Turing machine can compute."

The thesis is named for Alonzo Church and Alan Turing, who independently arrived at equivalent answers in the 1930s using completely different formalisms. Church defined computability through the **lambda calculus**, a system based on function abstraction and application. Turing defined it through his tape-based machines. Emil Post proposed yet another model (Post production systems), and Kurt Gödel worked with **recursive functions**. The striking result was that all four formalisms — developed independently, with very different mathematical machinery — turned out to define exactly the same class of computable functions. Every function computable by lambda calculus is computable by a Turing machine, and vice versa. This convergence from independent directions is the strongest evidence for the thesis.

Crucially, the Church-Turing thesis is not a theorem — it cannot be proved, because one side of the equivalence ("what an algorithm can compute") is an informal concept, not a mathematical object. You cannot formally prove that an informal notion matches a formal one. It is more like a natural law or a definitional axiom: we *define* "computable" to mean "Turing-computable" because every plausible alternative formalization has turned out to be equivalent. In the nearly ninety years since its formulation, no one has proposed a physically realizable model of computation that computes something a Turing machine cannot.

The practical consequence is profound. When you want to argue that a problem is unsolvable by any algorithm, it suffices to show that no Turing machine solves it. The Church-Turing thesis assures you that this impossibility extends to any programming language, any computer architecture, any computational model humans have conceived. This is what gives results like the undecidability of the halting problem their force — they are not merely statements about a particular machine model, but about the fundamental limits of computation itself.

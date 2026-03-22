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
stage: advanced
status: draft
---

# Church-Turing Thesis and Computability

## Core Idea
The Church-Turing thesis states that the informal notion of 'computable by an algorithm' is equivalent to 'recognizable by a Turing machine'. Though unprovable, it is supported by the equivalence of multiple independent models (λ-calculus, recursive functions, Turing machines) and is widely accepted as true.

## Questions

```yaml
- question: "A computer scientist claims to have formally proved the Church-Turing thesis by demonstrating that lambda calculus and Turing machines compute the same class of functions. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "The claim is correct — showing two formalisms are equivalent constitutes a proof of the thesis"
    - "The proof only covers lambda calculus; it would need to address all computational models"
    - "The thesis involves an informal notion ('computable by an algorithm') that cannot be a target of formal proof"
    - "The equivalence of lambda calculus and Turing machines has not actually been demonstrated"
  answer: 2
  explanation: "The Church-Turing thesis cannot be formally proved because one side of the equivalence — 'computable by an algorithm' — is an informal, intuitive concept, not a mathematical object. You can formally prove that two specific formalisms (lambda calculus and Turing machines) compute the same functions, but that does not prove the thesis. The thesis claims this formal class captures the informal notion of 'any algorithm' — a claim that cannot be made rigorous enough for formal proof."

- question: "The convergence of lambda calculus, Turing machines, recursive functions, and Post production systems on the same class of computable functions is significant because:"
  type: multiple-choice
  options:
    - "It proves that no new computational models are possible"
    - "It shows that any one of these models is sufficient to define computability"
    - "Multiple independent formalisms arriving at identical results provides strong empirical evidence for the thesis without constituting a proof"
    - "It confirms that computation is ultimately equivalent to mechanical symbol manipulation"
  answer: 2
  explanation: "The convergence is the strongest available evidence for the thesis precisely because the formalisms were developed independently using very different mathematical machinery. When diverse approaches consistently yield the same boundary, this is compelling — analogous to how multiple independent experiments that agree lend confidence to a scientific hypothesis. But it remains evidence, not proof, because the informal notion of 'algorithm' cannot be formally captured to complete the equivalence."

- question: "The Church-Turing thesis has been formally proved using mathematical logic."
  type: true-false
  answer: false
  explanation: "The Church-Turing thesis cannot be formally proved. A formal proof requires both sides of the equivalence to be mathematically defined objects, but 'computable by an algorithm' is an informal, pre-formal concept. This is not a gap in human mathematical ability — it is a fundamental obstacle. The thesis is accepted on the basis of strong empirical evidence (convergence of independent formalisms) and the absence of any counterexample, not on the basis of proof."

- question: "Proving that the halting problem cannot be decided by any Turing machine implies it cannot be solved by any algorithm on any physical computer."
  type: true-false
  answer: true
  explanation: "This is the practical force of the Church-Turing thesis. Because the thesis asserts that Turing machine computability captures the full scope of algorithmic computation, a Turing machine impossibility result extends to every programming language, every computer architecture, and every physically realizable model of computation. The undecidability of the halting problem is therefore a claim about the limits of computation itself, not merely about a specific machine model."

- question: "Why can the Church-Turing thesis not be formally proved, even in principle, despite nearly 90 years of effort?"
  type: short-answer
  answer: "Because one side of the equivalence — the informal notion of 'what an algorithm can compute' — is not a mathematical object and therefore cannot participate in a formal proof. A proof requires both sides to be rigorously defined, but 'algorithm' in the intuitive sense resists full formalization."
  explanation: "This is the deepest point about the thesis. It is not a theorem waiting to be proved; it is a definitional commitment — we adopt Turing computability as the formal definition of 'computable' because every alternative formalization has turned out to be equivalent. The thesis cannot be refuted by counterexample either, unless someone produces an intuitively algorithmic process that no Turing machine can compute. No such example has appeared in nearly a century of searching."
```

## Explainer

You have studied the universal Turing machine — a single machine that can simulate any other Turing machine given its description as input. This establishes Turing machines as remarkably powerful computational devices. But a fundamental question remains: are there algorithms that Turing machines *cannot* execute? Or conversely, does every conceivable algorithm correspond to some Turing machine? The **Church-Turing thesis** addresses this by asserting that the informal, intuitive notion of "what an algorithm can compute" is exactly captured by the formal notion of "what a Turing machine can compute."

The thesis is named for Alonzo Church and Alan Turing, who independently arrived at equivalent answers in the 1930s using completely different formalisms. Church defined computability through the **lambda calculus**, a system based on function abstraction and application. Turing defined it through his tape-based machines. Emil Post proposed yet another model (Post production systems), and Kurt Gödel worked with **recursive functions**. The striking result was that all four formalisms — developed independently, with very different mathematical machinery — turned out to define exactly the same class of computable functions. Every function computable by lambda calculus is computable by a Turing machine, and vice versa. This convergence from independent directions is the strongest evidence for the thesis.

Crucially, the Church-Turing thesis is not a theorem — it cannot be proved, because one side of the equivalence ("what an algorithm can compute") is an informal concept, not a mathematical object. You cannot formally prove that an informal notion matches a formal one. It is more like a natural law or a definitional axiom: we *define* "computable" to mean "Turing-computable" because every plausible alternative formalization has turned out to be equivalent. In the nearly ninety years since its formulation, no one has proposed a physically realizable model of computation that computes something a Turing machine cannot.

The practical consequence is profound. When you want to argue that a problem is unsolvable by any algorithm, it suffices to show that no Turing machine solves it. The Church-Turing thesis assures you that this impossibility extends to any programming language, any computer architecture, any computational model humans have conceived. This is what gives results like the undecidability of the halting problem their force — they are not merely statements about a particular machine model, but about the fundamental limits of computation itself.

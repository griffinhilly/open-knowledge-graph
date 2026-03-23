---
id: reducibility-many-one-formal
title: Many-One Reducibility in Computability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: computability-reductions
  type: hard
builds-toward:
- undecidability-proof-by-reduction
- turing-degrees
tags:
- reductions
- decidability
- undecidability
stage: formal-systems
status: draft
---

# Many-One Reducibility in Computability

## Core Idea
A language A is many-one reducible to B (A ≤_m B) if there is a computable function f such that w ∈ A iff f(w) ∈ B. This formal notion of reduction allows us to transfer decidability properties: if A ≤_m B and B is decidable, then A is decidable. Many-one reducibility is the foundational tool for proving undecidability via reduction.

## Questions

```yaml
- question: "You prove that A_TM (the TM acceptance problem) many-one reduces to language L, i.e., A_TM ≤_m L. Given that A_TM is undecidable, what can you conclude about L?"
  type: multiple-choice
  options:
    - "L is decidable, because the reduction provides an efficient translation between A_TM and L instances"
    - "L is undecidable, because a decider for L would give us a decider for A_TM via the reduction"
    - "Nothing can be concluded about L; the reduction only tells us about A_TM's relationship to L"
    - "L is undecidable only if L also reduces many-one back to A_TM"
  answer: 1
  explanation: "The key transfer property: if A ≤_m B and A is undecidable, then B must be undecidable. Proof by contrapositive — if L were decidable, compose the reduction function f with L's decider to decide A_TM. Since A_TM is not decidable, neither can L be. Option 2 is the most tempting wrong answer: it suggests the reduction is uninformative, but the *direction* A_TM ≤_m L (A_TM maps into L) is precisely what propagates undecidability upward to L. Only if the reduction went the other way (L ≤_m A_TM) would we learn nothing new about L."

- question: "In the many-one reduction A ≤_m B via function f, what does f do?"
  type: multiple-choice
  options:
    - "f decides membership in A by using an oracle for B as a subroutine"
    - "f transforms instances of A into instances of B such that membership is preserved in both directions"
    - "f transforms instances of B into instances of A, allowing A to be solved using B's structure"
    - "f accepts strings in A and rejects strings not in A, using the same steps a B-decider would use"
  answer: 1
  explanation: "The reduction function f maps from A to B: it takes any string w (an instance of A) and produces f(w) (an instance of B) satisfying w ∈ A iff f(w) ∈ B. This is a one-way translation that preserves the yes/no membership answer. Option 2 reverses the direction — it describes B ≤_m A, which is a different and unrelated reduction. Option 0 confuses many-one reducibility with Turing reducibility (oracle computation). The function f is purely a translator; it does not decide A on its own."

- question: "The reduction function f in A ≤_m B must be total — it must halt and produce output for every input string w, including strings not in A."
  type: true-false
  answer: true
  explanation: "Totality is not optional. The composition argument works like this: to decide whether w ∈ A, compute f(w) (which must halt), then run the B-decider on f(w). If f were partial and looped on some inputs, the composed procedure would also loop, breaking the decidability transfer. Crucially, f must produce output for strings *not in A* as well — for those, f(w) must be a string *not in B*, and f must reach this output in finite time. The mapping is defined for the entire domain Σ*, not just strings in A."

- question: "If A ≤_m B and B is undecidable, then A must also be undecidable."
  type: true-false
  answer: false
  explanation: "This is a common inversion of the correct rule. A ≤_m B says A is no harder than B — if B were decidable, A would be too. B being *undecidable* does not pull A up to undecidability. A could be a trivially decidable language (say, the empty language ∅, which a TM can decide by always rejecting) that reduces many-one to an undecidable B via a constant function mapping everything to a string not in B. The useful direction is: if A ≤_m B and *A* is undecidable, then B is undecidable. B's hardness does not constrain A's hardness."

- question: "Explain why the reduction function f must output a *description* of a machine M' rather than running M on w, even though the reduction's correctness depends entirely on M's behavior on w."
  type: short-answer
  answer: "If f ran M on w, f would loop forever on any input where M does not halt — making f partial (undefined for those inputs) and breaking the composition. Instead, f performs only string manipulation: it takes ⟨M, w⟩ as input and outputs a description of a new machine M' that *encodes* contingent behavior ('simulate M on w; if M halts, do X'). Constructing this description is always a finite mechanical operation — f is essentially writing a short program as a string, without executing it. The description of M' is always a finite string producible in bounded time, even if running M' would be infinite."
  explanation: "The 'describe but don't run' pattern is the fundamental technique in computability theory for constructing things that depend on undecidable behavior. It exploits the fact that a Turing machine is just a data structure — a finite description of a computation. You can manipulate, compose, and embed TM descriptions as strings without ever executing them. The constructed M' may run forever when invoked, but its description is always a finite string. Once you internalize this pattern, most undecidability proofs follow a standard template: receive ⟨M, w⟩, construct M' by text manipulation, map to the target language's format."
```

## Explainer

You know from Turing machines that a language is **decidable** if some Turing machine always halts and correctly accepts or rejects every input. Many-one reducibility gives you a way to compare languages by computational difficulty without solving them directly. The definition is precise: A ≤_m B via f means there is a total computable function f such that for *every* string w, the string w belongs to A if and only if f(w) belongs to B. The function f translates the membership question for A into a membership question for B.

The key transfer property is what makes reductions useful. **If A ≤_m B and B is decidable, then A is decidable.** The proof is a simple composition: to decide whether w ∈ A, compute f(w) (which halts since f is total computable), then run the decider for B on f(w). If B accepts, accept; if B rejects, reject. This works because f(w) ∈ B iff w ∈ A. Reading the contrapositive: **if A ≤_m B and A is undecidable, then B is undecidable**. This contrapositive is how you actually use reductions in practice — to prove B is undecidable, reduce a *known* undecidable language to B.

The canonical undecidable language is the **halting problem** H_TM = {⟨M,w⟩ : M halts on w}. To show that a new language L is undecidable, you construct a computable function f such that ⟨M,w⟩ ∈ H_TM iff f(⟨M,w⟩) ∈ L. The key technique is **simulating inside the description**: you construct a new Turing machine M' whose description encodes the behavior of M on w, then map ⟨M,w⟩ to ⟨M'⟩ or some related object. When you verify the reduction, you check both directions of the iff: if ⟨M,w⟩ ∈ H_TM (M does halt on w), show f(⟨M,w⟩) ∈ L; if ⟨M,w⟩ ∉ H_TM (M does not halt), show f(⟨M,w⟩) ∉ L.

A common stumbling block is building f correctly. The function f must be *total* and *computable* — it cannot run M on w itself (that might not halt). Instead, f just *describes* what the constructed machine would do: it outputs a description of M' without executing M. This distinction between describing a computation and running it is at the heart of diagonalization-style arguments. The constructed machine M' typically says something like "simulate M on w; if M halts, then do something." The description of M' is always finite and constructible from ⟨M,w⟩, even though M might run forever if we ever executed it. Once you internalize this "describe but don't run" pattern, many-one reductions become a systematic and powerful tool for mapping the frontier of undecidability.


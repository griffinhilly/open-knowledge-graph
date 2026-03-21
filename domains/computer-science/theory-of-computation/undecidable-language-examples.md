---
id: undecidable-language-examples
title: 'Undecidable Languages: Examples and Techniques'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
- id: diagonalization-and-uncomputability
  type: soft
builds-toward:
- reduction-techniques-undecidability
tags:
- undecidability
- halting
- tm-equivalence
- acceptance
- examples
stage: advanced
status: draft
---

# Undecidable Languages: Examples and Techniques

## Core Idea
Beyond the halting problem, many natural problems are undecidable: equivalence of TMs (do two TMs accept the same language?), universal language (does a TM accept all strings?), and emptiness variants. Some are recognizable (Turing-recognizable) but not decidable; others like the complement of halting are not recognizable. Recognizing undecidability requires more than diagonalization—typically reduction techniques.

## Questions

```yaml
- question: "A programmer wants to write a tool that, given any program P as input, determines whether P outputs 'Hello, World!' for at least one possible input. By Rice's theorem, what can we conclude?"
  type: multiple-choice
  options:
    - "This is possible — the property involves specific output text, not the language structure"
    - "This is undecidable — 'outputs Hello, World! for at least one input' is a nontrivial property of the language P recognizes, so no algorithm can decide it in general"
    - "This is decidable if we restrict to programs without recursive functions"
    - "Rice's theorem only applies to mathematical Turing machines, not real programming languages"
  answer: 1
  explanation: "Rice's theorem covers every nontrivial property of the *language* recognized by a Turing machine (or equivalently, any program). 'Outputs Hello, World! for at least one input' is exactly a nontrivial language property: some programs have it (a program that always prints Hello, World!) and some don't (a program that prints nothing). Rice's theorem applies regardless of whether the property sounds practical — it sweeps up virtually every behavioral question you'd want to ask about programs. Option D is a common misconception: Turing machines are computationally equivalent to real programming languages, so the theorem applies fully."

- question: "The language A_TM = {⟨M, w⟩ : M accepts w} is Turing-recognizable but not decidable. What can we say about the complement of A_TM?"
  type: multiple-choice
  options:
    - "It is decidable, because the complement of a Turing-recognizable language is always decidable"
    - "It is Turing-recognizable but not decidable — the same classification as A_TM itself"
    - "It is not Turing-recognizable — no Turing machine can systematically confirm that M does not accept w"
    - "It is decidable if we restrict to Turing machines with a bounded number of states"
  answer: 2
  explanation: "This illustrates the recognition asymmetry at the heart of computability theory. A_TM is recognizable because we can confirm membership (simulate M on w; if M accepts, halt and accept). But we cannot confirm non-membership: if M doesn't accept w, it might run forever, and we can never distinguish 'still running' from 'will never accept.' The complement of a Turing-recognizable language is co-Turing-recognizable — and a language is decidable if and only if it is *both* Turing-recognizable and co-Turing-recognizable. Since A_TM is not decidable, its complement cannot be Turing-recognizable (otherwise A_TM would be decidable)."

- question: "Rice's theorem implies that whether a Turing machine M has fewer than 100 states is undecidable."
  type: true-false
  answer: false
  explanation: "Rice's theorem applies only to nontrivial properties of the *language recognized* by a TM — that is, properties of what the machine computes, not of the machine's structure. 'Has fewer than 100 states' is a property of the machine's *description* (its construction), not of its language. You can simply count the states in M's formal description — this is a decidable structural inspection. Rice's theorem would apply to 'L(M) is finite' or 'L(M) contains a string of length less than 100' (both language properties), but not to structural machine properties."

- question: "If a language L is Turing-recognizable, then there exists a Turing machine that always halts with a yes-or-no answer for every input."
  type: true-false
  answer: false
  explanation: "Turing-recognizable (recursively enumerable) only guarantees that a TM will halt and *accept* for strings that ARE in the language. For strings not in the language, the TM may loop forever — it is not required to halt and reject. A language is *decidable* (recursive) if and only if there exists a TM that halts on every input with either accept or reject. The halting problem's language A_TM is Turing-recognizable but not decidable: we can recognize membership but cannot always produce a definitive 'no' answer."

- question: "Explain why Rice's theorem makes undecidability the rule rather than the exception for questions about program behavior, and give one example of a question it covers and one it does not."
  type: short-answer
  answer: "Rice's theorem states that every nontrivial property of the language recognized by a Turing machine is undecidable. 'Nontrivial' simply means some TMs have the property and some don't — a remarkably broad category. Virtually every interesting behavioral question about a program fits this definition: 'Does it terminate for all inputs?', 'Does it ever produce output X?', 'Does it compute the correct function?', 'Does it read more than N bytes?' — all are nontrivial language properties and therefore undecidable. Example covered: 'Does this program accept the empty string?' (nontrivial language property — undecidable). Example NOT covered: 'Does this program's description have more than 50 characters?' (a property of the machine's syntactic structure, not of its language — decidable by inspection). This shows that undecidability is not a curiosity of self-referential puzzles; it is a fundamental limitation on the analyzability of programs by programs."
```

## Explainer

The halting problem established that undecidability exists — there is at least one well-defined question that no algorithm can answer in general. But the halting problem might seem like an isolated curiosity, a contrived self-referential puzzle. The purpose of studying further undecidable languages is to show that undecidability is **pervasive**: it infects virtually every nontrivial question you might ask about the behavior of programs.

Consider three natural questions about a Turing machine M. Does M accept at least one string? (**emptiness**: is L(M) = ∅?) Does M accept every string? (**universality**: is L(M) = Σ*?) Do two machines M₁ and M₂ accept the same language? (**equivalence**: is L(M₁) = L(M₂)?) All three are undecidable. The key technique for proving this is **reduction** — showing that if you could solve the new problem, you could use it as a subroutine to solve the halting problem, which you already know is impossible. For instance, to prove universality is undecidable, you construct a Turing machine that "encodes" a halting question into a universality question: if the original machine halts, the constructed machine accepts everything; if not, it misses some string. A solver for universality would then solve halting — contradiction.

An important distinction emerges when you classify these undecidable problems more finely. The language A_TM = {⟨M, w⟩ : M accepts w} is **Turing-recognizable** (also called recursively enumerable): a machine can confirm membership by simulating M on w and halting if M accepts. It just cannot confirm *non*-membership, because M might run forever. The complement of A_TM — the set of ⟨M, w⟩ where M does *not* accept w — is **not even Turing-recognizable**. No machine can systematically confirm that M fails to accept w, because there is no way to distinguish "still running" from "will never accept." This creates a hierarchy: decidable languages sit inside Turing-recognizable languages, which sit inside all languages, with strict containment at each level.

Rice's theorem generalizes these individual results into a sweeping conclusion: **every nontrivial property of the language recognized by a Turing machine is undecidable**. A property is "nontrivial" if some TMs have it and some do not. Whether L(M) is empty, finite, regular, context-free, equal to a specific language — all undecidable, because each is a nontrivial property of L(M). Rice's theorem does not apply to properties of the machine itself (like "does M have fewer than 100 states"), only to properties of the language it recognizes. This theorem transforms undecidability from a collection of individual results into a structural feature of computation: the behavior of programs is, in general, unanalyzable by programs.

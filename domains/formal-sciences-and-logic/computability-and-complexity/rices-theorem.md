---
id: rices-theorem
title: Rice's Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: computability-reductions
  type: hard
- id: church-turing-thesis-formal
  type: soft
builds-toward:
- re-and-co-re-languages
tags:
- undecidability
- semantic-properties
- computability
stage: advanced
status: validated
---

# Rice's Theorem

## Core Idea
Rice's theorem states that every non-trivial semantic property of Turing machines is undecidable. A semantic property is one that depends on the function a TM computes — not its syntactic description — and non-trivial means it is true of some TMs and false of others. Consequently, questions like 'Does this program output 42 on input 5?', 'Does this program halt on all inputs?', or 'Do these two programs compute the same function?' are all undecidable. The proof reduces from the halting problem by showing any non-trivial semantic property could be used to detect halting.

## How It's Best Learned
First internalize the syntactic/semantic distinction — properties of program descriptions versus properties of the functions they compute. Then work through the formal proof by contradiction, understanding how any non-trivial semantic property can be co-opted to solve the halting problem.

## Common Misconceptions
- Rice's theorem applies to semantic properties, not syntactic ones — checking whether a program has exactly 10 states is syntactic and decidable.
- The theorem does not mean nothing useful can be verified; static analysis and type checking examine syntactic overapproximations of semantic properties.

## Explainer

The halting problem showed that one specific question about programs — "does this program halt on this input?" — is undecidable. Rice's theorem is a sweeping generalization: *every* interesting question about what a program computes is undecidable. The key distinction that makes this precise is between **syntactic** and **semantic** properties. A syntactic property depends on the description of the Turing machine — its states, transitions, tape alphabet. A semantic property depends only on the function the machine computes, regardless of how it is encoded. "This TM has fewer than 100 states" is syntactic. "This TM outputs 42 on input 5" is semantic.

To see why semantic properties are harder, notice that two machines with wildly different descriptions might compute the same function, and two nearly-identical machines might compute completely different functions. You cannot read off what a program computes from its description without, in effect, running it. Rice's theorem makes this precise: if P is a semantic property that is non-trivial (some TMs have it, some don't), then there is no algorithm that takes a TM description and correctly decides whether that TM has property P.

The proof uses the halting problem reduction you already know. Suppose you had an algorithm A deciding property P. Pick a TM M₀ that has P (exists by non-triviality) and a TM M₁ that lacks P. Given any TM T and input w, build a new TM T_{w} that: (1) first runs T on w, and (2) if T halts, runs as M₀, otherwise diverges forever. The machine T_{w} computes M₀'s function if T halts on w, and computes nothing (or M₁'s function) if T doesn't halt. Now run A on T_{w}: A answers "yes" iff T halts on w. This solves the halting problem — a contradiction. Every part of this construction generalizes to any non-trivial semantic property.

The practical implication is profound: no static analysis tool can be both sound and complete for any semantic property. Tools like type checkers and linters are always either incomplete (they miss some bugs) or unsound (they report false positives) — not from engineering failure, but from fundamental mathematical necessity. Rice's theorem explains why program verification is hard in principle, and why all practical static analysis tools approximate semantic properties through syntactic overapproximations.

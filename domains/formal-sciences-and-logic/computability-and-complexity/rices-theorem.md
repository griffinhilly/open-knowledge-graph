---
id: rices-theorem
title: Rice's Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem
  type: hard
- id: computability-reductions
  type: hard
- id: church-turing-thesis
  type: soft
builds-toward:
- re-and-co-re-languages
tags:
- undecidability
- semantic-properties
- computability
stage: advanced
status: draft
---

# Rice's Theorem

## Core Idea
Rice's theorem states that every non-trivial semantic property of Turing machines is undecidable. A semantic property is one that depends on the function a TM computes — not its syntactic description — and non-trivial means it is true of some TMs and false of others. Consequently, questions like 'Does this program output 42 on input 5?', 'Does this program halt on all inputs?', or 'Do these two programs compute the same function?' are all undecidable. The proof reduces from the halting problem by showing any non-trivial semantic property could be used to detect halting.

## How It's Best Learned
First internalize the syntactic/semantic distinction — properties of program descriptions versus properties of the functions they compute. Then work through the formal proof by contradiction, understanding how any non-trivial semantic property can be co-opted to solve the halting problem.

## Common Misconceptions
- Rice's theorem applies to semantic properties, not syntactic ones — checking whether a program has exactly 10 states is syntactic and decidable.
- The theorem does not mean nothing useful can be verified; static analysis and type checking examine syntactic overapproximations of semantic properties.

---
id: decidability-and-semi-decidability
title: Decidable and Semi-Decidable Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: hard
builds-toward:
- re-and-co-re-languages
- reducibility-many-one-formal
tags:
- decidability
- languages
- recognition
stage: advanced
status: draft
---

# Decidable and Semi-Decidable Languages

## Core Idea
A language is decidable (in RE ∩ co-RE) if a Turing machine can recognize it and also recognize its complement. A language is semi-decidable (RE) if a machine can recognize membership but may loop indefinitely on non-members. The halting problem is semi-decidable but not decidable, illustrating the fundamental gap between 'can verify a solution' and 'can decide membership.'

## How It's Best Learned
Construct machines that decide versus semi-decide simple languages (e.g., palindromes vs. Gödel numbers of terminating programs).

## Common Misconceptions
- Treating 'semi-decidable' as 'almost decidable' (the gap is absolute: a machine cannot bound the time before giving up).
- Confusing co-RE with the complement of a language (co-RE is the complement in the recursion-theoretic hierarchy).

## Explainer

You already know what a Turing machine is and that the halting problem cannot be solved — no TM can decide, for every input, whether an arbitrary program halts. Build on that foundation by asking a more refined question: what kinds of problems can a Turing machine *partially* solve? The answer carves computational problems into two fundamental classes. A language L is **decidable** (also called recursive) if there exists a TM that always halts and correctly answers "yes" or "no" for every input. A language is **semi-decidable** (also called recursively enumerable, or RE) if there exists a TM that halts and accepts on every input in L, but may run forever on inputs not in L. The machine can confirm membership but cannot always confirm non-membership.

The halting problem is the canonical semi-decidable language. You can simulate a given program and halt as soon as it halts — outputting "yes." But if the program runs forever, your simulator also runs forever, never giving a "no" answer. This is why the halting problem is semi-decidable but not decidable: the asymmetry between "yes" and "no" witnesses is fundamental, not a gap to be closed with a cleverer algorithm.

The key structural insight is that decidability requires both the language *and* its complement to be semi-decidable. If L is RE and its complement L̄ is also RE, you can run both machines in parallel (dovetailing): whichever one accepts first gives you the answer. Since every input is either in L or in L̄, one machine will eventually halt, giving a total decision procedure. This characterizes decidability as RE ∩ **co-RE**, where co-RE is the class of languages whose complements are RE. The halting problem is RE but not co-RE — you cannot semi-decide non-halting — so it is not decidable.

The gap between semi-decidable and decidable is not a matter of degree. It is absolute. There is no way to "time-limit" a semi-decision procedure and get a correct answer — doing so would sometimes incorrectly reject valid inputs that would have been accepted eventually. This asymmetry drives the entire hierarchy of undecidability: problems above the decidable level are classified by whether they are RE, co-RE, or neither, and by how hard they are relative to each other under reducibility. Everything you will encounter about reduction, completeness, and the RE and co-RE hierarchies flows from this basic trichotomy.

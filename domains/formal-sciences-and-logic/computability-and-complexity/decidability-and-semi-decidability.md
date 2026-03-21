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

## Questions

```yaml
- question: "What does it mean to say the halting problem is semi-decidable?"
  type: multiple-choice
  options:
    - "There exists a Turing machine that always halts and correctly answers 'yes' or 'no' for every input"
    - "There exists a Turing machine that halts and accepts whenever a program halts on its input, but may run forever when the program does not halt"
    - "The halting problem can be decided in exponential time but not polynomial time"
    - "The halting problem is almost decidable — a small fraction of inputs cannot be determined"
  answer: 1
  explanation: "Semi-decidable means there is a TM that accepts every member of the language (here: every (program, input) pair where the program halts) but may run forever on non-members. For the halting problem: simulate the given program. If it halts, output 'yes' and halt. If it runs forever, your simulator also runs forever — never producing a 'no.' You can confirm halting but cannot confirm non-halting. Option A describes decidability. Option C confuses decidability with computational complexity. Option D misrepresents the gap as quantitative — it is absolute."

- question: "A language L is recursively enumerable (RE). Its complement L̄ is also recursively enumerable. What can we conclude?"
  type: multiple-choice
  options:
    - "L is undecidable, because two RE machines cannot decide a language"
    - "L is decidable, because we can run both machines in parallel and one will always halt with the correct answer"
    - "L is in co-RE but not necessarily in RE"
    - "Nothing — knowing both L and L̄ are RE tells us only that L is semidecidable in both directions"
  answer: 1
  explanation: "If both L and L̄ are RE, dovetail two TMs: M₁ that semi-decides L and M₂ that semi-decides L̄. For any input x, either x ∈ L or x ∈ L̄ — one of the two machines will eventually halt and accept. Run both in parallel (alternating steps); whichever accepts first gives the decision. This constructs a TM that always halts with the correct yes/no answer — a decider. Decidability equals RE ∩ co-RE, and having both L ∈ RE and L̄ ∈ RE (which means L ∈ co-RE) is exactly that intersection."

- question: "If a language L is decidable, then its complement L̄ is also decidable."
  type: true-false
  answer: true
  explanation: "If TM M decides L (always halts, accepts on L-members, rejects on non-members), construct M̄ by swapping the accept and reject states. M̄ accepts exactly the inputs M rejects — which are the non-members of L, i.e., the members of L̄. M̄ always halts (because M always halts) and correctly decides L̄. Decidability is closed under complementation. This contrasts with semi-decidability: the halting problem is RE but its complement (non-halting) is not RE, so RE is not closed under complementation."

- question: "A semi-decidable language can be made decidable by adding a timeout: if the Turing machine does not halt within some fixed number of steps, output 'no.'"
  type: true-false
  answer: false
  explanation: "This is the most tempting misconception about semi-decidability. Adding a timeout creates a TM that always halts, but it no longer correctly decides the language — it incorrectly rejects inputs that would have been accepted after more steps. The gap between semi-decidable and decidable is absolute: no finite timeout can serve as a correct 'no' witness, because for any timeout value T, there are programs that halt after T+1 steps. You cannot know in advance how long to wait, and no bound works for all inputs simultaneously."

- question: "Explain why the gap between semi-decidable and decidable is 'absolute' — why can't a semi-decision procedure be converted into a decision procedure by limiting computation time?"
  type: short-answer
  answer: "A semi-decision procedure has an asymmetry: it can produce 'yes' witnesses (accepting) but never produces 'no' witnesses — it just runs forever on non-members. To convert it to a decider, you'd need a finite time after which you can safely output 'no.' But for the halting problem, programs can take arbitrarily long to halt: for any timeout T you choose, there exist programs that halt on step T+1. Stopping at T and outputting 'no' would incorrectly reject those programs. There is no computable function that bounds the runtime of all halting programs, so no timeout is correct for all inputs. The gap is absolute because 'may run forever on non-members' cannot be made finite by a computable bound."
  explanation: "The reason this fails is that the set of programs that halt within T steps grows as T grows, but is never the complete set of halting programs. Deciding membership in the halting problem would require knowing, for an arbitrary program, whether it eventually halts — which is exactly the undecidable question you started with. Any timeout-based approach simply relocates the problem rather than solving it."
```

## Explainer

You already know what a Turing machine is and that the halting problem cannot be solved — no TM can decide, for every input, whether an arbitrary program halts. Build on that foundation by asking a more refined question: what kinds of problems can a Turing machine *partially* solve? The answer carves computational problems into two fundamental classes. A language L is **decidable** (also called recursive) if there exists a TM that always halts and correctly answers "yes" or "no" for every input. A language is **semi-decidable** (also called recursively enumerable, or RE) if there exists a TM that halts and accepts on every input in L, but may run forever on inputs not in L. The machine can confirm membership but cannot always confirm non-membership.

The halting problem is the canonical semi-decidable language. You can simulate a given program and halt as soon as it halts — outputting "yes." But if the program runs forever, your simulator also runs forever, never giving a "no" answer. This is why the halting problem is semi-decidable but not decidable: the asymmetry between "yes" and "no" witnesses is fundamental, not a gap to be closed with a cleverer algorithm.

The key structural insight is that decidability requires both the language *and* its complement to be semi-decidable. If L is RE and its complement L̄ is also RE, you can run both machines in parallel (dovetailing): whichever one accepts first gives you the answer. Since every input is either in L or in L̄, one machine will eventually halt, giving a total decision procedure. This characterizes decidability as RE ∩ **co-RE**, where co-RE is the class of languages whose complements are RE. The halting problem is RE but not co-RE — you cannot semi-decide non-halting — so it is not decidable.

The gap between semi-decidable and decidable is not a matter of degree. It is absolute. There is no way to "time-limit" a semi-decision procedure and get a correct answer — doing so would sometimes incorrectly reject valid inputs that would have been accepted eventually. This asymmetry drives the entire hierarchy of undecidability: problems above the decidable level are classified by whether they are RE, co-RE, or neither, and by how hard they are relative to each other under reducibility. Everything you will encounter about reduction, completeness, and the RE and co-RE hierarchies flows from this basic trichotomy.

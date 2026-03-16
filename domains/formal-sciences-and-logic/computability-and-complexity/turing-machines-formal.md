---
id: turing-machines-formal
title: Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: soft
- id: algorithm-complexity
  type: soft
- id: binary-relations
  type: soft
- id: mathematical-induction
  type: soft
- id: set-theory-basics
  type: soft
- id: algorithm-analysis-big-o
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: hard
- id: proof-structure-and-terminology
  type: soft
builds-toward:
- church-turing-thesis-formal
- halting-problem-formal
- nondeterministic-turing-machines
- kolmogorov-complexity
- time-complexity-classes-formal
tags:
- computation
- automata
- models-of-computation
stage: advanced
status: validated
---

# Turing Machines

## Core Idea
A Turing machine is an abstract computational device consisting of an infinite tape, a read/write head, and a finite set of states with transition rules. It can simulate any algorithmic process and serves as the foundational formal model of computation. Despite its simplicity, no physically realizable computing device has been shown to exceed its computational power. The model precisely defines what it means for a function to be computable and for a language to be decidable or recognizable.

## How It's Best Learned
Start by tracing simple Turing machines by hand on concrete inputs — e.g., a machine that accepts palindromes or increments a binary number. Build familiarity with the state-transition diagram formalism before studying multi-tape variants and their polynomial-time equivalence to single-tape machines.

## Common Misconceptions
- Turing machines are not infinite in practice; the tape is potentially infinite but only a finite prefix is ever used on any terminating computation.
- A Turing machine that loops forever on an input does NOT accept it — acceptance requires halting in a designated accept state.

## Questions

```yaml
- question: "A Turing machine M is run on input w and runs forever without halting. Which of the following is true?"
  type: multiple-choice
  options: ["M accepts w", "M rejects w", "M neither accepts nor rejects w — it loops", "M accepts w if the tape contains only blank symbols after finite steps"]
  answer: 2
  explanation: "Acceptance requires halting in a designated accept state; rejection requires halting in a reject state. Looping forever is a distinct third outcome — the machine neither accepts nor rejects. This is fundamental: the halting problem asks whether we can determine, for arbitrary M and w, which of these three outcomes will occur. The answer is no — no Turing machine can decide this in general."

- question: "Because a Turing machine's tape is infinite, any real simulation of a Turing machine would require an unbounded amount of memory."
  type: true-false
  answer: false
  explanation: "On any terminating computation, only a finite portion of the tape is ever visited or written. The tape is 'potentially infinite' as a theoretical convenience — guaranteeing the machine never runs out of scratch space — but a real computation halts after finitely many steps, having touched only finitely many cells. The infinite tape is an abstraction that removes resource constraints from the model, not a requirement for infinite physical memory."

- question: "What does it mean for a function f: Σ* → Σ* to be Turing-computable?"
  type: short-answer
  answer: "There exists a Turing machine that, when started on any input w encoding an argument in the function's domain, always halts and leaves the encoding of f(w) on the tape."
  explanation: "Turing-computability is the formal definition of 'algorithmically computable.' A function is computable if a Turing machine can produce the correct output for every valid input and always terminates. Functions that cannot be computed by any TM — such as the function that maps (M, w) to 1 if M halts on w and 0 otherwise — are formally uncomputable, regardless of how much time or memory is available."
```

## Explainer

A Turing machine is the simplest formal device that captures what we mean by "algorithm." It has four components: an infinite tape of cells each holding a symbol from a finite alphabet, a read/write head positioned over one cell, a finite set of states (including a designated start state and accept/reject states), and a transition function. At each step the machine reads the symbol under the head, consults the transition function to decide what symbol to write, which direction to move the head, and which state to enter next. That is the complete description — yet this minimal device can simulate any computation ever devised.

The transition function is the heart of the machine. Formally it is a partial function δ: Q × Γ → Q × Γ × {L, R}, where Q is the set of states and Γ is the tape alphabet. From your study of functions-and-function-properties, you know a partial function need not be defined on all inputs. When the machine reaches a configuration for which δ is undefined, it halts. The three possible outcomes — accept (halts in accept state), reject (halts in reject state), loop (never halts) — are all distinct. A language is decidable if some TM accepts every string in the language and rejects every string outside it, always halting. A language is merely recognizable if some TM accepts every string in the language but may loop forever on strings not in it. This distinction, which you will explore when studying the halting problem, is the deepest divide in computability theory.

The infinite tape is a theoretical abstraction, not a practical requirement. On any halting computation, only finitely many cells are ever touched — the tape head can only advance one cell per step, and there are only finitely many steps before halting. The infinite tape removes the awkward question of "what if the machine needs more space?" from the theory, letting us focus on what is computably possible rather than what fits in finite memory. Think of it as an idealized scratch pad that never fills up.

Multi-tape Turing machines, nondeterministic Turing machines, and even random-access machines are all equivalent in computational power to the basic single-tape deterministic model. They differ in efficiency — a k-tape machine can be simulated by a single-tape machine with at most a quadratic slowdown — but not in what they can compute at all. This robustness is why the Turing machine is the standard model: the Church-Turing thesis holds that any effectively computable function is Turing-computable, making the TM the formal definition of computation itself. The limits of Turing machines are therefore the limits of all possible algorithms.

---
id: partial-vs-total-recursive-functions
title: Partial vs. Total Recursive Functions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: general-recursive-functions
  type: hard
- id: mu-recursive-functions
  type: hard
builds-toward:
- decidability-and-semi-decidability
- halting-problem-formal
tags:
- recursion
- partial-functions
- computability
stage: advanced
status: draft
---

# Partial vs. Total Recursive Functions

## Core Idea
Partial recursive functions (computable by Turing machines) may not halt on all inputs, while total recursive functions halt on every input. Not all computable functions are total: the halting problem shows no total recursive function can predict if an arbitrary program halts. This gap between partial and total computability is foundational to undecidability.

## How It's Best Learned
Write examples of partial functions (e.g., integer division when denominator is computed) and total functions, then study the proof that some total functions are not computable.

## Common Misconceptions
- Assuming a computable partial function can always be extended to a total function.
- Confusing 'total recursive function' with 'algorithm that works' (many algorithms naturally admit partial functions).

## Explainer

You have already studied general recursive (µ-recursive) functions, which extend primitive recursion with the **minimization operator** µ. The µ-operator searches for the least input satisfying a predicate — and it may search forever if no such input exists. This possibility of non-termination is precisely what introduces **partiality**: a **partial recursive function** is one that may be undefined on some inputs (meaning a Turing machine computing it diverges on those inputs). A **total recursive function**, by contrast, halts and returns a value on every input without exception.

Partiality is not a defect in the theory; it is an unavoidable feature of any sufficiently powerful computational model. Any system capable of simulating other programs — including Turing machines — will inevitably contain programs that loop forever on some inputs. You cannot excise all non-terminating programs while preserving the same expressive power. More precisely, the set of total recursive functions is not recursively enumerable: there is no algorithm that, given a program description, decides whether that program is total.

This asymmetry is the crux of the halting problem's undecidability, which you will explore next. If totality were decidable, you could decide halting: to ask whether M halts on w, build a new function f that, on any input, simulates M on w and outputs 0 if M halts — then ask whether f is total. Since halting is undecidable, totality must be undecidable too. The argument works by a diagonalization similar to Cantor's: any hypothetical totality-tester could be used to construct a self-defeating function, producing a contradiction.

The practical lesson is directional: computability and termination are distinct properties that do not imply each other. You can write a partial function that always gives the correct answer whenever it terminates, or a total function that always terminates but cannot solve certain problems at all. The partial recursive functions are exactly the **computable functions** — those computed by some Turing machine. The total computable functions are a strict subset. The gap between "total recursive" and "all total functions" contains functions that are always defined yet cannot be computed by any algorithm, and understanding that gap is a central project of computability theory.

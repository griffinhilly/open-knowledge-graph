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
stage: formal-systems
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

## Questions

```yaml
- question: "A programmer writes a function f that is computable and she has proven it halts on every possible input. What is the correct classification of f?"
  type: multiple-choice
  options:
    - "f is a total recursive function, because it is computable and halts for all inputs"
    - "f is partial recursive but not total, because all computable functions may fail to terminate on some inputs"
    - "f is primitive recursive but not total recursive, because total recursive functions require additional proof techniques"
    - "f cannot be classified without knowing whether it uses the µ-operator"
  answer: 0
  explanation: "A total recursive function is exactly a function computed by some Turing machine (or equivalent formalism) that halts and returns a value on every input. 'Total' means 'halts for all inputs,' and 'recursive' means 'computable.' The programmer's function satisfies both conditions. Option B is the classic misconception: partial recursive functions are those that *may* fail to terminate on some inputs, not all computable functions. A computable function that provably terminates everywhere is by definition total recursive."

- question: "A theorem states that the set of total recursive functions is not recursively enumerable. What does this imply for a hypothetical program TOTAL(f) that claims to decide whether any given program f halts on every input?"
  type: multiple-choice
  options:
    - "TOTAL(f) would need to run f on all inputs before deciding, but could still halt in principle for finite input domains"
    - "TOTAL(f) cannot exist as a computable algorithm — deciding totality is undecidable"
    - "TOTAL(f) exists but requires exponential time to terminate"
    - "TOTAL(f) exists for all primitive recursive programs but fails only for µ-recursive programs"
  answer: 1
  explanation: "If TOTAL(f) existed as a total recursive function, it would semi-decide which programs halt on all inputs. But totality is undecidable by reduction from the halting problem: to ask whether M halts on w, build a new function g that simulates M on w on any input; g is total iff M halts on w. Since halting is undecidable, totality is undecidable. The non-enumerability result is even stronger: you cannot even semi-decide totality — there is no algorithm that accepts exactly the total programs."

- question: "Every partial recursive function can be extended to a total recursive function by defining its output to be 0 on inputs where it would otherwise diverge."
  type: true-false
  answer: false
  explanation: "This is a common misconception. While you can mathematically define a total function that agrees with f on halting inputs and outputs 0 elsewhere, this extended function is not necessarily computable. Computing it requires knowing which inputs cause f to diverge — but recognizing the domain of a partial recursive function is not in general computable (it is equivalent to the halting problem). So although a total extension exists as a mathematical object (a set of ordered pairs), there need not be any algorithm that computes it. You cannot freely convert a partial computable function into a total computable one."

- question: "A function that is defined (returns a value) for every natural number input must be computable by some Turing machine."
  type: true-false
  answer: false
  explanation: "Totality and computability are independent properties. The total computable functions are a strict subset of all total functions. There exist functions provably defined on every input that are not computable by any Turing machine — the Busy Beaver function Σ(n) is a classic example: it is defined for every n (it counts something specific), but it grows faster than any computable function and cannot be computed algorithmically. The gap between 'all total functions' and 'total computable functions' is a central object of study in computability theory."

- question: "Explain why partiality is unavoidable in any sufficiently powerful computational model: why can't we simply restrict to total programs while keeping the same expressive power?"
  type: short-answer
  answer: "Any computational model powerful enough to simulate arbitrary programs — including itself — will necessarily contain programs that loop forever on some inputs. If you try to restrict to only total programs while keeping full expressive power (the ability to compute all computable functions), you face a diagonalization argument: given any enumeration of supposedly total programs, you can construct a function that differs from each one on some input — this new function is total (defined everywhere) but cannot be in your enumeration, so your enumeration was incomplete. More concretely, the set of total recursive functions is not recursively enumerable, meaning no algorithm can enumerate all of them. Any programming language that guarantees termination — like a proof assistant's type-checked term language — necessarily sacrifices the ability to compute some computable functions."
  explanation: "This connects the partial/total distinction to the fundamental limits of formalism. Dependently-typed proof assistants like Coq and Agda guarantee termination through structural recursion but cannot compute all computable functions. General-purpose languages (Python, C) admit all computable functions but inevitably include non-terminating programs. This is not a design failure — it is a mathematical necessity that follows from diagonalization."
```

## Explainer

You have already studied general recursive (µ-recursive) functions, which extend primitive recursion with the **minimization operator** µ. The µ-operator searches for the least input satisfying a predicate — and it may search forever if no such input exists. This possibility of non-termination is precisely what introduces **partiality**: a **partial recursive function** is one that may be undefined on some inputs (meaning a Turing machine computing it diverges on those inputs). A **total recursive function**, by contrast, halts and returns a value on every input without exception.

Partiality is not a defect in the theory; it is an unavoidable feature of any sufficiently powerful computational model. Any system capable of simulating other programs — including Turing machines — will inevitably contain programs that loop forever on some inputs. You cannot excise all non-terminating programs while preserving the same expressive power. More precisely, the set of total recursive functions is not recursively enumerable: there is no algorithm that, given a program description, decides whether that program is total.

This asymmetry is the crux of the halting problem's undecidability, which you will explore next. If totality were decidable, you could decide halting: to ask whether M halts on w, build a new function f that, on any input, simulates M on w and outputs 0 if M halts — then ask whether f is total. Since halting is undecidable, totality must be undecidable too. The argument works by a diagonalization similar to Cantor's: any hypothetical totality-tester could be used to construct a self-defeating function, producing a contradiction.

The practical lesson is directional: computability and termination are distinct properties that do not imply each other. You can write a partial function that always gives the correct answer whenever it terminates, or a total function that always terminates but cannot solve certain problems at all. The partial recursive functions are exactly the **computable functions** — those computed by some Turing machine. The total computable functions are a strict subset. The gap between "total recursive" and "all total functions" contains functions that are always defined yet cannot be computed by any algorithm, and understanding that gap is a central project of computability theory.

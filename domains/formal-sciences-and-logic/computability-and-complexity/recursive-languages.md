---
id: recursive-languages
title: 'Recursive Languages: The Decidable Languages'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: soft
- id: set-fundamentals
  type: hard
- id: functions-and-function-properties
  type: soft
builds-toward:
- recursively-enumerable-languages
- complexity-class-definitions-hierarchy
tags:
- decidability
- recursive
- formal-languages
- algorithms
stage: advanced
status: draft
---

# Recursive Languages: The Decidable Languages

## Core Idea
A language is recursive (or decidable) if there exists a Turing machine that halts on every input and accepts exactly those strings in the language. Recursive languages form a proper subset of recursively enumerable languages; they represent problems that can be completely solved by algorithms.

## Explainer

You already know what a Turing machine is and what it means for a machine to accept or reject a string. The class of **recursive** (decidable) languages is defined by a stricter requirement: not just that the machine accepts the right strings, but that it *always halts*. A **decider** for a language L is a Turing machine that, for every input, either accepts (if the input is in L) or rejects (if not), and always terminates. This "always halts" condition is what separates recursion from mere recognizability.

The distinction from recursively enumerable (RE) languages is crucial. An RE language only needs a machine that accepts members — it is allowed to run forever on non-members. This asymmetry means RE recognition is a weaker guarantee: you can confirm membership but never confirm non-membership (the machine might just be running slowly). A recursive language is symmetric: membership and non-membership are both decidable in finite time. Equivalently, a language is recursive if and only if both it and its complement are RE — recognizers for both sides can be run in parallel, and whichever halts first gives the answer.

Concrete examples ground the concept. The language of palindromes is recursive: a TM scans the input, compares first and last characters repeatedly, and always halts. The language of strings of the form aⁿbⁿcⁿ is recursive. Regular and context-free languages are all recursive — membership in these classes is decidable by finite automata and pushdown automata, which always halt. Contrast these with the halting problem: no TM can decide, for all pairs (M, w), whether M halts on w. The halting problem is RE but not recursive.

Recursive languages correspond precisely to the class of problems solvable by algorithms in the informal sense — the Church-Turing thesis equates "algorithmically solvable" with "recursive." This is why the class is also called **decidable**. When you study complexity theory next, you will refine decidability further by asking not just whether a problem is solvable, but how efficiently — with polynomial-time deciders corresponding to the class P. The recursive languages form the outer boundary of tractability; the study of what lies outside (RE but not recursive, or not even RE) is the study of undecidability.

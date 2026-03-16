---
id: programming-fundamentals-switch-case
title: Switch-Case Statements
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-if-else-statements
  type: soft
tags:
- control-flow
- switch
- case
stage: abstract-reasoning
status: draft
---

# Switch-Case Statements

## Core Idea
Switch-case statements provide a cleaner alternative to if-else-if chains for testing a single value against multiple cases. Each case runs a block of code if its value matches; a default case runs if no case matches.

## Explainer

You have already used if-else-if chains to make decisions based on conditions. They work fine when you have two or three branches, but imagine you are building a menu system with ten options, or handling day-of-the-week logic. An if-else chain testing the same variable against ten different values becomes repetitive and hard to scan. A **switch-case statement** is designed for exactly this situation: you provide a single expression to evaluate, and the program jumps directly to the matching **case** label.

The basic structure looks like this: `switch(expression)` followed by a series of `case value:` blocks. The expression is evaluated once, and execution jumps to the case whose value matches. If no case matches, the **default** case runs — it is the catch-all, analogous to the final `else` in an if-else chain. One critical detail that trips up beginners in languages like C, Java, and JavaScript is **fall-through**: without a `break` statement at the end of each case block, execution continues into the next case below it. This means that if case 1 matches and has no `break`, the code for case 2 also runs, then case 3, and so on. Fall-through is occasionally useful for grouping multiple cases that share the same logic, but unintentional fall-through is a common source of bugs.

Think of a switch-case like a building directory in a lobby. You look at the directory (the switch expression), find your floor number (the matching case), and go directly there. You do not check every floor on the way up — you jump straight to the right one. This direct dispatch makes switch-case not only more readable than a long if-else chain, but in many compiled languages it is also more efficient, because the compiler can build a jump table instead of evaluating conditions one by one. Not every language supports switch — Python, for example, only added structural pattern matching (`match-case`) in version 3.10 — but the concept appears in most mainstream languages and is worth recognizing whenever you are branching on a single value against a known set of possibilities.

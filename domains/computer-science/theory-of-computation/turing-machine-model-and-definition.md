---
id: turing-machine-model-and-definition
title: Turing Machine Model and Formal Definition
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: pushdown-automata-and-equivalence
  type: soft
builds-toward:
- multi-tape-turing-machines
- universal-turing-machine
tags:
- turing-machine
- tape
- head
- control
- acceptance
- computation
stage: advanced
status: draft
---

# Turing Machine Model and Formal Definition

## Core Idea
A Turing machine has a finite control, infinite tape, and read-write head. Each step: read symbol, change state, write symbol, move head. TMs formalize algorithms without committing to specifics of implementation. A TM accepts if it halts in an accepting state; computes a function if halting output is well-defined. TMs embody the Church-Turing thesis about the limits of computation.

## Explainer

Having studied finite automata and pushdown automata, you have seen increasingly powerful computational models — each one recognizing a strictly larger class of languages than the last. A **Turing machine** represents the final step in this hierarchy: a model powerful enough to capture everything we intuitively mean by "algorithm." The formal definition is a 7-tuple (Q, Σ, Γ, δ, q₀, q_accept, q_reject), where Q is the finite set of states, Σ is the input alphabet (not including the blank symbol), Γ is the tape alphabet (including Σ and the blank symbol), δ is the transition function, q₀ is the start state, and q_accept and q_reject are the accepting and rejecting halt states.

The key difference from previous models is the **infinite read-write tape**. A finite automaton can only read input left-to-right with no memory beyond its current state. A pushdown automaton adds a stack — useful, but limited to last-in-first-out access. A Turing machine has an unbounded tape that it can read from, write to, and move across in both directions. This tape serves simultaneously as the input medium, the working memory, and the output medium. At each step, the machine reads the symbol under its head, and the transition function δ(q, a) specifies three things: the new state to enter, the symbol to write in the current cell, and whether to move the head left or right. This simple loop — read, write, move, change state — is all a Turing machine ever does.

A Turing machine can do one of three things on a given input: **accept** (halt in q_accept), **reject** (halt in q_reject), or **loop forever** (never halt). This three-way distinction is important. A language is **decidable** (recursive) if some TM always halts and correctly accepts or rejects every input. A language is **recognizable** (recursively enumerable) if some TM accepts every string in the language but might loop forever on strings not in it. The difference matters enormously: decidable problems are the ones we can actually solve algorithmically, while merely recognizable problems represent a weaker guarantee where "no" answers may never arrive.

The power of this simple model is captured by the **Church-Turing thesis**: any function that can be computed by any mechanical process — by any programming language, any physical computer, any algorithm described in pseudocode — can be computed by a Turing machine. This is not a theorem (it cannot be proved, since "mechanical process" is informal) but rather a definitional claim that has withstood every attempt at refutation since the 1930s. Every programming language you have ever used, every computer ever built, computes exactly the class of functions that Turing machines compute. Some machines are faster, some use less memory, but none compute anything a Turing machine cannot. This is why the Turing machine serves as the foundation for all of computability and complexity theory: it gives us a single, precise model against which to measure what is and is not computable.

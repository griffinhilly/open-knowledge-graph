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
status: validated
---

# Turing Machine Model and Formal Definition

## Core Idea
A Turing machine has a finite control, infinite tape, and read-write head. Each step: read symbol, change state, write symbol, move head. TMs formalize algorithms without committing to specifics of implementation. A TM accepts if it halts in an accepting state; computes a function if halting output is well-defined. TMs embody the Church-Turing thesis about the limits of computation.

## Questions

```yaml
- question: "A Turing machine is run on an input string and runs for 10 million steps without halting. What can we conclude?"
  type: multiple-choice
  options:
    - "The input is rejected, because TMs must halt to give an answer"
    - "The TM has a bug — a correct TM always halts on all inputs"
    - "The input is in a language that is not decidable"
    - "Nothing definitive — the machine may be looping forever, or it may halt at step 10 million and one"
  answer: 3
  explanation: "A Turing machine has three possible behaviors: accept (halt in q_accept), reject (halt in q_reject), or loop forever. Observing that a TM has not halted after any finite number of steps does not tell us which of these will ultimately happen — the machine might halt on the very next step, or never. This is precisely why 'recognizable but not decidable' languages exist: a recognizer will eventually accept strings in the language, but on strings not in the language, it may loop forever. We can never distinguish 'running slowly' from 'looping forever' by observation alone."

- question: "How does a Turing machine differ most fundamentally from a pushdown automaton?"
  type: multiple-choice
  options:
    - "A TM can move its head in both directions and write to the tape; a PDA has only read-only left-to-right input and a LIFO stack"
    - "A TM has more states than a PDA"
    - "A TM uses an infinite input tape while a PDA's stack is finite"
    - "A TM can be nondeterministic while a PDA cannot"
  answer: 0
  explanation: "The critical difference is the nature of the memory mechanism and head movement. A PDA augments a finite automaton with a stack — powerful, but limited to last-in-first-out access; once a symbol is buried in the stack, it cannot be accessed until everything above it is popped. The head also moves only left-to-right. A Turing machine's tape allows random access (by moving left or right) and supports reading *and* writing, making the tape simultaneously input, workspace, and output. This bidirectional read-write tape is what elevates TMs above PDAs in computational power. Number of states is irrelevant — power comes from the data structure, not state count."

- question: "A language that is Turing-recognizable (recursively enumerable) is also Turing-decidable (recursive), because any machine that accepts strings in the language can be modified to also reject strings outside it."
  type: true-false
  answer: false
  explanation: "This is the central confusion between recognizability and decidability. A recognizer accepts strings in the language but may loop forever on strings not in the language — it never explicitly rejects them. A decider always halts (with accept or reject) on every input. The two classes are strictly different: the Halting Problem is Turing-recognizable but not Turing-decidable. There is no general procedure to convert a recognizer into a decider because doing so would require solving the Halting Problem itself. The existence of this gap is one of the most important results in computability theory."

- question: "The Church-Turing thesis claims that every problem solvable by a modern computer is also solvable by a Turing machine, because modern computers are just very fast Turing machines."
  type: true-false
  answer: true
  explanation: "The Church-Turing thesis asserts that any function computable by an effective mechanical process is computable by a Turing machine. Modern computers — regardless of architecture — compute exactly the same class of functions as Turing machines (though often much faster and with practical memory constraints). The thesis is not a theorem that can be formally proved, since 'mechanical process' is an informal notion, but it has been validated by the fact that every proposed computational model (lambda calculus, RAM machines, cellular automata, programming languages) has been shown to be Turing-equivalent. Speed and memory differ; computational power does not."

- question: "What is the significance of the distinction between a Turing machine that loops forever versus one that explicitly rejects, and why does this matter for the languages we can compute?"
  type: short-answer
  answer: "When a TM halts in q_reject, it gives a definitive 'no' answer. When it loops forever, no answer ever arrives — we can never distinguish 'will eventually reject' from 'will run forever.' A language is decidable only if some TM always halts (accept or reject) on every input; it is merely recognizable if a TM accepts all strings in the language but may loop on strings not in it. This distinction matters enormously: decidable problems are the ones we can reliably solve algorithmically for all inputs, while the merely recognizable ones — like the Halting Problem — have no algorithm that works for all inputs. The looping case is the source of undecidability."
  explanation: "The asymmetry between accept and loop/reject is what makes the Halting Problem undecidable. A recognizer for the Halting Problem exists: simulate the given TM, and if it halts, accept. But no decider exists because we cannot detect the 'loops forever' case in finite time. This asymmetry propagates through all of computability theory — many practical software verification and static analysis problems are undecidable for the same reason."
```

## Explainer

Having studied finite automata and pushdown automata, you have seen increasingly powerful computational models — each one recognizing a strictly larger class of languages than the last. A **Turing machine** represents the final step in this hierarchy: a model powerful enough to capture everything we intuitively mean by "algorithm." The formal definition is a 7-tuple (Q, Σ, Γ, δ, q₀, q_accept, q_reject), where Q is the finite set of states, Σ is the input alphabet (not including the blank symbol), Γ is the tape alphabet (including Σ and the blank symbol), δ is the transition function, q₀ is the start state, and q_accept and q_reject are the accepting and rejecting halt states.

The key difference from previous models is the **infinite read-write tape**. A finite automaton can only read input left-to-right with no memory beyond its current state. A pushdown automaton adds a stack — useful, but limited to last-in-first-out access. A Turing machine has an unbounded tape that it can read from, write to, and move across in both directions. This tape serves simultaneously as the input medium, the working memory, and the output medium. At each step, the machine reads the symbol under its head, and the transition function δ(q, a) specifies three things: the new state to enter, the symbol to write in the current cell, and whether to move the head left or right. This simple loop — read, write, move, change state — is all a Turing machine ever does.

A Turing machine can do one of three things on a given input: **accept** (halt in q_accept), **reject** (halt in q_reject), or **loop forever** (never halt). This three-way distinction is important. A language is **decidable** (recursive) if some TM always halts and correctly accepts or rejects every input. A language is **recognizable** (recursively enumerable) if some TM accepts every string in the language but might loop forever on strings not in it. The difference matters enormously: decidable problems are the ones we can actually solve algorithmically, while merely recognizable problems represent a weaker guarantee where "no" answers may never arrive.

The power of this simple model is captured by the **Church-Turing thesis**: any function that can be computed by any mechanical process — by any programming language, any physical computer, any algorithm described in pseudocode — can be computed by a Turing machine. This is not a theorem (it cannot be proved, since "mechanical process" is informal) but rather a definitional claim that has withstood every attempt at refutation since the 1930s. Every programming language you have ever used, every computer ever built, computes exactly the class of functions that Turing machines compute. Some machines are faster, some use less memory, but none compute anything a Turing machine cannot. This is why the Turing machine serves as the foundation for all of computability and complexity theory: it gives us a single, precise model against which to measure what is and is not computable.

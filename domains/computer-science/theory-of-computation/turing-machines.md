---
id: turing-machines
title: Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pushdown-automata
  type: hard
- id: recursion-basics
  type: soft
- id: cfg-pda-equivalence
  type: soft
- id: pumping-lemma-cfl
  type: soft
- id: formal-logic-propositions
  type: soft
- id: theory-of-computation-overview
  type: soft
builds-toward:
- turing-machine-variants
- church-turing-thesis
- decidability
- time-complexity-classes
tags:
- Turing-machine
- computation
- model
- tape
- decidability
stage: advanced
status: validated
---
# Turing Machines

## Core Idea
A Turing machine (TM) is a finite-state control with an infinite read-write tape. At each step it reads the current tape symbol, writes a new symbol, moves left or right, and transitions to a new state. TMs can accept by entering an accept state, reject by entering a reject state, or loop forever. TMs are the formal model of computation underlying modern computer science — a language is computable if and only if some TM decides it (halting on all inputs). Compared to PDAs, the key power boost is the ability to read and rewrite the tape arbitrarily, not just use a stack.

## How It's Best Learned
Design TMs for simple tasks: copy a string, test if a string is of the form aⁿbⁿ, or increment a binary number. Trace execution on concrete inputs to build intuition for how the tape replaces both the stack and the program's working memory.

## Common Misconceptions
- Thinking a TM is a modern computer — it is an idealized, infinitely-taped mathematical model.
- Confusing a TM that *accepts* (halts in accept state) with one that *decides* (halts on all inputs in either accept or reject state).
- Assuming TMs can only move one direction — the standard model moves left or right, and this bidirectionality is what makes them more powerful than PDAs.

## Questions

```yaml
- question: "Which of the following correctly describes a Turing machine that *decides* a language?"
  type: multiple-choice
  options:
    - "It accepts every string in the language and may loop forever on strings not in it"
    - "It halts on every input, accepting strings in the language and rejecting all others"
    - "It rejects every string not in the language but may loop on strings that are in it"
    - "It always moves rightward and halts when it reaches a blank symbol"
  answer: 1
  explanation: "A decider must halt on all inputs — both accepting members and explicitly rejecting non-members. A recognizer (Turing-acceptable) only guarantees halting on members; it may loop forever on non-members. This accept/reject/loop trichotomy is the central distinction in computability theory."

- question: "A Turing machine is essentially a mathematical model of a modern computer — both have finite memory and equivalent computational power."
  type: true-false
  answer: false
  explanation: "A Turing machine has an *infinite* tape, giving it unbounded working memory — far more idealized than any real computer. Real computers have finite memory, which technically makes them closer to finite automata. The TM is a theoretical abstraction used to define the limits of computation, not a description of physical hardware."

- question: "What is the key property that makes Turing machines more computationally powerful than pushdown automata?"
  type: short-answer
  answer: "The ability to move bidirectionally on an infinite read-write tape, reading and rewriting arbitrary cells — replacing the limited LIFO stack with unrestricted working memory."
  explanation: "PDAs use a stack — last-in, first-out memory that can only be accessed from the top. A TM's tape head can move left or right and rewrite any cell, giving it full random-access working memory. This allows TMs to recognize languages like {aⁿbⁿcⁿ} that PDAs cannot, and underpins the Church-Turing thesis that TMs capture all effectively computable functions."
```

## Explainer

You have already studied pushdown automata (PDAs), which extended finite automata with a stack. That stack was powerful — it let PDAs handle nested structures like balanced parentheses and context-free grammars — but the stack has a fundamental limitation: it is last-in, first-out and can only be accessed from the top. A Turing machine replaces the stack with an infinite tape that the machine can read and write anywhere, moving left or right at each step. This seemingly small change is enormous in computational power.

Formally, a Turing machine consists of a finite set of states, a tape alphabet, an initial state, accept and reject states, and a transition function. At each step, the machine reads the symbol under its tape head, writes a new symbol (possibly the same one), moves the head left or right, and transitions to a new state. Execution can end in three ways: the machine enters the accept state (it accepts the input), enters the reject state (it rejects), or runs forever (it loops). This third possibility — looping — has no analog in finite automata or PDAs, and it is what makes computability theory so rich and subtle.

The accept/decide distinction is the central conceptual divide in computability theory. A TM *recognizes* a language if it accepts every string in the language (though it may loop on strings not in it). A TM *decides* a language if it halts on every input — accepting members and rejecting non-members. Every decidable language is recognizable, but not every recognizable language is decidable. The halting problem is the canonical example of a language that is recognizable but not decidable: a TM can tell you when a program halts (by simulating it until it does), but no TM can always tell you when a program will loop forever.

Turing machines are the formal model underlying the Church-Turing thesis: the claim that any function a human can compute by following a mechanical procedure can also be computed by some Turing machine. This is not a theorem (it cannot be proved, since "mechanical procedure" is informal), but it has withstood every challenge. Quantum computers, parallel computers, and probabilistic machines all turn out to decide exactly the same class of languages as deterministic TMs — they differ in speed, not in what they can compute.

When designing a TM for practice, start simple: write a TM that copies a string, or one that recognizes {aⁿbⁿcⁿ}. Trace execution on a short input, writing out the tape contents and current state at each step. This builds the intuition you need before encountering decidability proofs, where you will argue about what TMs *cannot* do — one of the most surprising and important results in all of theoretical computer science.


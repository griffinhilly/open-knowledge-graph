---
id: hoare-logic
title: Hoare Logic
domain: computer-science
course: formal-methods
prerequisites:
- id: propositional-logic
  type: hard
- id: predicate-logic
  type: hard
- id: programming-language-semantics
  type: hard
builds-toward:
- weakest-precondition
- floyd-hoare-verification
- separation-logic
tags:
- hoare-triple
- partial-correctness
- total-correctness
- program-verification
stage: expert
status: validated
---
# Hoare Logic

## Core Idea
Hoare logic is a formal system for reasoning about the correctness of imperative programs using triples of the form {P} C {Q}, where P is a precondition, C is a command, and Q is a postcondition. The triple asserts that if P holds before executing C, and C terminates, then Q holds afterward (partial correctness). Hoare logic provides axioms and inference rules for each language construct (assignment, sequencing, conditionals, loops), enabling compositional proofs that a program meets its specification.

## Questions

```yaml
- question: "What does the Hoare triple {x > 0} x := x - 1 {x >= 0} assert?"
  type: multiple-choice
  options:
    - "If x > 0 before execution and x := x - 1 terminates, then x >= 0 afterward"
    - "The program x := x - 1 always terminates with x >= 0"
    - "If x >= 0 before execution, then x > 0 afterward"
    - "The assignment x := x - 1 is only valid when x > 0"
  answer: 0
  explanation: "A Hoare triple {P} C {Q} is a partial correctness assertion: it says that IF the precondition P holds before executing C, and IF C terminates, THEN the postcondition Q holds afterward. It does not guarantee termination (that would be total correctness), nor does it constrain when the command may be executed."

- question: "Hoare logic's rule for assignment is {Q[x/E]} x := E {Q}, where Q[x/E] substitutes E for x in Q. This rule works backward from the postcondition, not forward from the precondition."
  type: true-false
  answer: true
  explanation: "The assignment axiom is one of the most counterintuitive aspects of Hoare logic for newcomers. To prove that Q holds after x := E, you must show that Q with E substituted for x held before the assignment. For example, to prove {?} x := x + 1 {x > 5}, substitute x + 1 for x in the postcondition to get the precondition x + 1 > 5, i.e., x > 4. The rule works backward because the assignment determines what must have been true before in order for the postcondition to hold after."

- question: "What is the difference between partial correctness and total correctness in Hoare logic, and which does the standard Hoare triple {P} C {Q} assert?"
  type: short-answer
  answer: "Partial correctness (standard {P} C {Q}) asserts that IF the program terminates, the postcondition holds. Total correctness ([P] C [Q]) asserts that the program DOES terminate and the postcondition holds. Proving total correctness additionally requires showing termination, typically via a well-founded variant (ranking function) that decreases on each loop iteration."
  explanation: "The distinction matters because a non-terminating program trivially satisfies any partial correctness specification — {true} while(true) skip {false} is valid in partial correctness since the program never terminates, so the postcondition is never checked. Total correctness adds the obligation to prove termination, usually by exhibiting a natural-number-valued expression that strictly decreases with each iteration and cannot decrease forever."

- question: "In Hoare logic, the rule of consequence allows strengthening the precondition and weakening the postcondition. Why is this sound?"
  type: short-answer
  answer: "If {P} C {Q} holds and P' implies P (stronger precondition) and Q implies Q' (weaker postcondition), then {P'} C {Q'} holds because: starting from a stronger assumption still guarantees P, so Q holds after execution, and since Q implies Q', Q' holds too. The rule lets you adapt proven triples to fit into larger proof contexts."
  explanation: "The rule of consequence is the 'glue' that makes compositional proofs possible. Without it, you would need each subproof to produce exactly the precondition/postcondition needed by adjacent proof steps. With it, you can prove a triple with natural pre/postconditions and then adjust them to interface with surrounding code."
```

## Explainer

Hoare logic, introduced by Tony Hoare in 1969, provides a rigorous framework for proving that programs meet their specifications. The central object is the **Hoare triple** {P} C {Q}. P is a logical assertion (the precondition) describing what must be true before command C executes; Q (the postcondition) describes what will be true afterward. The triple is a **partial correctness** assertion: it only guarantees Q when C actually terminates. If C loops forever, the triple is vacuously satisfied regardless of Q.

The power of Hoare logic lies in its compositional proof rules — one rule per language construct. The **assignment axiom** {Q[x/E]} x := E {Q} works backward: to establish postcondition Q after assigning E to x, you need Q with E substituted for every occurrence of x to hold beforehand. The **sequencing rule** lets you chain triples: if {P} C1 {R} and {R} C2 {Q}, then {P} C1; C2 {Q}. The **conditional rule** splits on the branch condition: prove the then-branch under the condition and the else-branch under its negation. The **while rule** introduces a loop invariant I: if {I and B} body {I}, then {I} while B do body {I and not B}. Finding the right loop invariant is typically the hardest step in a Hoare logic proof.

The **rule of consequence** is the structural glue. It says: if you can prove {P} C {Q}, and P' implies P and Q implies Q', then {P'} C {Q'} holds. This lets you strengthen preconditions (assume more) and weaken postconditions (promise less), which is always sound. Without this rule, composing subproofs would be impractical because each step's postcondition would need to exactly match the next step's precondition.

A key subtlety is that Hoare logic as described only handles partial correctness — a non-terminating program satisfies any specification. To prove **total correctness**, you must additionally show termination, typically by exhibiting a variant (also called a ranking function): a natural-number-valued expression that decreases with each loop iteration and is bounded below, guaranteeing the loop must eventually exit. This extension connects Hoare logic to well-founded orderings and termination analysis.

Hoare logic provides the conceptual foundation for all subsequent work in program verification. Floyd-Hoare verification automates the process, weakest precondition calculus mechanizes the backward reasoning the assignment axiom uses, and separation logic extends the framework to handle heap-manipulating programs. Understanding Hoare triples and their proof rules is the entry point to the entire field of formal program verification.

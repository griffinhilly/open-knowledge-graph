---
id: mealy-moore-machines
title: Mealy and Moore Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata
  type: hard
- id: finite-state-machines
  type: hard
tags:
- automata
- output-machines
- transducers
stage: advanced
status: validated
---

# Mealy and Moore Machines

## Core Idea
Mealy and Moore machines extend finite automata with output. Moore machines output from states (output = f(state)); Mealy machines output from transitions (output = g(state, input)). Both recognize the same input languages but differ in output timing: Moore machines are synchronous, Mealy machines asynchronous. Both are equivalent in power and widely model digital sequential circuits, protocol controllers, and stateful transducers where input and output are intertwined.

## Questions

```yaml
- question: "A Moore machine and a Mealy machine both implement the same input-output function. Which of the following statements is most likely true about their sizes?"
  type: multiple-choice
  options:
    - "The Moore machine has fewer states because outputs are stored compactly in states rather than on every transition"
    - "The Mealy machine may have fewer states because output differentiation is handled by transition labels rather than requiring separate states"
    - "Both machines must have exactly the same number of states since they compute the same function"
    - "The Mealy machine always has more states because each transition must carry an output symbol"
  answer: 1
  explanation: "In a Moore machine, different outputs require different states — if two transitions into the same state would need to produce different outputs, you must split that state into two. In a Mealy machine, the same state can have different outputs on different outgoing transitions, avoiding the split. This means Mealy machines can often represent the same behavior with fewer states. The equivalence is in computational power, not in machine size."

- question: "A traffic light controller cycles through RED, YELLOW, and GREEN based on a timer. Two designers disagree: one uses a Moore machine, the other a Mealy machine. A student claims the Moore machine is wrong because 'output should depend on the input.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "The student is correct — traffic lights must respond to sensor input, so only Mealy machines are appropriate"
    - "The student is wrong — both models are valid; in the Moore machine, the output (light color) depends only on which phase (state) the controller is in, not on the timer input that triggered the transition"
    - "The student is correct because Moore machines cannot produce multiple distinct output values"
    - "The student is wrong because Moore machines are more powerful than Mealy machines and can handle this case more efficiently"
  answer: 1
  explanation: "Both Moore and Mealy machines can model the traffic light. In the Moore model, the light color is a property of the current state (e.g., the 'RED phase' state always outputs RED), which is perfectly natural when output represents the stable condition of a phase. In the Mealy model, the output is on the transition (e.g., when the timer fires in RED state, output GREEN). Neither is wrong — they are equivalent in power. The student confuses 'output depends on input' (Mealy's definition) with 'output must depend on input' (a false requirement)."

- question: "A Mealy machine is strictly more powerful than a Moore machine — it can recognize languages or compute functions that a Moore machine cannot, because its output depends on both state and input."
  type: true-false
  answer: false
  explanation: "Mealy and Moore machines are equivalent in computational power. Every Mealy machine can be converted to a Moore machine that computes the same input-output function, and vice versa. The difference is where output is associated (transitions vs states), which affects machine size and output timing — but not what functions can be computed. Both are transducers that map finite input sequences to finite output sequences."

- question: "In a Moore machine, the same state always produces the same output regardless of which input symbol or transition sequence led to that state."
  type: true-false
  answer: true
  explanation: "This is definitional: in a Moore machine, output is a function of the current state alone — output = f(state). No matter which path through the automaton led to state q, being in q always produces the same output. This is the fundamental contrast with Mealy machines, where output = g(state, input), so the same state can produce different outputs depending on which input is currently being read."

- question: "Explain why a designer might prefer a Mealy machine over a Moore machine when implementing the same behavior, and give an example of when the Moore machine would require more states."
  type: short-answer
  answer: "A Mealy machine can encode output differentiation in transition labels, so a single state can produce different outputs on different transitions leaving it. A Moore machine must use separate states to produce different outputs, even if those states are otherwise identical in their transition behavior. For example, if a machine must output 0 or 1 depending on whether the current input is A or B, while staying in the same logical 'phase,' a Mealy machine handles this with one state and two labeled transitions; a Moore machine needs two states (one outputting 0, one outputting 1) with identical outgoing transitions."
  explanation: "The key insight is that Mealy machines pack more information into transitions, while Moore machines pack it into states. This is a design trade-off: Moore machines are often simpler to reason about (output is stable within a state), while Mealy machines are often more compact (fewer states needed when output varies within a phase)."
```

## Explainer

The finite automata you studied — DFAs and FSMs — are decision machines: they read input and either accept or reject. But many real systems do more than classify inputs; they *produce output* as they process input. A vending machine does not just decide whether your coin sequence is valid — it dispenses a product and returns change. A traffic light controller does not just accept or reject a stream of sensor readings — it outputs signal colors. **Mealy and Moore machines** extend finite automata with an output mechanism, turning them from recognizers into **transducers** that map input sequences to output sequences.

A **Moore machine** associates its output with *states*. Each state has a fixed output label, and whenever the machine is in a particular state, it emits that state's output regardless of what input symbol it just read. The output depends only on where you are, not on how you got there on this particular step. A **Mealy machine** associates its output with *transitions* instead. Each transition is labeled with both an input symbol and an output symbol, so the output depends on the combination of the current state *and* the input being read. The difference is like two styles of toll booth: a Moore-style booth charges based on which zone you are in (the state), while a Mealy-style booth charges based on which zone you are in *and* which road you took to enter (the transition).

In practice, this difference affects timing and machine size. A Moore machine emits output as soon as it enters a state, before reading the next input — its output is **synchronous** with state changes. A Mealy machine emits output as it processes each input symbol — its output can respond to the current input immediately, making it **asynchronous** in the sense that the output reflects the latest input within the same step. Because of this, Mealy machines can often represent the same behavior with fewer states: the output differentiation that requires separate states in a Moore machine can be handled by labeling transitions differently in a Mealy machine. Every Moore machine can be converted to an equivalent Mealy machine and vice versa, so they are equally powerful — the choice between them is a design preference, not a capability difference.

These machines are foundational in **digital circuit design** and **protocol engineering**. Sequential logic circuits — flip-flops, counters, shift registers — are naturally modeled as Moore or Mealy machines, where states represent stored bit patterns and outputs drive downstream components. Communication protocols, where each received message triggers both a state change and a response message, are textbook Mealy machines. Understanding both models gives you a precise formal language for describing any system that reads input, maintains state, and produces output — which is to say, nearly every interactive system that exists.

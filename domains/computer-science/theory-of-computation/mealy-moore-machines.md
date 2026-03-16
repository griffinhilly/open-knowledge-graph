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
status: draft
---

# Mealy and Moore Machines

## Core Idea
Mealy and Moore machines extend finite automata with output. Moore machines output from states (output = f(state)); Mealy machines output from transitions (output = g(state, input)). Both recognize the same input languages but differ in output timing: Moore machines are synchronous, Mealy machines asynchronous. Both are equivalent in power and widely model digital sequential circuits, protocol controllers, and stateful transducers where input and output are intertwined.

## Explainer

The finite automata you studied — DFAs and FSMs — are decision machines: they read input and either accept or reject. But many real systems do more than classify inputs; they *produce output* as they process input. A vending machine does not just decide whether your coin sequence is valid — it dispenses a product and returns change. A traffic light controller does not just accept or reject a stream of sensor readings — it outputs signal colors. **Mealy and Moore machines** extend finite automata with an output mechanism, turning them from recognizers into **transducers** that map input sequences to output sequences.

A **Moore machine** associates its output with *states*. Each state has a fixed output label, and whenever the machine is in a particular state, it emits that state's output regardless of what input symbol it just read. The output depends only on where you are, not on how you got there on this particular step. A **Mealy machine** associates its output with *transitions* instead. Each transition is labeled with both an input symbol and an output symbol, so the output depends on the combination of the current state *and* the input being read. The difference is like two styles of toll booth: a Moore-style booth charges based on which zone you are in (the state), while a Mealy-style booth charges based on which zone you are in *and* which road you took to enter (the transition).

In practice, this difference affects timing and machine size. A Moore machine emits output as soon as it enters a state, before reading the next input — its output is **synchronous** with state changes. A Mealy machine emits output as it processes each input symbol — its output can respond to the current input immediately, making it **asynchronous** in the sense that the output reflects the latest input within the same step. Because of this, Mealy machines can often represent the same behavior with fewer states: the output differentiation that requires separate states in a Moore machine can be handled by labeling transitions differently in a Mealy machine. Every Moore machine can be converted to an equivalent Mealy machine and vice versa, so they are equally powerful — the choice between them is a design preference, not a capability difference.

These machines are foundational in **digital circuit design** and **protocol engineering**. Sequential logic circuits — flip-flops, counters, shift registers — are naturally modeled as Moore or Mealy machines, where states represent stored bit patterns and outputs drive downstream components. Communication protocols, where each received message triggers both a state change and a response message, are textbook Mealy machines. Understanding both models gives you a precise formal language for describing any system that reads input, maintains state, and produces output — which is to say, nearly every interactive system that exists.

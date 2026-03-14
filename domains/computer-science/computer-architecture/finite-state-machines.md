---
id: finite-state-machines
title: Finite State Machines (FSMs)
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
- id: combinational-circuit-design
  type: hard
- id: set-theory-basics
  type: soft
- id: boolean-algebra
  type: soft
builds-toward:
- sequential-circuit-design
- cpu-control-unit
tags:
- FSM
- Moore
- Mealy
- sequential-logic
- state-machine
stage: formal-systems
status: validated
---

# Finite State Machines (FSMs)

## Core Idea
A finite state machine (FSM) is a model of a sequential system with a finite number of discrete states. At each clock edge, the system transitions to a next state determined by the current state and the inputs (next-state logic). Outputs are produced either as a function of the current state only (Moore machine) or of both state and inputs (Mealy machine). FSMs are implemented in hardware using flip-flops to hold state and combinational logic for the transition and output functions, and they model everything from traffic lights to CPU control units.

## How It's Best Learned
Design FSMs for simple problems like a sequence detector or vending machine controller. Draw the state diagram, derive the state transition table, assign binary encodings, and implement with flip-flops and combinational logic. Verify with timing diagrams.

## Common Misconceptions
- Moore and Mealy machines are equally expressive; a Moore FSM can be converted to a Mealy FSM with fewer states, and vice versa.
- State encoding (one-hot vs. binary) is an implementation choice that affects logic complexity and speed but does not change the FSM's behavior.

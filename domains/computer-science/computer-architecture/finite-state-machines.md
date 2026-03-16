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
- id: formal-languages-and-strings
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

## Questions

```yaml
- question: "In a Moore machine that controls a traffic light, the light color (red, green, yellow) is determined by:"
  type: multiple-choice
  options:
    - "The current input signal from a car sensor"
    - "Both the current state and the current input"
    - "The current state alone"
    - "The previous state and the previous input"
  answer: 2
  explanation: "In a Moore machine, outputs are a function of the current state only — not the current inputs. Each state has a fixed output associated with it. This means the light color is determined entirely by which state the FSM is currently in, regardless of what the sensor is doing right now. A Mealy machine would instead allow the output to vary based on both state and input."

- question: "A Mealy machine always requires more states than an equivalent Moore machine to recognize the same behavior."
  type: true-false
  answer: false
  explanation: "It is actually the opposite: a Mealy machine often requires *fewer* states than the equivalent Moore machine. In a Mealy FSM, outputs are associated with transitions (state + input), so a single state can produce different outputs depending on the input. A Moore FSM must create separate states to produce different outputs, which can increase the state count. Both models are equally expressive — any FSM in one form can be converted to the other."

- question: "Why does a finite state machine require flip-flops, while a combinational circuit does not?"
  type: short-answer
  answer: "An FSM must remember its current state across clock cycles, but combinational circuits have no memory — their output is a pure function of current inputs. Flip-flops are edge-triggered memory elements that store the current state register and update it once per clock cycle, giving the FSM its ability to exhibit time-dependent (sequential) behavior."
  explanation: "This connects to the prerequisite topic: combinational circuits compute a function with no stored state; adding flip-flops creates a sequential circuit. The FSM architecture is exactly this: combinational logic computes the next state and the output, while flip-flops hold the current state. Without the flip-flops, the 'state' would immediately change as inputs changed, making the machine combinational rather than sequential."
```

## Explainer

A combinational circuit computes a pure function of its current inputs — it has no memory of what happened before. This is powerful but limiting. Real-world controllers — traffic lights, elevator controllers, CPU control units — need to remember where they are in a sequence. That is exactly what a finite state machine adds: a finite set of discrete states that summarize all the history the system needs.

An FSM is defined by five elements: a set of states, an input alphabet, a transition function (current state + input → next state), an output function, and an initial state. The state diagram is the most intuitive representation: circles are states, arrows are transitions labeled with inputs (and sometimes outputs). When you design an FSM for a problem, you start with the state diagram — drawing out every situation the system needs to distinguish — before thinking about gates.

The two classic variants differ in where outputs are placed. In a **Moore machine**, each state has a fixed output label; the output depends only on the current state. In a **Mealy machine**, outputs are labels on transitions; the output depends on both the current state and the current input. Moore machines are easier to reason about and produce glitch-free outputs (since outputs only change at clock edges when state changes). Mealy machines typically require fewer states to achieve the same behavior because a single state can emit different outputs depending on the input. Both models are equally powerful — you can always convert one to the other.

Hardware implementation connects directly to your combinational circuit design knowledge. The FSM has two parts: (1) **next-state logic** — a combinational circuit that takes the current state bits and inputs and computes what state to move to; and (2) **output logic** — another combinational circuit (or a direct wiring for Moore outputs) that produces the outputs. The current state is held in a register of flip-flops, one per state bit. At every rising clock edge, the flip-flops capture the next-state logic's output and the system advances to the new state.

When implementing, you must also choose a **state encoding** — how to represent each state as a binary number stored in the flip-flops. Binary encoding uses the minimum number of flip-flops (⌈log₂ n⌉ for n states), while one-hot encoding uses one flip-flip per state (exactly one flip-flop is 1 at all times). Binary encoding is more compact; one-hot encoding produces simpler next-state logic because checking "are we in state X?" is just reading a single flip-flop. The choice affects the complexity of your combinational logic but not the FSM's observable behavior.

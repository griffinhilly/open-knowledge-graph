---
id: multiplexers-and-demultiplexers
title: Multiplexers and Demultiplexers
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-circuit-design
  type: hard
builds-toward:
- cpu-datapath
- registers-and-register-files
tags:
- multiplexer
- demultiplexer
- data-routing
- combinational
stage: formal-systems
status: validated
---

# Multiplexers and Demultiplexers

## Core Idea
A multiplexer (MUX) selects one of several input signals and routes it to a single output, controlled by select lines. An n-to-1 MUX has log₂(n) select bits. A demultiplexer (DEMUX) routes a single input to one of several outputs. Multiplexers are universal: any Boolean function can be implemented with a single large enough MUX. In CPU datapaths, MUXes select operands, route results, and switch between different data sources based on control signals.

## How It's Best Learned
Draw a 4-to-1 MUX schematic from its truth table, then implement it with basic gates. Practice implementing arbitrary Boolean functions using a MUX's select lines as inputs. Trace MUX use in a simple CPU datapath diagram.

## Common Misconceptions
- The select lines of a MUX are control inputs, not data inputs — they determine which data channel is active, not what value is output.
- A MUX is not the same as a decoder; they perform complementary but different routing functions.

## Questions

```yaml
- question: "A designer wants to implement a 3-variable Boolean function using only a single MUX, exploiting its universality. What is the minimum MUX size needed, and how is it connected?"
  type: multiple-choice
  options:
    - "A 4-to-1 MUX, using 2 variables as select lines and computing the third with a gate"
    - "An 8-to-1 MUX, using all 3 variables as select lines and hardwiring truth table output values to the data inputs"
    - "Three cascaded 2-to-1 MUXes, one per variable"
    - "A 4-to-1 MUX with all three variables driving the inputs simultaneously"
  answer: 1
  explanation: "MUX universality works as follows: for an n-variable function, use a 2ⁿ-to-1 MUX. Apply all n variables to the select lines — these enumerate every possible input combination. Then hardwire each data input to the corresponding output value from the truth table (0 or 1). For a 3-variable function, the 8-to-1 MUX's select lines step through all 8 input combinations, and the data inputs directly encode the truth table. No additional logic gates are needed — the MUX itself implements the entire function."

- question: "What is the correct structural relationship between a 1-to-4 demultiplexer and a 2-to-4 decoder?"
  type: multiple-choice
  options:
    - "They are identical circuits described with different terminology"
    - "A DEMUX is a decoder with its enable input serving as the data line — the active output receives the data value, others stay at 0"
    - "A decoder is a DEMUX with extra outputs added for unused address combinations"
    - "They are unrelated circuits that happen to have the same number of outputs"
  answer: 1
  explanation: "A 2-to-4 decoder takes 2 select inputs and asserts exactly one of 4 outputs. A 1-to-4 DEMUX has the same structure, except its single data input acts as an enable: the selected output receives whatever value is on the data line, while the others remain 0. This is structurally identical to a decoder with an enable pin. A decoder without an enable is a DEMUX with its data input permanently tied to logic 1. The select lines determine which output is active; the data input controls what that active output carries."

- question: "A 4-to-1 MUX can implement any Boolean function of exactly 2 variables by hardwiring the four truth table output values to its data inputs and using the two variables as select lines."
  type: true-false
  answer: true
  explanation: "This is precisely the universality property. A 4-to-1 MUX with two select lines (S1, S0) enumerates all four input combinations: 00, 01, 10, 11. By wiring D0–D3 to the corresponding output values from the truth table, the MUX reads out the correct output for any combination of the two variables. Since every Boolean function of 2 variables is fully specified by its 4-row truth table, the MUX can implement all of them — AND, OR, XOR, NAND, and every other 2-input function — simply by changing the data input wiring."

- question: "The output of a 2-to-1 MUX with select line S = 0 depends on both data inputs D0 and D1."
  type: true-false
  answer: false
  explanation: "When S = 0, a 2-to-1 MUX outputs exactly D0 — D1 is completely ignored. The Boolean expression Y = S'·D0 + S·D1 makes this explicit: when S = 0, the term S·D1 = 0, so Y = D0 regardless of D1's value. This is the core function of a MUX: it selects exactly one input and routes it to the output. Unselected inputs have no effect on the output — a MUX routes, it does not combine inputs the way an OR gate does."

- question: "Why are multiplexers considered 'universal' logic elements? Explain the key insight that makes any Boolean function implementable with a single large enough MUX."
  type: short-answer
  answer: "A MUX with n select lines and 2ⁿ data inputs can implement any n-variable Boolean function: apply the n input variables to the select lines, and hardwire each data input to the corresponding truth table output value. For any combination of variable values, the select lines route exactly that row's truth table entry to the output. Since every Boolean function is completely defined by its truth table, and the MUX can encode any truth table, it can implement any Boolean function."
  explanation: "The universality insight is that select lines enumerate input combinations while data inputs store corresponding outputs — the MUX is a hardware lookup table. This makes MUXes powerful for reconfigurable logic: changing the data input wiring changes the implemented function without altering the select structure. FPGAs exploit exactly this principle: their programmable logic elements are essentially lookup tables that implement any Boolean function of their inputs by storing the truth table in configurable memory."
```

## Explainer

From your work with combinational circuit design, you know how to build circuits that compute Boolean functions using gates. A **multiplexer** (MUX) is a specific combinational circuit that acts as a digitally controlled switch: it has several data inputs, a set of select lines, and one output. The select lines determine which input gets routed to the output. Think of it like a railroad switch — multiple tracks converge, and a control lever picks which one connects through to the main line.

A **2-to-1 MUX** is the simplest case: two data inputs (D0 and D1), one select line (S), and one output (Y). When S = 0, the output equals D0; when S = 1, the output equals D1. The Boolean expression is Y = S'·D0 + S·D1, which you can implement directly with two AND gates, one NOT gate, and one OR gate. Scaling up, a **4-to-1 MUX** has four data inputs and two select lines, an **8-to-1 MUX** has eight inputs and three select lines, and in general an n-to-1 MUX requires log₂(n) select lines. Larger MUXes can be built by cascading smaller ones — two 4-to-1 MUXes feeding into a 2-to-1 MUX create an 8-to-1 MUX.

One of the most powerful properties of multiplexers is their **universality**: any Boolean function of n variables can be implemented using a single 2^n-to-1 MUX by hardwiring the truth table values to the data inputs and using the function's variables as select lines. For example, to implement a 3-variable function, connect the eight rows of its truth table (each either 0 or 1) to the eight data inputs of an 8-to-1 MUX, and use the three variables as select lines. This makes MUXes a practical alternative to sum-of-products implementations, especially when the function is complex or needs to be reconfigurable.

A **demultiplexer** (DEMUX) performs the inverse operation: it takes a single data input and routes it to one of several outputs based on the select lines. All other outputs remain inactive (typically 0). A DEMUX is structurally identical to a decoder with an enable input — the data input serves as the enable, and the select lines determine which output receives it. In practice, MUXes and DEMUXes often work as pairs: a DEMUX at the sending end distributes data across multiple channels, and a MUX at the receiving end selects which channel to listen to. In CPU datapaths, multiplexers are everywhere — selecting between register values and immediate operands, choosing which ALU result to write back, deciding whether the next program counter comes from an increment or a branch target. Understanding MUXes is essential to reading any datapath diagram.

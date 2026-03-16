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

## Explainer

From your work with combinational circuit design, you know how to build circuits that compute Boolean functions using gates. A **multiplexer** (MUX) is a specific combinational circuit that acts as a digitally controlled switch: it has several data inputs, a set of select lines, and one output. The select lines determine which input gets routed to the output. Think of it like a railroad switch — multiple tracks converge, and a control lever picks which one connects through to the main line.

A **2-to-1 MUX** is the simplest case: two data inputs (D0 and D1), one select line (S), and one output (Y). When S = 0, the output equals D0; when S = 1, the output equals D1. The Boolean expression is Y = S'·D0 + S·D1, which you can implement directly with two AND gates, one NOT gate, and one OR gate. Scaling up, a **4-to-1 MUX** has four data inputs and two select lines, an **8-to-1 MUX** has eight inputs and three select lines, and in general an n-to-1 MUX requires log₂(n) select lines. Larger MUXes can be built by cascading smaller ones — two 4-to-1 MUXes feeding into a 2-to-1 MUX create an 8-to-1 MUX.

One of the most powerful properties of multiplexers is their **universality**: any Boolean function of n variables can be implemented using a single 2^n-to-1 MUX by hardwiring the truth table values to the data inputs and using the function's variables as select lines. For example, to implement a 3-variable function, connect the eight rows of its truth table (each either 0 or 1) to the eight data inputs of an 8-to-1 MUX, and use the three variables as select lines. This makes MUXes a practical alternative to sum-of-products implementations, especially when the function is complex or needs to be reconfigurable.

A **demultiplexer** (DEMUX) performs the inverse operation: it takes a single data input and routes it to one of several outputs based on the select lines. All other outputs remain inactive (typically 0). A DEMUX is structurally identical to a decoder with an enable input — the data input serves as the enable, and the select lines determine which output receives it. In practice, MUXes and DEMUXes often work as pairs: a DEMUX at the sending end distributes data across multiple channels, and a MUX at the receiving end selects which channel to listen to. In CPU datapaths, multiplexers are everywhere — selecting between register values and immediate operands, choosing which ALU result to write back, deciding whether the next program counter comes from an increment or a branch target. Understanding MUXes is essential to reading any datapath diagram.

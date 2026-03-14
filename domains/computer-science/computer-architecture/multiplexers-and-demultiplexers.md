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
